# Cloud-Resume
Deploying a shorten version of my current resume into the cloud with AWS. 
**Amazon Web Services used:**
- S3
- Amazon Route 53
- Certificate Manager
- Cloudfront
- Lambda
- DynamoDB

## [Live Demo](https://han-pham-resume.click/)

## Project Description 
The purpose is this project to practice AWS by deploying a shorten version of my resume. 

- Created a resume using HTML and CSS.
- Used a custom domain name using Amazon Route 53.
- Utilized S3 bucket to host the simplified resume.
- Updated records to point to the S3 website endpoints. 
- Setted up SSL/HTTPS with AWS Certificate Manager. 
- Created a Cloudfront Distribution.

## Future Implementations 
This resume is a part of the [Cloud Resume Challenge](https://cloudresumechallenge.dev/docs/the-challenge/aws/).

I hope to implement the following:
1) Javascript (To count the number of visitors that have accessed this site).
2) Adding a Database (Amazon's DynamoDB to save and update the visitor count).
3) Implementing an API that communicates with my web application and the DB.
