# RFC Submission Guide — PHAROS Ethical Stack

This guide explains how contributors submit new RFCs for protocol changes.

---

## 1. When You MUST Submit an RFC

An RFC is required for:

- Changes to E-IP core behaviors  
- Semantic field additions or removals  
- Updates to schema or manifest structure  
- Protocol-level normative rules  
- Governance model changes  
- New layers (interpretation, transparency, compliance)  
- New categories of tooling (validators, detectors, scoring)  

If you are unsure — **submit an RFC**.

---

## 2. Workflow Overview

### Step 1 — Open an Issue
Discuss the idea:  
- Problem to solve  
- Proposed direction  
- Rough outline  

### Step 2 — Draft the RFC
Create the file:

```
/RFC/####-title.md
```

Use the template at `/RFC/TEMPLATE.md`.

### Step 3 — Submit Pull Request
The PR MUST include:
- Link to issue  
- Rationale  
- Ethical considerations  
- Any diagrams or schema diffs  

### Step 4 — Community Feedback
Discussion occurs openly.

### Step 5 — Maintainer Review
Maintainters evaluate:
- Technical correctness  
- Security  
- Alignment risks  
- Backward compatibility  

### Step 6 — Decision Log
Maintainters record the outcome in an entry inside `/DECISIONS/`.

### Step 7 — Merge or Reject

---

## 3. Review Expectations

RFCs should be:

- **Clear** — free of jargon  
- **Specific** — include detailed definitions  
- **Minimal** — change only what’s required  
- **Ethically aligned** — must include risk evaluation  
- **Backwards-aware** — note compatibility concerns  

---

## 4. Ethical Alignment Requirement

Every RFC MUST include:
- Semantic drift analysis  
- Misuse scenarios  
- Interpretational ambiguity considerations  
- LDT semantic-consistency justification  
- Human-impact considerations  

RFCs without this will be rejected.

---

## 5. After Approval

If accepted:

- Update specs  
- Update schemas  
- Update validators  
- Add examples  
- Mention in release notes  
- Bump version as required  

---

## 6. Withdrawing an RFC

Add:
```
Status: Withdrawn
```
Keep the file.  
Never delete RFC history.

---

## 7. Example File Tree

```
/RFC/
  0001-initial-governance.md
  0002-semantic-fields.md
  0003-alignment-validator.md
  TEMPLATE.md
  RFC_INDEX.md
```

