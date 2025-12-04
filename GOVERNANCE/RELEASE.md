# Release Process — PHAROS Ethical Stack

This document defines the release workflow for the E-IP / LDT protocol stack.

---

## 1. Versioning

The project uses **Semantic Versioning**:

```
MAJOR.MINOR.PATCH
```

- **MAJOR** — breaking changes to schemas, definitions, or protocols  
- **MINOR** — new features, backward-compatible  
- **PATCH** — documentation, tooling fixes, non-breaking updates  

---

## 2. Release Cadence

There is no set schedule.  
Releases occur when:
- RFCs are approved  
- Maintainers signal readiness  
- Backward compatibility is validated  

Patch releases may be made anytime as needed.

---

## 3. Release Types

### Patch Release
- Requires 1 maintainer  
- No RFC required  
- Must not modify specs  

### Minor Release
- Requires maintainer consensus  
- Must reference associated RFCs  
- Requires updated changelog  

### Major Release
- Requires full RFC cycle  
- Requires alignment review  
- Requires consensus + Decision Log entry  

---

## 4. Release Steps

1. Ensure all PRs are merged and tests pass  
2. Update version in `VERSION.txt`  
3. Update change log in `RELEASE_NOTES.md` (or root README)  
4. Tag release:

```
git tag -a vX.Y.Z -m "Release X.Y.Z"
git push origin vX.Y.Z
```

5. Publish GitHub release  
6. Announce in discussions  

---

## 5. Backward Compatibility Rules

A release must not:
- Invalidate existing manifests  
- Remove fields without deprecation  
- Introduce schema-breaking changes without MAJOR bump  
- Change semantic interpretation without an alignment review  

---

## 6. Emergency Fixes

Only the **Lead Maintainer** can greenlight an emergency patch.

Criteria:
- Security issue  
- Critical validation failure  
- Protocol-breaking regression  

Must still be logged in Decision Log.

---

## 7. Deprecation Policy

Every deprecation requires:
- RFC or minor PR (depending on scope)  
- Clear justification  
- Sunset timeline  
- Documentation in the release notes  

---

