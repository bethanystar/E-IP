# TOOLING

This directory contains command-line tools, validators, generators, and helper
scripts that support the implementation and adoption of the E-IP protocol stack.

While E-IP provides schemas, specifications, and conceptual architecture, the
TOOLING folder provides *practical utilities* that make the protocol usable in
real developer, governance, and policy environments.

## Tool Categories

### 1. Validation Tools
Scripts that check conformance to:
- `manifest.schema.json`
- `modelcard.schema.json`
- `decisionlog.schema.json`
- Protocol event formatting
- Semantic-layer output structure

### 2. Generators
Templates and automation for:
- Creating new manifests
- Generating baseline model cards
- Creating decision logs
- Initializing new E-IP compliant services

### 3. Semantic Utilities
Basic tools for:
- Running symbolic distinction checks
- Computing semantic coherence scores
- Formatting LDT-aligned semantic traces

### 4. Governance Tools
CLI helpers for:
- Creating governance proposals
- Submitting updates to the decision log
- Checking compliance with alignment rules
- Running governance-cycle simulations

## Philosophy
This folder contains minimal, example-level tooling designed to help developers
bootstrap adoption. Production tools can be built on top of these examples.

All tools should aim to be:
- Lightweight
- Transparent
- Dependency-minimal
- Easy to extend
- Compatible with any language or environment

## Contents
- `validate-manifest.py`
- `validate-modelcard.py`
- `validate-decisionlog.py`
- `generate-manifest-template.py`
- `generate-modelcard-template.py`
- `semantic-evaluator.py`
- `governance-check.py`

