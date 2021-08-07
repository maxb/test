#!/usr/bin/python3

import json
import yaml

with open('example.yaml') as f:
    data = yaml.safe_load(f)

with open('example.json', 'w') as f:
    json.dump(data, f)
    f.write('\n')
