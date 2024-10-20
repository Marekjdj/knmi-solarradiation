#!/usr/bin/python3

import requests
import datetime
import json
import yaml

with open('/config/secrets.yaml', 'r') as f:
    knmi_token = yaml.safe_load(f)['knmi_token']

location = ""

payload={}
headers = {'Authorization': knmi_token}

now = datetime.datetime.now(datetime.UTC).replace(tzinfo=None)

# Round down to the nearest 10-minute interval
rounded = now - datetime.timedelta(minutes=now.minute % 10,seconds=now.second,microseconds=now.microsecond)

# Subtract 10 minutes from the rounded time
start_time = rounded - datetime.timedelta(minutes=10)

list = []

for i in range(2):
    # format the datetime object into RFC 3339 timestamp
    rfc3339 = start_time.replace(microsecond=0).isoformat('T') + 'Z'
    url = f"https://api.dataplatform.knmi.nl/edr/v1/collections/observations/locations/{location}?datetime={rfc3339}&parameter-name=q_glob_10"
    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text)
    try:
        value = data["ranges"]["q_glob_10"]["values"]
        list.append(value)
    except KeyError:
        pass
    # add 10 minutes to the start time
    start_time += datetime.timedelta(minutes=10)

flat_list = sum(list, [])
print(int(flat_list[-1]))
