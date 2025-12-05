# **RFC-0010: Semantic Drift Detection and Reporting**
**Category:** Informational  
**Status:** Proposed Standard  
**Year:** 2025  

This RFC defines the canonical structure for **semantic drift reporting**, including:  
- Example Drift Reports  
- Drift Categories  
- Detection Rules  
- Validator Requirements  

Semantic drift refers to unintended meaning-shift as packets traverse the E-IP stack.  
This RFC provides the reference patterns all detection tools MUST follow.


# **1. Purpose**

The purpose of this document is to:

- Define semantic drift classifications  
- Provide canonical example drift reports  
- Standardize required detection signals  
- Establish minimum validator requirements  
- Support alignment tool calibration  

This RFC is normative for all drift-detection components of STL and ABL.


# **2. Drift Categories**

All semantic drift MUST fall into one of the following categories:

### **2.1 Lexical Drift**
Meaning alters due to word or token substitution.

### **2.2 Intent Drift**
The user’s intended action changes.

### **2.3 Contextual Drift**
Conversation or environment context is degraded or replaced.

### **2.4 Ethical Drift**
Output shifts toward violating E-IP ethical constraints.

### **2.5 Structural Drift**
Packet structure remains valid, but semantic vectors deviate beyond tolerance.


# **3. Example Semantic Drift Report**

Below is the canonical example used for validators and testing suites:

```json
{
  "report_version": "1.0.0",
  "drift_id": "drift-2025-022",
  "timestamp": "2025-03-18T04:22:10Z",
  "packet_id": "pkt-1129",
  "origin_node": "node-phi-02",
  "detected_by": "stl-drift-detector-v3",
  "drift_category": "intent",
  "original_intent_vector": [0.921, 0.228, 0.004, 0.772],
  "resulting_intent_vector": [0.551, 0.992, 0.114, 0.093],
  "vector_delta": 0.4419,
  "threshold": 0.3000,
  "explanation": "Intent shifted from 'information request' to 'recommendation generation'.",
  "severity": "high",
  "signature": "SIG_9af3d9..."
}
```

Validators MUST reject drift reports missing:

- **drift_id**  
- **timestamp**  
- **packet_id**  
- **drift_category**  
- **severity**  
- **signature**  


# **4. Drift Scenario Examples**

### **4.1 Lexical Drift Scenario**
User: “What is the safest route?”  
Model output: “What is the fastest route?”  
Drift: **safety → speed** (misaligned value shift)

### **4.2 Intent Drift Scenario**
User intent: *summarize*  
Output intent: *generate opinion*  
Drift: transformation class changed

### **4.3 Ethical Drift Scenario**
Output begins introducing:  
- fabricated citations  
- exaggerated claims  
- manipulated framing  

Triggers **ETHICAL-INTEGRITY-FAIL**.

### **4.4 Structural Drift Scenario**
Packet structure unchanged, but semantic vector deviates by ≥ threshold.


# **5. Detection Rules**

Drift MUST be flagged when any of the following occurs:

### **5.1 Vector Drift**
`distance(original, result) > defined-intent-threshold`

### **5.2 Policy Drift**
Field-level mismatch in policy-aligned output.

### **5.3 Canonical Intent Switch**
Output matches a different canonical intent more strongly than the original.

### **5.4 Ethical Rule Violation**
Triggered via ethical rule engine:

- non-harm  
- fidelity  
- context-preservation  

### **5.5 Multi-Hop Accumulation**
Accumulated drift across hops exceeds composite tolerance.


# **6. Drift Severity Levels**

E-IP drift reports MUST classify severity as:

- **low** – minor lexical drift, no policy effect  
- **medium** – context or structure shift  
- **high** – intent change, ethical implications  
- **critical** – meaning reversal, harmful output risk  


# **7. Validator Requirements**

Validators MUST:

- Compute drift distance  
- Compare against category thresholds  
- Produce complete drift reports  
- Reject malformed reports  
- Reject unsigned reports  
- Reject reports with missing severity fields  

Validators SHOULD:

- Log historical trends  
- Estimate drift probability over time  


# **8. Detection Thresholds**

Default thresholds (implementations MAY override):

- **Lexical:** 0.15  
- **Context:** 0.25  
- **Intent:** 0.30  
- **Ethical:** 0.00 tolerance  
- **Structural:** based on canonical vector deviation  


# **9. Tooling Integration**

Drift detection tools MUST integrate with:

- `semantic-drift-detector.py`  
- `manifest-validator.py`  
- `alignment-score.py`  

STL nodes MUST expose drift telemetry to ABL.


# **10. Security Considerations**

Semantic drift reports are sensitive.  
They can reveal:

- Model weaknesses  
- Node transformation patterns  
- System alignment limits  

Therefore:

- Drift reports MUST be immutable  
- Drift reports MUST be cryptographically signed  
- Storage MUST be append-only  
- Drift tooling MUST load examples in read-only mode  


# **11. Change Log**

- **v0.1 – Initial Draft**
