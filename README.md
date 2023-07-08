# AWS Projects

## Overview

This repo will be used to demonstrate some projects that I have implemented using the Free Tier offered by AWS. 

As a Data Engineer, I am always looking to improve my skills and gain exposure to new technologies. 

# 

## Project Overviews

### 1. [ETL using Glue](/ETL-Glue/)

#### Overview 
In this project, we will build upon the Watch Scrape project and transform the data in our S3 bucket and load to an output S3 bucket. Find the file here: Lambda Function

#### Challenges
The main challenge was dealing with the output `.json` file from Lambda. I had to configure the Lambda function to output the `.json` file in the correct format. 

### 2. [Streamlit App Host using EC2](/Streamlit-app-host/)

#### Overview
In this project, we will configure an AWS EC2 Instance to host our Streamlit app. Our Streamlit app is one that allows users to receive recommendations for gym exercises. I have a separate repo for this app [here](https://github.com/IshNjie/Exercise_Recommender)


#### Challenges

1. Copying over the folder, I have to familiarize myself more with Linux commands. 
2. Configuring the Inbound Rules, I assumed HTTP and HTTPS rules were enough, but I had to configure a custom rule for the port 8501
3. I still need to configure the app to run continuously within the EC2 Instance: https://www.youtube.com/watch?v=3sQhVKO5xAA


### 3. [Web Scraping using Lambda](/Watch-Scrape/)

#### Overview
In this project, we will configure a Lambda function to scrape a website with watch prices and load that into an S3 bucket.


#### Challenges

1. Testing did not immediately work for me. I had to deploy my function every time I wanted to test

2. I had to learn how to bring in the Python dependencies via a zip file. Size was an issue so I had to be selective as to which packages I zipped up

3. I had to change the time out configuration to increase the time to 10 minutes.

4. I had to reinstall a version of urllib 


