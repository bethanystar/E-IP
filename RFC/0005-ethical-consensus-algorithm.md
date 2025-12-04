# RFC-0005: Ethical Consensus Algorithm (ECA)
Category: Standards Track  
Status: Proposed Standard  
Year: 2025

## 1. Overview
The Ethical Consensus Algorithm (ECA) is the mechanism E-IP uses to compute, validate, and enforce ethical constraints across all packets, agents, and participating nodes.  
It ensures that *ethical alignment* is stable, reproducible, and context-aware, and that no packet can bypass its required ethical checks.

The ECA does **three** things:

1. Computes the **ethical_state** of a packet based on ontology rules  
2. Applies **ethical_flags** that must be preserved end-to-end  
3. Produces a deterministic **consensus decision** that upstream and downstream nodes can verify  

ECA is executed inside the **Alignment Boundary Layer (ABL)**, but its decisions propagate through the entire protocol stack.

---

## 2. Ethical Inputs
The ECA consumes the following required inputs:

- **intent**  
- **context_scope**  
- **semantic_checksum**  
- **ethical_flags**  
- **lineage**  
- **risk_score**  
- **governance_ruleset_version**  
- **ethical_ontology_version**

Optional extended inputs:

- **actor identity class** (anonymous, pseudonymized, attributed)  
- **jurisdiction context**  
- **conflict-of-interest markers**

All inputs are immutable once the packet enters ABL validation.

---

## 3. Ethical Flag Categories
E-IP defines a canonical taxonomy of ethical flags:

### 3.1 Mandatory Flags
These must be evaluated for every packet:

- `harm_risk`  
- `coercion`  
- `privacy_violation`  
- `misinformation`  
- `systemic_bias`  
- `accountability_required`  

### 3.2 Contextual Flags
Evaluated only when relevant:

- `sensitive_domain`  
- `youth_protection`  
- `geopolitical_implications`  
- `collective_safety`  

### 3.3 Enforcement Flags
Flags that change how the STL handles delivery:

- `requires_human_review`  
- `high_risk_route`  
- `quarantine`  

---

## 4. Ethical Consensus Function
The core of the ECA is the **ethical_consensus()** function.
ethical_consensus(packet) → {
ethical_state: "...",
decision: "allow" | "restrict" | "quarantine" | "deny",
risk_score: float,
flags: [...],
reasoning: "..."
}

### 4.1 Ethical State Levels
Ethical states are discrete:

- **"aligned"**  
- **"conditionally_aligned"**  
- **"misaligned"**  
- **"ethically_blocked"**  

### 4.2 Decision Matrix (Normative)
if harm_risk > threshold_high → deny
if coercion detected → deny
if privacy_violation and no consent → restrict
if systemic_bias unresolved → restrict
if misinformation high-confidence → quarantine
else → allow

The threshold values must be provided by the governance ruleset.

---

## 5. Consensus Determinism Requirements
To be valid, an ECA implementation MUST satisfy:

### MUST
- Produce identical outputs for identical inputs  
- Be fully deterministic  
- Preserve all ethical_flags  
- Include machine-readable reasoning  
- Log every consensus decision  

### SHOULD
- Support pluggable rule engines  
- Provide human-readable explanations  
- Support jurisdiction-specific modifiers  

### MAY
- Offer caching for repeated identical packets  
- Provide accelerated hardware-backed validation  

---

## 6. Governance Interactions
The Ethical Consensus Algorithm is tightly coupled to the governance layer.

Governance may:

- Update thresholds  
- Add or remove ethical rules  
- Require multi-party review  
- Override decisions with justification  
- Add new ethical flag categories  

All governance modifications must increment:

- `governance_ruleset_version`  
- `ethical_ontology_version`  

---

## 7. Failure & Rejection Codes
The ECA defines standardized error modes:

| Code | Meaning |
|------|---------|
| **ECA-001** | Missing required ethical flags |
| **ECA-002** | Invalid or outdated ontology version |
| **ECA-003** | Conflict between rulesets |
| **ECA-004** | High-risk harm threshold exceeded |
| **ECA-005** | Coercion detected |
| **ECA-006** | Privacy violation without consent |
| **ECA-007** | Insufficient context for evaluation |
| **ECA-008** | Unresolvable contradiction in lineage |
| **ECA-009** | Governance override required |

Error codes MUST be returned in machine-readable format.

---

## 8. Output Schema
Every ECA run must output the following object:

```json
{
  "ethical_state": "aligned",
  "decision": "allow",
  "risk_score": 0.14,
  "ethical_flags": ["privacy_violation", "systemic_bias"],
  "reasoning": "...",
  "ruleset_version": "2025.1",
  "ontology_version": "2025.3",
  "timestamp": "2025-01-01T12:00:00Z"
}
## **9. Safety Limits**

The Ethical Consensus Algorithm (ECA) must enforce non-bypassable safety limits that prevent unethical, misaligned, or semantically-corrupted outputs from propagating through the E-IP stack.

### **9.1 Hard Safety Limits**
Hard limits are absolute. Any violation results in immediate packet rejection.

- **HL-01:** No content may violate human rights or cause material harm.  
- **HL-02:** No content may bypass alignment_envelope requirements.  
- **HL-03:** All packets must include a valid semantic_checksum.  
- **HL-04:** No packet may contain unresolved high-risk ethical_flags.  
- **HL-05:** No packet may degrade below minimum alignment confidence (`min_alignment = 0.75`).

If any hard limit triggers:
{
"status": "rejected",
"reason": "HARD_LIMIT_VIOLATION",
"violations": ["HL-XX"]
}

### **9.2 Soft Safety Limits**
Soft limits trigger warnings, not automatic rejection.

- **SL-01:** Missing lineage references.
- **SL-02:** Low context depth.
- **SL-03:** Ambiguous intent expression.
- **SL-04:** Semantic drift below threshold.

Soft-limit output:
{
"status": "accepted_with_warnings",
"warnings": ["SL-XX"]
}

---

## **10. Failure Modes**

The ECA must identify and classify failure modes so downstream systems can observe, monitor, and remediate alignment risk.

### **10.1 Failure Classes**

#### **F1 — Semantic Failure**
Occurs when meaning cannot be validated, checksum mismatch, or drift exceeds threshold.
{
"failure_class": "F1_SEMANTIC",
"details": "semantic_checksum mismatch"
}

#### **F2 — Ethical Failure**
Ethical flags indicate high-risk or unresolvable ethics violations.
{
"failure_class": "F2_ETHICAL",
"details": ["HARM_RISK", "COERCION_PATTERN"]
}

#### **F3 — Structural Failure**
Packet does not conform to schema or required fields.
{
"failure_class": "F3_STRUCTURAL",
"details": "Missing required field: alignment_envelope.intent"
}

#### **F4 — Consensus Failure**
Consensus round cannot reach required quorum or confidence threshold.
{
"failure_class": "F4_CONSENSUS",
"details": "alignment_confidence < required_min"
}

### **10.2 Failure Mode Triggers**

- **Checksum mismatch → F1**  
- **Ethical rules violation → F2**  
- **Schema invalid → F3**  
- **Consensus loop stalls → F4**  
- **Context bleed detected → F1 + F2**  
- **Adversarial intent detected → F2 + automatic shutdown**

---

## **11. Appendix: Reference Objects**

### **11.1 Reference: alignment_envelope**
{
"intent": "string",
"context_scope": "string",
"semantic_checksum": "string",
"ethical_flags": [],
"lineage": {
"parent_ids": []
},
"risk_score": 0.0
}

### **11.2 Reference: consensus_result**
{
"alignment_confidence": 0.0,
"evaluation_summary": {},
"risk_score": 0.0,
"consensus_notes": []
}

### **11.3 Reference: failure_result**
{
"status": "failed",
"failure_class": "F1_SEMANTIC | F2_ETHICAL | F3_STRUCTURAL | F4_CONSENSUS",
"details": "string"
}

### **11.4 Reference: validated_packet**
{
"status": "validated",
"risk_score": 0.0,
"alignment_confidence": 0.0,
"consensus_result": { ... },
"packet": {
"header": { ... },
"body": { ... }
}
}










