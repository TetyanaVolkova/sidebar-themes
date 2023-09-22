
def get_schema(schema):    
    import os
    import json

    root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    with open(root + "/schemas/" + schema) as schema_file:
        return json.loads(schema_file.read())