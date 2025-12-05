# Change Control Process

This document describes how changes are proposed, reviewed, approved, and recorded.

## 1. Proposing a Change
Anyone may propose:
- Issue labeled "spec change"
- Pull Request (PR)
- Request for Comment (RFC) submitted to `/SPEC/rfcs/` (optional)

## 2. Required Sections for Any Change Proposal
Each PR must include:
- Summary of change  
- Protocol layer(s) impacted  
- Motivation & rationale  
- Backwards compatibility  
- Ethical considerations  
- Semantic implications  
- Link to Decision Log entry

## 3. Review Workflow
1. **Initial Maintainer Review**
   - Evaluates completeness & clarity.
2. **Cross-Layer Review**
   - Technical
   - Semantic
   - Alignment (if required)
3. **Final Maintainer Approval**
   - Two maintainers minimum.
4. **Merge to Main**
   - Only after Decision Log entry is validated.

## 4. Versioning
E-IP follows **Semantic Versioning + Layer Notation**:

`v1.2.0-ALPHA`  
`v1.4.1-SEMLAY`  
`v2.0.0-GOVERNANCE`

## 5. Release Cadence
- Minor releases: monthly (as needed)
- Major releases: quarterly  
- Emergency ethical patches: immediate
