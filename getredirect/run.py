import os
import json

short = os.environ['REQ_PARAMS_SHORT']

res = { "status": 301,
        "headers": { "location": "https://aka.ms/" + str(short) },
        "body": None}

# Output the response to the client

output = open(os.environ['response'], 'w')
output.write(json.dumps(res))