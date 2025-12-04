import json
import sys

TEMPLATE = {
  "id": "",
  "version": "0.1",
  "system_type": "",
  "description": "",
  "capabilities": [],
  "constraints": [],
  "dependencies": { "software": [] },
  "telemetry_requirements": { "expected_inputs": [], "emitted_outputs": [] },
  "governance_hooks": { "rule_checks": [] },
  "ldt_semantic_profile": { "core_dimensions": [] },
  "maintainers": [{"name": "", "contact": ""}],
  "verification": {"schema_version": "1.0", "signature": ""}
}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate-manifest-template.py <output_file.json>")
        sys.exit(1)
    with open(sys.argv[1], "w") as f:
        json.dump(TEMPLATE, f, indent=2)
    print("✔ Manifest template generated:", sys.argv[1])
