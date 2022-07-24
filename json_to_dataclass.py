# https://stackoverflow.com/questions/6921699/can-i-get-json-to-load-into-an-ordereddict
import json
from collections import OrderedDict
from pprint import pprint

from dacite import from_dict

from status_codes_dataclasses import Status_Code

http_status_codes_dict = json.load(open('http_statuscodes.json'), object_pairs_hook=OrderedDict)

pprint(http_status_codes_dict)

status_codes = {}
for code in http_status_codes_dict:
    data = code
    result = from_dict(data_class=Status_Code, data=data)
    print(result)
    print('=' * 111)


