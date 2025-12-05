# Ethical Alignment Review (EAR) Process

Any change affecting user rights, agent autonomy, data, or safety must undergo an EAR using the E-IP Alignment Protocol.

## Steps
1. **Identify Ethical Impact**
   - Does the change modify agent behavior?
   - Does it alter risk exposure?
   - Does it introduce new failure or coercion modes?

2. **Assessment Using E-IP Alignment Criteria**
   - Human agency preservation  
   - Transparency  
   - Contextual boundaries  
   - Consent integrity  
   - Misalignment risk scoring  
   - Downstream consequences  

3. **Evaluator Roles**
   - At least 2 Alignment Reviewers required.

4. **Outcome Types**
   - **APPROVED** — No ethical conflict detected.
   - **APPROVED WITH SAFEGUARDS** — Must implement additional constraints.
   - **REJECTED** — Ethical conflict cannot be mitigated.

5. **Documentation**
   - Completed in `/DECISIONLOG/`.
   - Must pass schema validation.

6. **Escalation**
   - If reviewers disagree → escalate to Governance Chair.
   - If still unresolved → deferred to public comment.
