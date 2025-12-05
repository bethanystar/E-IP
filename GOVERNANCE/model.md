# E-IP Governance Model

The E-IP Governance Model establishes how the protocol evolves and how decisions are made by maintainers, contributors, and reviewers.

## Principles
1. **Transparency** — All changes must be publicly visible and documented.
2. **Alignment First** — Any change must pass an Ethical Alignment Review (EAR) using the E-IP Alignment Protocol.
3. **Multi-Layer Review** — Technical, ethical, and semantic layers must all approve before merge.
4. **No Single Gatekeeper** — Authority is distributed across maintainers.
5. **Open Participation** — Anyone may propose changes, file issues, or suggest improvements.

## Roles
### **Contributors**
- Submit issues, proposals, and PRs.
- Provide peer review.

### **Maintainers**
- Approve or reject proposed changes.
- Ensure protocol coherence across layers.

### **Alignment Reviewers**
- Specialists who use the E-IP Alignment Protocol to evaluate ethical, societal, and potential downstream risks.

### **Semantic Stewards**
- Ensure all language, definitions, and symbolic conventions align with the E-IP Semantic Layer.

### **Governance Chair (optional rotation)**
- Coordinates releases.
- Ensures cross-layer review is complete.
- No special approval authority.

## Decision Types
### **1. Editorial**
Small fixes, typos, formatting.  
→ Single maintainer approval.

### **2. Minor Technical or Clarification**
No protocol-breaking impact.  
→ Two maintainers + semantic review.

### **3. Major Protocol Changes**
Affects schemas, required fields, or protocol logic.  
→ Full review: maintainers + alignment reviewers + semantic stewards.

### **4. Ethical Impacting Changes**
Any change that affects user rights, safety boundaries, data use, agent decision-making, or downstream risks.  
→ Mandatory Ethical Alignment Review (EAR)  
→ Requires unanimous alignment reviewer approval.

## Decision Documentation
All decisions must include:
- Decision summary  
- Rationale  
- Type (editorial, minor, major, ethical)  
- Cross-layer validation  

Documented in `/DECISIONLOG/` using schema-compliant JSON.
