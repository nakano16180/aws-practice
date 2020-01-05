from __future__ import print_function
import os
import sys
import subprocess

import pprint
# Just a test lambda, run with:
# docker run --rm -v "$PWD":/var/task lambci/lambda:python2.7
# OR
# docker run --rm -v "$PWD":/var/task lambci/lambda:python3.6
# OR
# docker run --rm -v "$PWD":/var/task lambci/lambda:python3.7 lambda_function.lambda_handler

def lambda_handler(event, context):
    context.log('Hello!')
    context.log('Hmmm, does not add newlines in 3.7?')
    context.log('\n')

    print(sys.executable)
    print(sys.argv)
    print(os.getcwd())
    print(__file__)
    
    print('#######################')
    print('AWS_ACCESS_KEY_ID', os.environ.get('AWS_ACCESS_KEY_ID'))
    print('AWS_SECRET_ACCESS_KEY', os.environ.get('AWS_SECRET_ACCESS_KEY'))
    
    print('#######################')
    pprint.pprint(os.environ)
    pprint.pprint(context.__dict__)

    return {
        "executable": str(sys.executable),
        "sys.argv": str(sys.argv),
        "os.getcwd": str(os.getcwd()),
        "__file__": str(__file__),
        "os.environ": str(os.environ),
        "context.__dict__": str(context.__dict__),
        "event": event
    }
