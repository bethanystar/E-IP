# Governance Model — PHAROS Ethical Stack (E-IP / LDT Protocols)

This document defines how decisions are made, who has authority, and how changes enter the protocol. It is intentionally lightweight, transparent, and scalable for open-source growth.

---

## 1. Core Principles

- **Transparency**  
  All decisions, changes, and debates must be logged publicly using the Decision Log (DL) format.

- **Open Participation**  
  Anyone may propose improvements through RFCs, issues, or discussions.

- **Role-Based Accountability**  
  Authority is assigned to roles, not individuals.

- **Ethical Integrity**  
  Changes must preserve the PHAROS Ethical Stack: safety, alignment, transparency, and human-centric principles.

- **Protocol Stability**  
  Backward compatibility is strongly preferred unless breaking changes are explicitly justified in an RFC.

---

## 2. Governance Structure

### 2.1 Maintainers
Maintainers are responsible for custodianship of the repository.  
They:
- Review and merge pull requests  
- Approve or reject RFCs  
- Enforce coding, documentation, and ethical standards  
- Manage releases and versioning  

Maintainers operate via **rough consensus**, documented in the Decision Log.

See `MAINTAINERS.md` for specific responsibilities.

---

## 3. Decision-Making Process

### 3.1 Daily Decisions
For small, non-spec-altering changes (typos, formatting, CI fixes):  
- Maintainer merges after a quick sanity check  
- No RFC required  

### 3.2 Significant Changes
Anything affecting the protocol, schemas, definitions, or governance requires an **RFC**
