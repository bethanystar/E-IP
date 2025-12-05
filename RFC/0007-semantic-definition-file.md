# **RFC-0007: Semantic Definition File (SDF) Specification**

**Category:** Standards Track  
**Status:** Proposed Standard
**Year:** 2025  

# **1. Overview**

The Semantic Definition File (SDF) is the authoritative semantic contract for any entity participating in the E-IP ecosystem.  
It defines meaning, intent ranges, contextual boundaries, validation rules, and ethical constraints required for semantic integrity.

SDFs allow nodes, agents, and domains to establish *shared semantic ground truth* and provide the inputs needed for:

- semantic routing  
- alignment scoring  
- risk computation  
- intent validation  
- meaning-preserving transformation  
- cross-domain interoperability  

Every domain MUST maintain at least one SDF, and every packet referencing a semantic domain MUST resolve to a valid definition.

---

# **2. Responsibilities of the SDF**

The SDF must:

- Define canonical meaning for semantic entities  
- Specify allowed transformations  
- Provide domain context boundaries  
- Define ethical constraints  
- Declare required metadata fields  
- Provide checksum rules  
- Declare prohibited mutations  
- Establish consistency requirements  
- Enable cross-domain mapping  

The SDF MUST be versioned and cryptographically signed.

---

# **3. SDF Architecture**

## **3.1 Core Structure**

Every SDF MUST include:

- `domain_id`  
- `version`  
- `canonical_definition`  
- `intent_taxonomy[]`  
- `contextual_boundaries[]`  
- `ethical_constraints[]`  
- `transformation_rules[]`  
- `checksum_rules`  
- `prohibited_mutations[]`  
- `cross_domain_mappings[]`  

## **3.2 Versioning Rules**

SDFs follow semantic versioning:

- **MAJOR:** meaning changes  
- **MINOR:** taxonomy/context updates  
- **PATCH:** typo or metadata fixes  

Nodes MUST reject packets referencing deprecated MAJOR versions unless explicitly permitted.

## **3.3 Integrity Requirements**

Every SDF MUST generate:

- `sdf_checksum`  
- `signature` (ECDSA or domain-approved algorithm)  
- `lineage`  

Nodes MUST verify all three before using the SDF for routing or validation.

---

# **4. SDF Schema**

## **4.1 Schema Definition (JSON)**

```json
{
  "domain_id": "string",
  "version": "string",
  "canonical_definition": "string",
  "intent_taxonomy": [
    {
      "intent_id": "string",
      "description": "string",
      "allowed_ranges": []
    }
  ],
  "contextual_boundaries": [
    {
      "boundary_id": "string",
      "scope": "string",
      "constraints": []
    }
  ],
  "ethical_constraints": [
    {
      "constraint_id": "string",
      "description": "string",
      "severity": "low|medium|high|critical"
    }
  ],
  "transformation_rules": [
    {
      "rule_id": "string",
      "type": "mutation|translation|compression",
      "conditions": [],
      "output_format": "string"
    }
  ],
  "checksum_rules": {
    "algorithm": "SHA3-256",
    "parameters": {}
  },
  "prohibited_mutations": [],
  "cross_domain_mappings": [
    {
      "target_domain": "string",
      "mapping_rules": []
    }
  ],
  "sdf_checksum": "string",
  "signature": "string",
  "lineage": {
    "parent_versions": []
  }
}
```
# **5. Intent Taxonomy Specification**

## **5.1 Requirements**

Each intent entry in the SDF MUST include:

- **intent_id** (unique identifier)
- **description**
- **allowed_ranges[]**
- **conflict_rules[]**
- **allowed_mutation_classes[]**

The taxonomy establishes the semantic boundaries within which all packets must operate.

## **5.2 Conflict Handling**

If two intents are mutually exclusive, the SDF MUST declare:

- `conflicts_with[]`

When detected:

- The **Semantic Router MUST block routing**.
- The **ABL MUST reject validation**.
- The system MUST emit: **SDF-INTENT-CONFLICT**

## **5.3 Expansion Rules**

Intent taxonomies MAY expand in **MINOR version updates**.

Intent definitions:

- MUST remain semantically stable  
- MUST NOT redefine existing meaning  
- MUST NOT narrow previously valid intent ranges  

Breaking changes require a **MAJOR version update**.


# **6. Contextual Boundary Model**

## **6.1 Boundary Types**

Domains MAY define:

- **Scope boundaries**  
- **Geographic boundaries**  
- **Ethical boundaries**  
- **Temporal boundaries**  
- **Regulatory boundaries**  

Each boundary MUST include:

- `boundary_id`  
- `scope`  
- `constraints[]`  

## **6.2 Enforcement**

The **ABL MUST enforce contextual boundaries** before any packet reaches the STL.

Packets violating a boundary MUST NOT propagate.

## **6.3 Violation Codes**

Boundary violations MUST generate:

- **SDF-CTX-INVALID**  
- **SDF-RANGE-EXCEEDED**  
- **SDF-BOUNDARY-BLOCK**  


# **7. Ethical Constraint Framework**

## **7.1 Severity Levels**

Severity levels MUST be one of:

- **low**  
- **medium**  
- **high**  
- **critical**  

## **7.2 Mandatory Enforcement**

- **Critical** constraints MUST result in rejection.  
- **High** constraints MAY allow transformation with justification.  
- **Medium/Low** constraints provide advisory warnings.

## **7.3 Ethical Drift Detection**

Nodes MUST detect semantic or behavioral drift.

Violations MUST emit:

- **SDF-ETHICAL-DRIFT**


# **8. Transformation Rules**

## **8.1 Allowed Types**

The SDF MAY declare allowed transformations:

- **semantic mutation**  
- **compression**  
- **contextual translation**  
- **cross-domain translation**  

Each transformation MUST declare:

- `rule_id`  
- `type`  
- `conditions[]`  
- `output_format`  

## **8.2 Forbidden Types**

Forbidden transformations MUST be listed in:

- `prohibited_mutations[]`

Any attempt MUST generate:

- **SDF-PROHIBITED-MUTATION**  


# **9. Cross-Domain Mappings**

Cross-domain mappings MUST specify:

- target domain  
- mapping rules  
- compatibility requirements  
- lossless vs lossy mapping indicators  
- fallback behaviors  

Cross-domain routing MUST validate mapping integrity before packet transformation.


# **10. Validation Requirements**

Nodes MUST validate:

- **Schema conformity**  
- **SDF checksum**  
- **Signature authenticity**  
- **Lineage correctness**  
- **Domain compatibility**  

Failures MUST return one of:

- **SDF-INVALID**  
- **SDF-CHECKSUM-MISMATCH**  
- **SDF-SIGNATURE-FAIL**  
- **SDF-LINEAGE-ERROR**  


# **11. Security Considerations**

The SDF functions as a **semantic root of trust**.

Therefore, every SDF MUST be:

- **Cryptographically signed**  
- **Immutable except through versioning**  
- **Replicated across trusted nodes**  
- **Verified at load and runtime**  

If compromise is detected, nodes MUST trigger:

- **SDF-REVOKE-URGENT**  


# **12. Change Log**

- **v0.1** — Initial Draft
