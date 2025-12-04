# Roles & Responsibilities — PHAROS Ethical Stack

This document defines all primary roles used in governance, contribution, and decision-making.

---

## 1. Contributors

Anyone submitting:
- Issues  
- Pull requests  
- Discussions  
- RFCs  

**Authority level:**  
- No decision power  
- Can propose anything  
- Can participate in discussions  

---

## 2. Maintainers

Trusted stewards responsible for:
- Reviewing PRs  
- Approving RFCs  
- Managing releases  
- Enforcing governance  

**Authority level:**  
- Full technical decision-making authority  
- Must follow consensus rules  

See MAINTAINERS.md for details.

---

## 3. Lead Maintainer

Responsibilities:
- Break consensus deadlocks  
- Ensure RFCs move forward  
- Manage release cadence  
- Represent the project externally  

**Authority level:**  
- Final decision-maker only if consensus fails  
- Cannot override ethical alignment checks  

---

## 4. Ethics Reviewers

Optional role for advanced governance.

Responsibilities:
- Review RFCs for ethical alignment  
- Evaluate semantic drift risks  
- Apply LDT interpretational guidance  
- Conduct Alignment Reviews  

**Authority level:**  
- Can block any change on ethical grounds  
- Must document justification in Decision Log  

---

## 5. Release Managers

Optional rotating role.

Responsibilities:
- Update version numbers  
- Prepare release notes  
- Validate backwards compatibility  
- Coordinate with Maintainers  

**Authority level:**  
- Patch-level merges  
- No governance authority  

---

## 6. Diagram Architect (optional)

Responsible for:
- Architecture diagrams  
- Stack visualizations  
- Semantic layering illustrations  

**Authority level:**  
- No governance authority  
- Provides clarity tools for community  

---

## 7. Tools Maintainer (optional)

Responsible for:
- Validators  
- Scanners  
- Drift detectors  
- CLI tools  

**Authority level:**  
- Maintainer authority within tooling directory  

---

## 8. Community Manager (optional)

Responsible for:
- Issue triage  
- Documentation improvements  
- New contributor onboarding  

**Authority level:**  
- No merging authority  

---

## 9. Summary Table

| Role | Decision Power | Technical Authority | Ethical Authority |
|------|----------------|---------------------|-------------------|
| Contributor | ❌ | ❌ | ❌ |
| Maintainer | ✔️ | ✔️ | Limited |
| Lead Maintainer | Breaks ties | ✔️ | Limited |
| Ethics Reviewer | Block on ethics | Limited | ✔️ |
| Release Manager | Patch-level | ✔️ | ❌ |

