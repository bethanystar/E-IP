# RFC: Ethical Interoperability Protocol (E-IP)
## Minimum Viable Protocol Draft

### 1. Purpose
Define the smallest possible standard enabling ethically aligned communication across intelligent agents.

---

## 2. MVP Components

### 2.1 Module 1 — Ethical Intent Packet Schema
Defines the mandatory and optional fields agents must transmit.

Minimal fields:
- agent_id
- action_type
- intended_outcome
- affected_entities
- ethical_standard
- confidence
- ambiguity_flag

Optional metadata:
- cultural_context
- anthropic_constraints
- HITL (human-in-the-loop)

---

### 2.2 Module 2 — Verification Layer
Performs four checks:

1. **Integrity** – compares intent vs. predicted outcome  
2. **Safety** – checks against minimal hazard ontology  
3. **Identity** – verifies signature  
4. **Transparency** – creates immutable log hash  

---

### 2.3 Module 3 — Consensus Layer
A lightweight quorum:

- 3 agents independently evaluate packet  
- quorum required to proceed  
- dissent → escalate  
- final decision hashed for audit  

---

### 3. Interop Requirements

Any system implementing E-IP must:
- support the ethical packet schema
- implement the four verification primitives
- support quorum logic
- maintain a hashed record of finalized decisions

---

### 4. Non-Requirements (Important)

E-IP does **not**:
- define moral frameworks  
- enforce specific values  
- require blockchain  
- require heavy compute  
- require centralized authority  

---

### 5. Status
This document defines the MVP required for v0.1.
