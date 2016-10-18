#!/usr/bin/env python

import sys
import json
import boto3


def parse_params(argv):
    size = len(argv)
    if size != 2 and size != 3:
        print ('Usage: lambda_client.py region lambda_function_name')
        return -1
    elif size == 2:
        url = 'https://www.udemy.com/api-2.0/courses?page_size=100'
    else:
        url = argv[2]
    return { 'region': argv[0], 'lambda_name': argv[1], 'url': url }


def main(argv):
    params = parse_params(argv)
    if params == -1:
        return
    payload = {'url': params['url']}
    payload_json = json.dumps(payload)

    print('Invoking lambda...')
    print(payload)
    lambda_client = boto3.client('lambda', region_name=params['region'])
    response = lambda_client.invoke(FunctionName=params['lambda_name'],
                                    InvocationType='RequestResponse', LogType='None',
                                    Payload=payload_json)
    body = response['Payload'].read()
    body_dict = json.loads(body)
    print(body_dict)

    if response['StatusCode'] != 200:
        print ('Error connecting to lambda!')
        return -1

    return 0

if __name__ == '__main__':
    main(sys.argv[1:])

