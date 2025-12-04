# RFC-0004: E-IP Packet Specification
Category: Standards Track  
Status: Proposed Standard  
Year: 2025

## 1. Overview
This RFC defines the official E-IP packet structure, required schemas, and the validation flow. Every object transmitted through the E-IP protocol must comply with these structural rules before entering the Alignment Boundary Layer (ABL) or the Semantic Transport Layer (STL).

This specification describes:

- Packet header schema  
- Packet body schema  
- Alignment envelope schema  
- Semantic checksum rules  
- Ethical flag rules  
- Validation pipeline  
- Error and rejection codes  

## 2. Packet Structure
Every packet in E-IP has two parts:
EIPPacket {
header: EIPHeader
body: EIPBody
}

## 3. Packet Header Schema
The header defines routing, identity, integrity, and alignment metadata.
EIPHeader {
packet_id: string
protocol_version: string
timestamp_utc: string
source: string
destination: string

alignment_envelope: AlignmentEnvelope
semantic_checksum: string
risk_score: number
ethical_flags: string[]
}

### 3.1 Field Definitions
- packet_id: Globally unique identifier for traceability  
- protocol_version: Must match VERSION.txt  
- timestamp_utc: ISO-8601 format  
- source: Origin system identifier  
- destination: Target system identifier  
- alignment_envelope: Full envelope defined in section 4  
- semantic_checksum: Deterministic hash of the body  
- risk_score: 0.0 to 1.0  
- ethical_flags: Flags validated in the ABL  

## 4. Alignment Envelope Schema
The alignment envelope is the core integrity and ethics metadata object that all packets must carry.
AlignmentEnvelope {
intent: string
context_scope: string
semantic_checksum: string
ethical_flags: string[]

lineage: {
parent_ids: string[]
}

risk_score: number
}

### 4.1 Requirements
- All fields are required  
- semantic_checksum must match the packet-level checksum  
- ethical_flags must include any issues detected upstream  
- lineage.parent_ids may be empty but must exist  
- risk_score must be computed before STL admission  

## 5. Packet Body Schema
The body contains the semantic content being transported.
EIPBody {
type: string
payload: object
metadata: object
}

### 5.1 Body Types
Recommended core body types:

- semantic_definition  
- instruction  
- modelcard  
- decision_log  
- alignment_report  
- manifest_update  

## 6. Semantic Checksum Specification
A semantic checksum is a deterministic hash of:
canonical(payload) + canonical(metadata)

Validation rules:

- Must use canonical JSON serialization  
- Must be reproducible byte for byte  
- Must use SHA-256 or stronger  
- Must match between header and alignment envelope  

## 7. Ethical Flags
Ethical flags are structured indicators raised during validation.

Common examples:

- risk_profile_high  
- missing_intent  
- context_mismatch  
- lineage_break  
- checksum_mismatch  
- prohibited_content  

Flags must be deterministic, serializable, and included in both the header and the envelope.

## 8. Validation Pipeline
Validation is performed in three phases.

### 8.1 Phase 1: Structural Validation
- Check required fields  
- Validate schema compliance  
- Validate header structure  

### 8.2 Phase 2: Alignment Validation
- Validate alignment_envelope  
- Compute and confirm risk_score  
- Validate ethical_flags  
- Validate lineage integrity  

### 8.3 Phase 3: Semantic Validation
- Compute checksum  
- Compare with header  
- Validate payload structure  
- Check semantic correctness  

## 9. Rejection Codes
Packets may be rejected with the following codes:

- EIP01 missing required field  
- EIP02 checksum mismatch  
- EIP03 invalid ethical flags  
- EIP04 lineage error  
- EIP05 prohibited content  
- EIP06 risk score too high  

## 10. Security Considerations
This specification prevents:

- Tampering  
- Unauthorized content injection  
- Semantic drift before ingestion  
- Loss of lineage or provenance  

Additional RFCs will define network-level security and consensus requirements.

## 11. Changelog
- v0.1 initial draft





