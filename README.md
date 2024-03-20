# Cloud-Resume
A shorten version of my current resume into the cloud with AWS. 
### [Live Demo](https://han-pham-resume.click/)
### AWS currently used:
- S3
- Amazon Route 53
- Certificate Manager
- Cloudfront
- Lambda
- DynamoDB

## Project Description 
The purpose is this project to practice AWS by deploying a shorten version of my resume. This resume is a part of the [Cloud Resume Challenge](https://cloudresumechallenge.dev/docs/the-challenge/aws/). I will be following this challenge to learn more about the cloud. 
### Part 1: Secure, static website with a custom domain 
- Created a resume using HTML and CSS.
- Used a custom domain name using Amazon Route 53.
- Utilized S3 bucket to host the simplified resume.
- Updated records to point to the S3 website endpoints. 
- Setted up SSL/HTTPS with AWS Certificate Manager. 
- Created a Cloudfront Distribution.
### Part 2: Counting visitors + making an API 
- Created lambda function to get count of visitors viewing the resume site.
- Added DynamoDB table to save/update visitor count.
- Developed an API using Lambda services to facilitate communication between a web application and DynamoDB.
### OPTIONAL: Part 3: Source Control + IaC using Terraform

## Future Implementations 
I hope to implement the following:
- [x] Javascript (To count the number of visitors that have accessed this site).
- [x] Adding a Database (Amazon's DynamoDB to save and update the visitor count).
  [] Optional: Implement Terraform  
