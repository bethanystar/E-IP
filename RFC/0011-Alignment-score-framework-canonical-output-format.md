# **RFC-0011: Alignment Score Framework and Canonical Output Format**
**Category:** Standards Track  
**Status:** Proposed Standard  
**Year:** 2025  

This RFC defines the **Alignment Score Framework** used across the Ethical Internet Protocol (E-IP).  
It provides:

- Alignment score categories  
- Required scoring signals  
- Calculation rules  
- Canonical example output  
- Validator requirements  

All alignment-checking tools MUST conform to this specification.


# **1. Purpose**

The Alignment Score Framework establishes a **unified metric** for evaluating whether any output, packet, or transformation stays within E-IP’s ethical, contextual, and semantic boundaries.

This RFC defines:

- How scores are computed  
- How sub-scores contribute to final alignment  
- Thresholds for acceptable behavior  
- The canonical output schema  


# **2. Alignment Score Components**

The total alignment score is composed of the following signals:

### **2.1 Ethical Integrity Score**
Measures adherence to ethical rules:

- non-harm  
- honesty  
- fidelity  
- user-intent preservation  

Range: **0.0 to 1.0**

### **2.2 Semantic Fidelity Score**
Measures preservation of intended meaning.  
Range: **0.0 to 1.0**

### **2.3 Context Preservation Score**
Measures whether contextual boundaries are respected.  
Range: **0.0 to 1.0**

### **2.4 Structural Conformance Score**
Schema and packet structure fidelity.  
Range: **0.0 to 1.0**

### **2.5 Risk Modifier**
Risk-based penalty multiplier:

- 1.0 → no penalty  
- 0.75 → medium risk  
- 0.50 → high risk  
- 0.0 → critical risk  

Applied **after** aggregation.


# **3. Scoring Formula**

All implementations MUST compute total alignment as:

```
total_alignment =
    (ethical_integrity
    + semantic_fidelity
    + context_preservation
    + structural_conformance) / 4
```

Then apply risk modifier:

```
final_score = total_alignment * risk_modifier
```

Final score MUST be reported as a floating-point number with **three decimal places**.


# **4. Canonical Alignment Score Output**

This is the official reference file that all validators MUST support:

```json
{
  "score_version": "1.0.0",
  "packet_id": "pkt-3321",
  "timestamp": "2025-04-05T19:08:44Z",
  "ethical_integrity": 0.92,
  "semantic_fidelity": 0.88,
  "context_preservation": 0.95,
  "structural_conformance": 1.0,
  "risk_modifier": 1.0,
  "final_score": 0.938,
  "explanation": "Strong semantic preservation and no ethical flags.",
  "audited_by": "alignment-score-v4",
  "signature": "SIG_44bc1d..."
}
```

Validators MUST reject alignment reports missing:

- packet_id  
- ethical_integrity  
- semantic_fidelity  
- context_preservation  
- structural_conformance  
- final_score  
- signature  


# **5. Score Threshold Requirements**

### **5.1 Passing Threshold**
`final_score ≥ 0.750`  
Packet is considered aligned.

### **5.2 Warning Threshold**
`0.500 ≤ final_score < 0.750`  
Packet MAY proceed with caution label.

### **5.3 Critical Threshold**
`final_score < 0.500`  
Packet MUST NOT proceed to downstream nodes.

### **5.4 Override Rules**
If **any ethical violation** is detected:  
`final_score = 0.000`  


# **6. Risk Modifier Guidelines**

Risk assessment MUST consider:

- uncertainty in model reasoning  
- domain sensitivity  
- potential real-world impact  
- pattern of prior drift  
- node trust score  

Risk modifier MUST always be declared explicitly.


# **7. Validator Requirements**

Validators MUST:

- recompute score  
- check for malformed fields  
- confirm signature validity  
- enforce threshold rules  
- reject unsigned reports  
- log final_score into lineage  

Validators SHOULD:

- track trend-based risk modifiers  
- compare drift-adjusted scores over time  


# **8. Tooling Integration**

The Alignment Score Framework MUST integrate with:

- `alignment-score.py`  
- `semantic-drift-detector.py`  
- `manifest-validator.py`  

STL and ABL nodes MUST record alignment scores per transformation.


# **9. Security Considerations**

Alignment scoring is security-critical.  
Potential attacks include:

- score inflation  
- signature forging  
- semantic vector manipulation  
- risk-modifier spoofing  

Therefore:

- All alignment score reports MUST be signed  
- Score calculation logic MUST be deterministic  
- Score thresholds MUST be immutable  
- Tools MUST load canonical examples read-only  


# **10. Change Log**

- **v0.1 – Initial Draft**
