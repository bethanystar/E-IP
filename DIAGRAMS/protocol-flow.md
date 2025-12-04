# Protocol Flow Diagram Explanation

## Overview
This diagram illustrates the lifecycle of an E-IP transaction, from creation through validation, alignment checks, and governance review (if required).

### Flow Steps

1. **Input Event / System Action**
   - Agent or model attempts an action.
   - A manifest is generated describing intent and contextual information.

2. **Semantic Validation**
   - Terms are validated against the Semantic Layer.
   - Definitions and references are checked for consistency.

3. **Alignment Validation**
   - Risk scoring  
   - Consent and agency boundaries  
   - Contextual drift detection  
   - Ethical constraints  

4. **Execution Decision**
   - APPROVE  
   - APPROVE WITH SAFEGUARDS  
   - REJECT  

5. **Governance Path (If Protocol Change)**
   - RFC triggered  
   - Maintainer review  
   - Alignment & Semantic review  
   - Decision Log entry created

6. **Immutable Record**
   - Final action logged in Decision Logs.
