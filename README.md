# Udemy API Module

Simple Python module that accesses the Udemy API.

This project uses Docker to build the AWS lambda against Python 2.7.

## Prerequisites

Ensure that you have the following installed:

### Docker

Ensure that you have built the Dockerfile:

    build . -t puffinz/lambda-maker

### AWS

Ensure that you have an AWS S3 bucket created. This lambda will write to this
bucket.

### Virtualenv

Install virtualenv with: 

    pip install virtualenv

### Configuration

Rename the `udemy_api/config/settings_example.cfg` file, to `udemy_api/config/settings_example.cfg`.  
Edit the `udemy_api/config/settings.cfg` file.

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


# TODO

* change python module to work as a lambda
* use LZO to compress raw course page data
* structure udemy page key
* use sns to pass the next page to the lambda
* investigate SNS for sending 'next' page scrapes to lambda
* investigate cost of lambda scrapes and sns/sqs/etc implementation


