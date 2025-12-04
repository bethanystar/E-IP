# RFCs (Requests for Comment)

This folder contains formal proposals for significant changes, extensions, or additions to the E-IP protocol. RFCs are used when a proposed change:

- Introduces new protocol functionality  
- Modifies the behavior of existing layers (Governance, Alignment, Semantic)  
- Requires substantial cross-layer review  
- Impacts safety, risk, or implementation patterns  
- Has ecosystem-wide implications  

RFCs ensure that major changes are publicly discussed, reviewed, and documented before integration into the specification.

## RFC Format
All RFCs must follow the template defined in:
- `RFC-TEMPLATE.md`

Before submitting an RFC:
1. Open an issue labeled **RFC Intent**  
2. Draft the RFC using the template  
3. Submit a Pull Request referencing the issue  

## RFC Lifecycle
1. **DRAFT** — Submitted for public comment  
2. **UNDER REVIEW** — Maintainers + Alignment + Semantic Stewards review  
3. **ACCEPTED** — Approved and scheduled for inclusion  
4. **REJECTED** — Closed with rationale  
5. **WITHDRAWN** — Author retracts  
6. **INTEGRATED** — Became part of the SPEC folder  

## File Naming
RFCs follow the convention:

rfc-YYYY-NNN-title.md

Where:
- `YYYY` = year created  
- `NNN` = sequential ID  
- `title` = short, hyphenated summary  

Example:  
`rfc-2025-001-alignment-boundary-layer.md`

