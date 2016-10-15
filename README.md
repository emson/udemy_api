# Udemy API Module

Simple Python module that accesses the Udemy API.

This project uses Docker to build the AWS lambda against Python 2.7.

## Prerequisites

Ensure that you have the following installed:

### Docker

Ensure that you have built the Dockerfile:

    build . -t puffinz/lambda-maker

### Virtualenv

Install virtualenv with:

    pip install virtualenv

### Configuration

Rename the `udemy_api/config/settings_example.cfg` file, to `udemy_api/config/settings_example.cfg`.
Edit the `udemy_api/config/settings.cfg` file.

    [Udemy]
    udemy_courses_url = <INSERT UDEMY URL>
    udemy_client_id = <INSERT UDEMY API CLIENT ID>
    udemy_client_secret =<INSERT UDEMY API CLIENT SECRET KEY>

    [AWS]
    AWS_BUCKET = <INSERT YOUR AWS BUCKET NAME>

## Running

Use Docker to build your lambda:

    docker run  -v "$PWD":/build  puffinz/lambda-maker

This builds a zip file in the `package` directory.

## Build locally

This project can be built without using Docker, however it may not work if you
need to compile against any binaries.

To build locally create a new virtualenv environment:

    virtualenv ./env &&  . ./env/bin/activate
    make clean build package
    deactivate

### AWS

Ensure that you have an AWS S3 bucket created, with the same name as that
created in the `settings.cfg` file. This lambda will write to this
bucket.

On the AWS Lambda service create a new lambda function:

1. Click the "Create a Lambda function" button
2. Select the "Blank Function" blueprint
3. Click "Next" (no triggers)
4. Name "UdemyApi"
5. Runtime "Python 2.7"
6. Code entry type "Upload .ZIP file"
7. Click the "Upload" button and select the .zip file from the `package`
   directory
8. Handler should be "udemy_api.lambda_handler"
9. Role "Choose an existing role"
10. Existing role "<ENSURE YOU HAVE CREATED A ROLE>"
11. Set Timeout to about "15" seconds
12. Click "Next" and then "Create Function"
13. Click the "Test" button
14. Use the Sample event template "Hello World"
15. Finally click the "Save and Test" button




# TODO

* change python module to work as a lambda
* use LZO to compress raw course page data
* structure udemy page key
* use sns to pass the next page to the lambda
* investigate SNS for sending 'next' page scrapes to lambda
* investigate cost of lambda scrapes and sns/sqs/etc implementation


