# https://stackoverflow.com/questions/6921699/can-i-get-json-to-load-into-an-ordereddict
import json
from collections import OrderedDict
from pprint import pprint
from xml.etree.ElementTree import Element, tostring

def dict_to_xml(tag, d):

    elem = Element(tag)
    for key, val in d.items():
        child = Element(str(key))
        child.text = str(val)
        elem.append(child)

    return elem



http_status_codes_dict = json.load(open('http_statuscodes.json'), object_pairs_hook=OrderedDict)

pprint(http_status_codes_dict)

status_codes = {}
for code in http_status_codes_dict:
    status_codes[code['code']] = code


pprint(status_codes[500])

print("\n\ncreated xml:\n")
e = dict_to_xml('http_statuscodes', status_codes)
print(e)
print()
pprint(tostring(e, encoding='unicode'))

