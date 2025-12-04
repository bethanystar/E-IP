# Decision Log Flow Diagram Explanation

## Flow Steps

1. **Trigger Event**
   - Merge, rejection, alignment issue, drift alert

2. **Create Decision Log Draft**
   - Follows schema:
     - actor
     - context
     - decision type
     - rationale
     - timestamp

3. **Cross-Layer Signoff**
   - Maintainers  
   - Semantic Stewards  
   - Alignment Reviewers  

4. **Publication**
   - Immutable entry stored
   - Linked to RFC or commit

5. **Reference**
   - Used in future decisions  
   - Ensures coherent governance over time  
