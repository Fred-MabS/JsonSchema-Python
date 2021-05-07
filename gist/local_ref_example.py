# Example usage for add_local_schemas_to
import os
import json
from pathlib import Path
from urllib.parse import urljoin
import jsonschema


def add_local_schemas_to(resolver, schema_folder, base_uri, schema_ext='.schema.json'):
    ''' Add local schema instances to a resolver schema cache. 
    
    Arguments:
        resolver (jsonschema.RefResolver): the reference resolver
        schema_folder (str): the local folder of the schemas. 
        base_uri (str): the base URL that you actually use in your '$id' tags 
            in the schemas
        schema_ext (str): filter files with this extension in the schema_folder
    '''
    for dir, _, files in os.walk(schema_folder):
        for file in files:
            if file.endswith(schema_ext):
                schema_path = Path(dir) / Path(file)
                rel_path = schema_path.relative_to(schema_folder)
                with open(schema_path) as schema_file:
                    schema_doc = json.load(schema_file)
                key = urljoin(base_uri, str(rel_path))
                resolver.store[key] = schema_doc


instance_filename = 'data.json'
schema_folder = Path('schemas')
schema_filename = schema_folder / 'root.schema.json'
base_uri = 'https://www.example.com/schemas/'

with open(schema_filename) as schema_file:
    schema = json.load(schema_file)
    
with open(instance_filename) as instance_file:
    instance = json.load(instance_file)

resolver = jsonschema.RefResolver(base_uri=base_uri, referrer=schema)
add_local_schemas_to(resolver, schema_folder, base_uri)
jsonschema.validate(instance, schema, resolver=resolver)
