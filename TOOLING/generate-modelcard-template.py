import json
import sys

TEMPLATE = {
  "model_name": "",
  "version": "0.1",
  "overview": "",
  "intended_use": "",
  "limitations": [],
  "ethical_considerations": {},
  "alignment_properties": {},
  "risk_profile": {},
  "input_output_specs": {},
  "data_sources": [],
  "evaluation_metrics": {},
  "governance_contacts": {}
}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate-modelcard-template.py <output.json>")
        sys.exit(1)
    with open(sys.argv[1], "w") as f:
        json.dump(TEMPLATE, f, indent=2)
    print("✔ Model Card template created:", sys.argv[1])
