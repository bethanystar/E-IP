import json
import jsonschema
import sys

SCHEMA_PATH = "../SPEC/manifest.schema.json"

def load_schema():
    with open(SCHEMA_PATH, "r") as f:
        return json.load(f)

def load_manifest(path):
    with open(path, "r") as f:
        return json.load(f)

def validate(manifest, schema):
    jsonschema.validate(instance=manifest, schema=schema)
    print("✔ Manifest is valid according to schema.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate-manifest.py <manifest.json>")
        sys.exit(1)
    schema = load_schema()
    manifest = load_manifest(sys.argv[1])
    validate(manifest, schema)
