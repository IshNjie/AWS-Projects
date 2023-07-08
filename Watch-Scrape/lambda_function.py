import requests
from bs4 import BeautifulSoup
import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event,context):

    bucket = 'watch-glue-input-bucket'
    
    url = 'https://www.goldsmiths.co.uk/c/Watches/Mens-Watches'
    
    resp = requests.get(url)
    
    soup = BeautifulSoup(resp.content,'html.parser')
    
    firstpage = soup.find_all('div','productTile firstPage')
    maxpage = soup.find(id='pagination-LoadMore')['data-total-pages']
    
    data_list = []
    
    for i in range(0,len(firstpage)):
        item = {}
        item['Brand'] = firstpage[i].find_all('div','productTileBrand')[0].text
        item['Name'] = firstpage[i].find_all('div','productTileName')[0].text
        item['Price'] = firstpage[i].find_all('div','productTilePrice')[0].text.replace('£','').replace(",", "").strip().split('\n')[0]
        item['Ref.Number'] = firstpage[i].find_all('a')[0].get('href').split('-')[-1]
        
        data_list.append(item)
    
    
    for page_number in range(1,int(maxpage)):
        n_page_link = 'https://www.goldsmiths.co.uk/c/Watches/Mens-Watches?q=%3Arelevance&page={}&sort=relevance'.format(page_number)
    
    
        respNext = requests.get(n_page_link)
        soupNext = BeautifulSoup(respNext.content,'html.parser')
    
        Nextpage = soupNext.find_all('div','productTile')
    
        for i in range(0,len(Nextpage)):
            itemNext = {}
            itemNext['Brand'] = Nextpage[i].find_all('div','productTileBrand')[0].text
            itemNext['Name'] = Nextpage[i].find_all('div','productTileName')[0].text
            itemNext['Price'] = Nextpage[i].find_all('div','productTilePrice')[0].text.replace('£','').replace(",", "").strip().split('\n')[0]
            itemNext['Ref.Number'] = Nextpage[i].find_all('a')[0].get('href').split('-')[-1]
    
            data_list.append(itemNext)
    
    #data_list = json.dumps(data_list, separators=(',', ':'))
    data_list = ', \n'.join(json.dumps(item,indent = 4, separators=(',', ':')) for item in data_list).encode('UTF-8') 
    uploadByte = bytes(data_list)
    s3.put_object(Bucket = bucket,Key='Watches1.json',Body=uploadByte)
    
    print('Put Complete to S3 Bucket')