import json
import jsonschema
import sys

SCHEMA_PATH = "../SPEC/modelcard.schema.json"

def load_schema():
    with open(SCHEMA_PATH, "r") as f:
        return json.load(f)

def load_card(path):
    with open(path, "r") as f:
        return json.load(f)

def validate(card, schema):
    jsonschema.validate(instance=card, schema=schema)
    print("✔ Model Card is valid.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate-modelcard.py <modelcard.json>")
        sys.exit(1)
    schema = load_schema()
    card = load_card(sys.argv[1])
    validate(card, schema)
