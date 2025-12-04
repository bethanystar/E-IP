import json
import sys

# Simple rule set for demonstration
RULES = {
    "autonomy_preservation": lambda x: "pass",
    "justification_integrity": lambda x: "pass",
    "coherence_check": lambda x: "pass"
}

def run_checks(system_id):
    return {
        "system": system_id,
        "results": {rule: fn(system_id) for rule, fn in RULES.items()},
        "overall_status": "aligned"
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python governance-check.py <system_id>")
        sys.exit(1)
    output = run_checks(sys.argv[1])
    print(json.dumps(output, indent=2))
