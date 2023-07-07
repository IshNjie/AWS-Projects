# Web Scrape - Lambda & S3

AWS S3 stands for Amazon Simple Storage Service. It is a storage service that permits the storage for large sums of data, of varying formats. Azure Blob Storage would be it's counterpart in the Microsoft world. 

S3 consists of buckets and objects. Buckets are a container to store data within; the objects would be the data you store within the buckets.

AWS Lambda is a serverless compute service. This allows the user to run code without managing servers/VMs (EC2 for example). Lambda supports a whole host of languages.

In this project, we will configure a Lambda function to scrape a website with watch prices and load that into an S3 bucket.

![ArchDiag](Images/ArchDiag.png)

#

## Steps

1. Create Account and navigate to `S3` via the services dashboard. 

2. Create bucket

This step is pretty straight forward and I kept the default settings for the bucket configuration

3. Navigate to `Lambda` via the services dashboard and create a Lambda Function

4. Create a new role

This role will need to have policies that allow the function to write to an S3 bucket.

![Role](Images/RoleCreate.png)

Head to the IAM Console to start this process

5. Choose Service for Role to interact with (use case)

![LambdaRole](Images/LambdaRole.png)

6. Create a new policy

The reason we create a new policy here is so that we can configure write access to the S3 bucket

![NewPol](Images/NewPol.png)

Then we name our new policy and `Create Policy`

![namePol](Images/NamePol.png)

7. Head back to create Role and select the new policy just set up

![addPol](Images/RoleAddPol.png)

Follow through, give the Role a name and `Create Role`

8. Head back to our Lambda Function and add the new existing role

You might need to refresh the list for it to show up

Also, do not forget to configure the Runtime to the language of your choice

![selectRole](Images/SelectRole.png)

`Create Function` and visit the UI

![LambdaUI](Images/LambdaUI.png)

9. Bring in Python dependencies 

On my local machine, I created a virtual environment and only installed the packages I needed for this project

```
pip install beautifulsoup4
pip install requests
```

Following that, I gathered the packages and compressed them into a zip file. Next, you could either, upload the zip file directly into the code editor area using the `Upload from` button, or first, upload the zip file to s3 then read from the URL (destination of the zip file in S3). I chose the latter.

### Caution!

Uploading large zip files will result in the code editor not being accessible to deploy and test. 

10. Amend the code in the .py file, deploy and test.

The test event is simple, navigate to test and `configure test event`

![test](Images/testEvent.png)

Give your test a name and hit `Save`

Once you test your code, you should see a response like this:

![executeRes](Images/execute.png)

To verify this has worked, go and check your `S3 bucket`:

![s3Bucket](Images/s3bucket.png)

Here, the new .json file `Watches1.json` is now in my S3 bucket. This data shows the Brand, Name, Price and Reference Number of a watch on https://www.goldsmiths.co.uk/c/Watches/Mens-Watches

## Challenges

Some Challenges included:

1. Testing did not immediately work for me. I had to deploy my function every time I wanted to test

2. I had to learn how to bring in the Python dependencies via a zip file. Size was an issue so I had to be selective as to which packages I zipped up

3. I had to change the time out configuration to increase the time to 10 minutes.

4. I had to reinstall a version of urllib 

https://stackoverflow.com/questions/76414514/cannot-import-name-default-ciphers-from-urllib3-util-ssl-on-aws-lambda-us

```
pip install --force-reinstall -v "urllib3==1.26.15"
```


