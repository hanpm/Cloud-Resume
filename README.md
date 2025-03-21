# Cloud-Resume 
A shorten version of my current resume into the cloud with AWS. 

<details>
<summary><b>Services used</b></summary>
<br>
  <ul>
    <li>Amazon Route 53</li>
    <li>S3</li>
    <li>Certificate Manager</li>
    <li>Cloudfront</li>
    <li>Lambda</li>
    <li>DynamoDB</li>
    <li>IAM</li>
    <li>Github Actions</li>
    <li>Terraform</li>
  <ul>
</details>

## Project Description 
The purpose is this project to practice AWS by deploying a shorten version of my resume. This resume is a part of the [Cloud Resume Challenge](https://cloudresumechallenge.dev/docs/the-challenge/aws/). I will be following this challenge to learn more about the cloud. 
### Part 1: Secure, static website with a custom domain 
- [x] Created a resume using HTML and CSS.
- [x] Used a custom domain name using Amazon Route 53.
- [x] Utilized S3 bucket to host the simplified resume.
- [x] Setted up SSL/HTTPS with AWS Certificate Manager. 
- [x] Created a Cloudfront Distribution to make site secure.
### Part 2: Counting visitors with DynamoDB & Lambda functions
- [x] Created lambda function to get count of visitors viewing the resume site.
- [x] Added DynamoDB table to save/update visitor count.
- [x] Developed an API using Lambda services to facilitate communication between a web application and DynamoDB.
### OPTIONAL Part 3: Integrating CI/CD pipeline for Frontend
- [x] Created new IAM user for Github Actions
- [x] Used Github Actions to create CI/CD pipeline.
- [x] CI/CD pipeline syncs the S3 bucket and clears the CloudFront cache.  
### OPTIONAL Part 4: IaC using Terraform
**Implementing terraform for my AWS lambda function:**
- [x] Created IAM user with appropriate permissions for Terraform
- [x] Configured AWS credentials, initialized Terraform in project 
- [x] Attached Lambda function and any other policies it depends on to .tf files

## Future Implementations 
I hope to implement the following:
- [x] Javascript (To count the number of visitors that have accessed this site).
- [x] Adding a Database (Amazon's DynamoDB to save and update the visitor count).
- [x] CI/CD pipeline
- [x] Try implementing Terraform for my lambda function
- [ ] Now, try implementing Terraform for S3 bucket
