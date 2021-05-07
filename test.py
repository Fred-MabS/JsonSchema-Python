from jsonschema import validate
from jsonschema.exceptions import ValidationError
import json
import urllib

def check(data_fn, schema_url):
    print(f'Checking {data_fn} against {schema_url}')
    with open(data_fn) as data_file, urllib.request.urlopen(schema_url) as schema_file:
    # with open('main.json') as schema_file, open('json/address1.json') as json_file:
        schema = json.load(schema_file)
        data = json.load(data_file)
        # print(json.dumps(schema))
        try:
            validate(instance=data, schema=schema)
            print('Valid')
        except ValidationError as e:
            print(f'message: {e.message}')
            print(f'validator: {e.validator}')
            print(f'validator_value: {e.validator_value}')
            print(f'relative_schema_path: {e.relative_schema_path}')
            print(f'absolute_schema_path: {e.absolute_schema_path}')
            print(f'relative_path: {e.relative_path}')
            print(f'absolute_path: {e.absolute_path}')
            print(f'instance: {e.instance}')
            print(f'context: {e.context}')
            print(f'cause: {e.cause}')
            print(f'parent: {e.parent}')

check('json/addresses-OK.json', 'https://fred-mabs.github.io/addresses.json')
check('json/addresses-KO.json', 'https://fred-mabs.github.io/addresses.json')

