import json
import jsonschema
import sys

SCHEMA_PATH = "../SPEC/decisionlog.schema.json"

def load_schema():
    with open(SCHEMA_PATH, "r") as f:
        return json.load(f)

def load_log(path):
    with open(path, "r") as f:
        return json.load(f)

def validate(log, schema):
    jsonschema.validate(instance=log, schema=schema)
    print("✔ Decision Log is valid.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate-decisionlog.py <decisionlog.json>")
        sys.exit(1)
    schema = load_schema()
    log = load_log(sys.argv[1])
    validate(log, schema)
