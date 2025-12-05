# **RFC-0009: Required Example Files for E-IP Implementations**
**Category:** Informational  
**Status:** Proposed Standard  
**Year:** 2025  

This RFC provides canonical **example files** that all E-IP implementers MUST reference.  
These examples ensure cross-implementation consistency and serve as templates for validators, engines, and nodes.


# **1. Purpose**

This document defines the required example files for the E-IP ecosystem:

- Decision Logs (DLOG)  
- Semantic Definition Files (SDF)  
- RFC Submission Template  
- Compliance Issue Report  

All examples in this RFC are normative.  
Any system-generated examples MUST conform exactly to these formats.


# **2. Required Example File Types**

E-IP implementations MUST include the following minimal examples:

- **One Decision Log example**  
- **One Semantic Definition File (SDF) example**  
- **One RFC submission example**  
- **One compliance issue example**

These examples are used for:

- Parser conformance tests  
- Schema validation  
- Tooling calibration  
- Regression testing  


# **3. Example Decision Log (DLOG)**

Decision Logs track alignment-critical decisions performed by ABL/STL.

Below is the canonical example:

```json
{
  "dlog_version": "1.0.0",
  "decision_id": "dlog-2025-001",
  "timestamp": "2025-01-18T16:42:55Z",
  "actor": "abl-engine-v2",
  "input_packet_id": "pkt-9823",
  "alignment_status": "valid",
  "risk_score": 0.14,
  "justification": "Intent confirmed, checksum verified, no ethical flags triggered.",
  "lineage_append": {
    "parent_ids": ["pkt-8101"],
    "mutation_type": "semantic_verification"
  },
  "signature": "SIG_e3af..."
}
```

Validators MUST reject any DLOG missing:

- **decision_id**  
- **timestamp**  
- **actor**  
- **alignment_status**  
- **signature**  


# **4. Example Semantic Definition File (SDF)**

SDFs define canonical intent structures and semantic boundaries.

```json
{
  "sdf_version": "1.1.0",
  "canonical_intents": [
    {
      "intent_id": "intent.ask.general",
      "description": "User asks for general information.",
      "allowed_transformations": ["summarization", "translation"],
      "ethical_rules": ["non-harm", "accuracy"]
    }
  ],
  "semantic_vectors": {
    "intent.ask.general": [0.129, 0.442, 0.981, 0.331]
  },
  "checksum": "sha256:91bd9f..."
}
```

SDFs MUST:

- Contain **at least one canonical intent**  
- Provide semantic vectors **or** intent mapping  
- Include a **checksum**  


# **5. Example RFC Submission Template**

Implementers MUST use this structure when submitting new RFCs:

```md
# RFC-XXXX: <Title>
**Category:** <Standards Track / Informational / Experimental>  
**Status:** <Draft / Proposed Standard / Final>  
**Year:** 2025  

# 1. Overview
<summary>

# 2. Motivation
<what problem this RFC solves>

# 3. Specification
<technical details, diagrams, schemas>

# 4. Security Considerations
<required>

# 5. Backwards Compatibility
<required>

# 6. Change Log
- v0.1 – Initial draft
```

Any RFC missing **Security Considerations** MUST be rejected.


# **6. Example Compliance Issue Report**

Used when a node, model, or agent violates E-IP policy.

```json
{
  "report_version": "1.0.0",
  "incident_id": "comp-2025-014",
  "timestamp": "2025-03-02T11:14:00Z",
  "entity_id": "node-alpha-03",
  "violation_type": "MANIFEST-UNDECLARED-CAPABILITY",
  "description": "Node attempted transformation not listed in manifest capabilities.",
  "severity": "high",
  "affected_packets": ["pkt-332", "pkt-334"],
  "recommended_action": "temporary suspension",
  "signature": "SIG_29ffee..."
}
```

Compliance validators MUST reject reports missing:

- **incident_id**  
- **entity_id**  
- **violation_type**  
- **severity**  
- **signature**  


# **7. Security Considerations**

Example files can become:

- Attack vectors if modified  
- Sources of schema drift  
- Inconsistent reference materials  

Therefore:

- All examples MUST be checksum-verified  
- All example files MUST be immutable  
- All validator tools MUST load examples in read-only mode  


# **8. Change Log**

- **v0.1 – Initial Draft**
