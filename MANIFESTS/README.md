# MANIFESTS

The **Manifests** directory contains machine-readable declarations describing the
identity, capabilities, constraints, and governance-relevant properties of
systems that participate in (or interact with) the E-IP architecture.

Manifests serve as:
- A self-attestation layer for agents, services, and subsystems
- A dependency transparency mechanism (informed by SBOM principles)
- A foundation for governance checks and semantic reasoning
- A standardized interface for compliance, auditing, and alignment
- A bridge between model documentation, telemetry, and protocol events

This directory uses the `manifest.schema.json` located in `/SPEC`.

## File Naming Convention

systemname-version-manifest.json

Examples:
- `alignment-agent-v0.1-manifest.json`
- `semantic-router-v1.0-manifest.json`
- `risk-monitor-v0.3-manifest.json`

## When to Add a Manifest

A manifest must be created when:
- A new agent or subsystem is introduced
- A service begins participating in E-IP telemetry flows
- A system updates capabilities or constraints
- Risk or alignment thresholds change
- A system moves between environments (dev → prod)

## Required Fields (from schema)

All manifests must follow the schema and include:
- `id`
- `version`
- `system_type`
- `description`
- `capabilities`
- `constraints`
- `dependencies`
- `telemetry_requirements`
- `governance_hooks`
- `ldt_semantic_profile`
- `maintainers`
- `verification`

See the example manifest for implementation details.
