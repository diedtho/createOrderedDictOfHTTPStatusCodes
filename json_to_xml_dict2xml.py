# https://stackoverflow.com/questions/6921699/can-i-get-json-to-load-into-an-ordereddict
import json
from collections import OrderedDict
from pprint import pprint
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString


http_status_codes_dict = json.load(open('http_statuscodes.json'), object_pairs_hook=OrderedDict)

pprint(http_status_codes_dict)

status_codes = {}
for code in http_status_codes_dict:
    status_codes[str(code['code'])] = code


xml = dicttoxml(http_status_codes_dict)
dom = parseString(xml)
print(dom.toprettyxml())

print("\n\nJust the simple dict:\n")
xml = dicttoxml(status_codes)
dom = parseString(xml)
print(dom.toprettyxml())