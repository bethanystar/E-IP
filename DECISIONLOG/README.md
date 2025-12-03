# DECISIONLOG

The **Decision Log** directory maintains an immutable, chronological record of
key architectural, governance, and ethical decisions made during the evolution
of the E-IP (Ethical Internet Protocol) and the Pharos Ethical Stack.

Decision logs provide:
- Transparency and traceability
- Rationale for protocol-level choices
- Accountability between contributors and governance bodies
- A durable audit trail that aligns with the E-IP Governance Protocol
- A reference for policymakers, implementers, and researchers

Each decision record must conform to the `decisionlog.schema.json` specification
found in the `/SPEC` folder.

## File Naming Convention

Use the following pattern:
YYYY-MM-Short-Name.json

Examples:
- `2025-01-Initial-Protocol-Decisions.json`
- `2025-02-LDT-Semantic-Layer-Expansion.json`
- `2025-03-Governance-Risk-Thresholds.json`

## When to Add a Decision Log

A decision log **must** be added when:
- A new protocol layer is created
- A schema is updated
- A governance rule changes
- A risk or ethical threshold is adjusted
- An alignment requirement is introduced
- A semantic rule (LDT-based) is formalized
- A policy-relevant feature is added or removed

## Required Fields

All decision logs must follow the schema:
- `id` – unique identifier
- `timestamp` – ISO-format timestamp
- `decision_summary` – short human-readable explanation
- `context` – relevant background
- `rationale` – why the decision was made
- `affected_components` – folder/file list or protocol layer
- `governance_impact` – implications for risk, trust, transparency
- `alignment_considerations` – LDT + E-IP alignment perspective
- `contributors` – individuals or orgs who participated
- `review_status` – draft / approved / superseded

See the example file for implementation details.


