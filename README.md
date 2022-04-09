# ResidentAPI
The residentAPI contains following APIs for ResidentPortal,

1) Admin/Resident Login API 
2) Add Resident API
3) Add Service Request API
4) Manage Service Request API

# List of AWS Services used in this project

1) DynamoDB: For storing resident and service request data.
2) Cognito: For storing Administrator data.
3) SNS: To send notification in project.
4) S3: For storing service request documents.
5) CloudFront: To provide content delivery of S3 objects.
6) CloudFormation: The above services are configured using cloud formation.

The ResidentAPI is used in the https://github.com/krishnajadav/residentWebPortal project.
