# RFC 0003 — E-IP Protocol Stack (Layer Model)
**Category:** Standards Track  
**Status:** Draft  
**Created:** 2025-12-04  
**Author:** Pharos Society / Bethany W.  
**Supersedes:** None  
**Depends on:** RFC-0001 (Governance Framework), RFC-0002 (Semantic Architecture & ABL)

---

# 1. Summary
This RFC defines the canonical **E-IP Protocol Stack**: the layered architecture, responsibilities of each layer, and their normative interfaces. The stack organizes semantic, alignment, routing, and application responsibilities so implementers and auditors can reason about conformance, interoperability, and governance.

This RFC provides:
- The layer diagram and descriptions  
- Layer-to-layer contracts (inputs, outputs, invariants)  
- Minimal normative behaviors required for compliance  
- Example flows for common operations  
- Interoperability notes with existing internet stacks

---

# 2. Motivation
To be a usable protocol, E-IP must present a clear stack that:
- Separates concerns (semantics vs transport vs governance)  
- Provides modular implementation boundaries  
- Enables independent auditing and tooling per layer  
- Ensures semantic integrity can be enforced consistently

RFC-0003 gives implementers the map to build, test, and certify E-IP components.

---

# 3. Canonical Layer Stack
The E-IP canonical stack (bottom to top):

L0 — Symbolic Grounding Layer (SGL)
L1 — Alignment Boundary Layer (ABL)
L2 — Semantic Transport Layer (STL)
L3 — Ethical Routing Layer (ERL)
L4 — Application Integrity Layer (AIL)

Each layer has explicit responsibilities and a small, stable interface to the adjacent layers.

---

# 4. Layer Definitions and Contracts

## L0 — Symbolic Grounding Layer (SGL)
**Purpose:** Provide the foundational semantic primitives and canonical definitions referenced by higher layers.  
**Responsibilities:**
- Maintain canonical term definitions (glossary, ontologies)  
- Provide semantic baseline snapshots (versioned)  
- Offer canonical interpreters or reference implementations for meaning_graph extraction  
**Inputs:** Schema updates, glossary entries, LDT formal definitions  
**Outputs:** Canonical term set, baseline meaning_graphs, SGL-version tag  
**Invariants:** Definitions are authoritative for a particular SGL-version; any change requires RFC and semantic review.

---

## L1 — Alignment Boundary Layer (ABL)
**Purpose:** Enforce alignment rules and attach an Alignment Envelope to content. (See RFC-0002.)  
**Responsibilities:**
- Validate alignment_envelope fields  
- Compute alignment_score or call verifier services  
- Emit alignment status and flags  
**Inputs:** Packets with alignment_envelope, SGL baseline  
**Outputs:** Validated/Rejected packet, alignment metadata, misalignment events  
**Invariants:** Packets accepted by higher layers must pass ABL checks (or be explicitly downgraded with recorded risk).

---

## L2 — Semantic Transport Layer (STL)
**Purpose:** Transport semantically enriched E-IP packets across nodes while preserving semantic context and lineage.  
**Responsibilities:**
- Route E-IP packets preserving alignment_envelope and lineage metadata  
- Maintain hop-by-hop logging of semantic changes  
- Provide guarantees for lineage immutability across transports  
**Inputs:** ABL-validated packets, routing metadata  
**Outputs:** Delivered packets, route logs, lineage proofs  
**Invariants:** Semantics and lineage must not be altered silently; any transformation must produce new lineage entries.

---

## L3 — Ethical Routing Layer (ERL)
**Purpose:** Determine eligible routes and policy-based forwarding considering ethical constraints and governance hooks.  
**Responsibilities:**
- Evaluate route policies against ethical flags and governance rules  
- Apply slow-path routing for high-risk packets (manual or multi-actor review)  
- Provide routing decisions with audit evidence  
**Inputs:** STL packets, governance policies, risk thresholds  
**Outputs:** Route decision (fast-path / slow-path), audit evidence, escalation triggers  
**Invariants:** Routing cannot bypass governance constraints; ERL logs decisions for auditors.

---

## L4 — Application Integrity Layer (AIL)
**Purpose:** Application-level enforcement, integrity checks, and final decision execution.  
**Responsibilities:**
- Consume packets and enforce application-specific invariants  
- Translate alignment outcomes into app actions (allow, deny, require review)  
- Expose human-readable justifications and decision logs  
**Inputs:** ERL-delivered packets, user policies, app state  
**Outputs:** Actions executed, decision logs, user notifications  
**Invariants:** Application behavior must reference alignment metadata and maintain traceability to lineage.

---

# 5. Layer Interfaces (Normative)

## Interface: SGL → ABL
- `SGL_version` tag required in alignment_envelope  
- ABL uses canonical definitions for semantic_checksum calculations

## Interface: ABL → STL
- `alignment_status`, `alignment_score` appended to packet header  
- `lineage` must reference SGL term IDs and parent packet IDs

## Interface: STL → ERL
- `route_metadata` includes risk flags and required governance hooks  
- ERL must provide `route_decision_id` for audit linkage

## Interface: ERL → AIL
- `delivery_decision` object with `action`, `justification`, `audit_refs`  
- AIL must store `audit_refs` and decision logs

All interfaces must be documented in machine-readable schema fragments in `/SPEC`.

---

# 6. Example Flows

## 6.1 Normal Flow (Low Risk)
1. Application constructs content and builds `alignment_envelope` (intent, context).  
2. ABL validates envelope and computes `alignment_score`.  
3. STL wraps packet, appends lineage, and transports it.  
4. ERL evaluates routing policy and allows fast-path.  
5. AIL executes action and logs decision.

## 6.2 High-Risk Flow (Slow Path)
1. Packet flagged by ABL with `risk_score > threshold`.  
2. ERL routes to slow-path: requires multi-actor review.  
3. Reviewers consult SGL, ABL reports, make decision.  
4. Decision recorded in Decision Log and attached to packet lineage.

---

# 7. Compliance and Conformance

## Musts (Normative)
- Any E-IP node must implement ABL checks (L1) before delivering to higher layers.  
- Any transformation to content must result in a new lineage entry.  
- Audit traces must be append-only and verifiable.

## Shoulds (Non-normative guidance)
- Implement drift detectors between SGL snapshots.  
- Provide public endpoints for alignment decision transparency.

---

# 8. Interoperability with TCP/IP and Application Stacks
E-IP is designed as a logical layer that maps onto existing transport and security stacks:

- **Encapsulation pattern:** E-IP packets may be carried over HTTPS or within application-level headers.  
- **Tunnel usage:** For compatibility, STL may use TLS tunnels but must preserve alignment_envelope integrity.  
- **DNS/Service discovery:** ERL may leverage existing service discovery mechanisms but must not delegate governance checks to external discovery services.

---

# 9. Auditing and Observability
Each layer must emit:
- `layer_event` records with timestamps, actor_id, and decision metadata  
- Persistent links to Decision Log entries for governance review  
- Lineage proofs that allow reconstructing semantic transformation chains

Observability data should be structured and machine readable (JSON or canonical serialization) and accessible to authorized auditors.

---

# 10. Security Considerations
- **Tampering:** Lineage and alignment envelopes must be cryptographically signed to prevent alteration.  
- **Privacy:** Alignment envelopes should minimize personal data; protocols must support selective redaction with traceable redaction metadata.  
- **Denial of Service:** ERL must throttle high-risk or high-volume packets; abuse patterns must be logged.  
- **Trust anchors:** Nodes must maintain trust material for verifying signatures and alignment verifications.

---

# 11. Governance and Versioning
- Layer interface changes require RFC and semantic review.  
- Each node declares the supported SGL and ABL versions in its manifest.  
- Backwards compatibility rules from RFC-0001 apply.

---

# 12. Example Schema Stub (for interface)
Here is a minimal illustrative JSON fragment for `eip_packet.header`:

```json
{
  "version": "EIP/1.0",
  "sender_id": "did:example:abc123",
  "timestamp": "2025-12-04T12:00:00Z",
  "sgl_version": "SGL-2025-01",
  "route_metadata": {
    "hop_limit": 16,
    "required_review": false
  }
}
And an alignment_envelope stub:
{
  "intent": "update-user-preferences",
  "ethical_flags": ["user_consent_required"],
  "semantic_checksum": "sha256-meaning-...",
  "lineage": { "parent_ids": [] },
  "context_scope": "user-settings",
  "risk_score": 0.12
}
Concrete schema files belong in /SPEC and must be linked to this RFC.
13. Changelog

2025-12-04: Initial draft.
::contentReference[oaicite:0]{index=0}
