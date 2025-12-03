# MODELCARDS

The **Model Cards** directory contains standardized documentation artifacts
describing the behavior, purpose, risks, constraints, and semantic properties of
systems, agents, or models operating within (or adjacent to) the E-IP
architecture.

This folder provides:
- Transparent disclosures for developers, auditors, and policymakers
- A reference for alignment, safety, and governance analysis
- A uniform format based on `modelcard.schema.json`
- Semantic grounding for LDT-based interpretability
- Artifacts required for adoption of the Pharos Ethical Stack

Model cards ensure that systems built on top of E-IP can be evaluated across
key dimensions, including purpose, data provenance, ethical considerations,
risk profiles, and decision boundaries.

## File Naming Convention

modelname-version-modelcard.json

Examples:
- `alignment-agent-v0.1-modelcard.json`
- `risk-scoring-module-v0.2-modelcard.json`
- `semantic-router-v1.0-modelcard.json`

## When to Add a Model Card

A model card must be created when:
- A new model, agent, or system interacts with E-IP
- A system receives a major update
- A model transitions between environments (dev → prod)
- Policy, risk, or ethical constraints change
- A new semantic capability is introduced

## Required Fields (from schema)

All model cards must follow the schema and include:
- `model_name`
- `version`
- `overview`
- `intended_use`
- `limitations`
- `ethical_considerations`
- `alignment_properties`
- `risk_profile`
- `input_output_specs`
- `data_sources`
- `evaluation_metrics`
- `governance_contacts`

See the example model card for implementation details.

