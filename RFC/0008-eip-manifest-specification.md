# **RFC-0008: E-IP Manifest Specification**
**Category:** Standards Track  
**Status:** Proposed Standard  
**Year:** 2025  

The Manifest defines the metadata package required for any model, agent, node, or service participating in the E-IP ecosystem.  
It acts as the **identity, capability declaration, and trust surface** for each entity.

Every manifest MUST be machine-readable, deterministic, and signed.


# **1. Purpose**

The Manifest ensures:

- Identity transparency  
- Declared capabilities  
- Declared limitations  
- Declared ethical constraints  
- Declared domain boundaries  
- Version consistency  
- Integrity and auditability  

Nodes MAY NOT participate in E-IP without a valid manifest.


# **2. Required Fields**

All manifests MUST include:

- **manifest_version**
- **entity_id**
- **entity_type** (node, agent, model, service)
- **owner**
- **description**
- **capabilities[]**
- **limitations[]**
- **ethical_policies[]**
- **supported_domains[]**
- **signature**
- **checksum**

Missing required fields MUST produce:

- **MANIFEST-REQUIRED-FIELD-MISSING**


# **3. Entity Types**

Valid entity types:

- **model**  
- **agent**  
- **node**  
- **router**  
- **service**  
- **governance-module**  

Invalid or undefined types MUST produce:

- **MANIFEST-INVALID-ENTITY-TYPE**


# **4. Capability Declarations**

Capabilities MUST be expressed as structured declarations:

Each entry MUST include:

- capability_id  
- description  
- version  
- constraints[]  
- risk_level  

Capabilities MUST NOT be implied; they MUST be explicitly listed.

If a node performs actions not declared, the system MUST emit:

- **MANIFEST-UNDECLARED-CAPABILITY**


# **5. Limitation Declarations**

Entities MUST declare limitations such as:

- domain restrictions  
- performance ceilings  
- privacy constraints  
- operational risk factors  
- transformation boundaries  

These are used by ABL + STL to prevent unsafe routing or transformation.

Missing limitation declarations MUST produce:

- **MANIFEST-LIMITATIONS-MISSING**


# **6. Ethical Policies**

Each manifest MUST embed ethical policies that define:

- behavior restrictions  
- forbidden outputs  
- safety rules  
- transformation constraints  
- override escalation paths  

Each policy entry MUST include:

- rule_id  
- severity  
- description  
- enforcement_action  

Nodes MUST NOT operate without at least **one ethical policy**.

Violation MUST result in:

- **MANIFEST-ETHICS-INVALID**


# **7. Domain Boundaries**

Manifests MUST declare which domains the entity may operate in:

- linguistic  
- cultural  
- legal  
- safety-critical  
- scientific  
- interpersonal  
- enterprise  
- medical  
- open general  

Nodes attempting to operate outside their declared domain MUST trigger:

- **MANIFEST-DOMAIN-VIOLATION**


# **8. Versioning Requirements**

Manifest versioning MUST follow:

- **MAJOR.MINOR.PATCH**

Rules:

- Breaking changes → increment **MAJOR**  
- Additive, non-breaking → increment **MINOR**  
- Fixes → increment **PATCH**  

Manifest version MUST match:

- The version of the SDF  
- The version of ethical policies  
- The version of declared capabilities  

If mismatch:

- **MANIFEST-VERSION-MISMATCH**


# **9. Trust & Signature Requirements**

Every manifest MUST include:

- **signature** (entity private key)
- **checksum** (SHA-256 or stronger)
- **signature_timestamp**

Nodes MUST verify manifests **before any packet exchange**.

If verification fails:

- **MANIFEST-SIGNATURE-INVALID**
- **MANIFEST-CHECKSUM-MISMATCH**


# **10. Validation Flow**

Validation MUST occur in the following order:

1. Check schema  
2. Check required fields  
3. Verify checksum  
4. Verify signature  
5. Validate entity type  
6. Validate capabilities  
7. Validate ethical policies  
8. Validate domains  
9. Validate version compatibility  

Any failure MUST halt operation and produce a failure code.


# **11. Security Considerations**

The manifest acts as a **root identity artifact**.

Therefore:

- It MUST be immutable except via versioning  
- It MUST be cryptographically signed  
- It MUST be verified on each load  
- It MUST be included in all routing decisions  
- It MUST be cached only with secure TTL  
- It MUST NOT include sensitive personal information  

If compromise is suspected, nodes MUST emit:

- **MANIFEST-REVOKE-IMMEDIATE**


# **12. Change Log**

- **v0.1** — Initial Draft
