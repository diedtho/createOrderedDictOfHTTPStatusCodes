# https://stackoverflow.com/questions/6921699/can-i-get-json-to-load-into-an-ordereddict
import json
from collections import OrderedDict
from pprint import pprint

http_status_codes_dict = json.load(open('http_statuscodes.json'), object_pairs_hook=OrderedDict)

pprint(http_status_codes_dict)

status_codes = {}
for code in http_status_codes_dict:
    status_codes[code['code']] = code


pprint(status_codes[500])