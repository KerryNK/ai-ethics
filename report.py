def generate_compas_audit_report(metrics):
    report = f"""
## COMPAS Recidivism Dataset Bias Audit Report

This audit analyzes the COMPAS Recidivism Dataset for racial bias in risk assessment scores using AI Fairness 360.

### Key Findings

- False Positive Rate (Caucasian): {metrics['False Positive Rate (Caucasian)']:.3f}
- False Positive Rate (African-American): {metrics['False Positive Rate (African-American)']:.3f}
- Disparate Impact: {metrics['Disparate Impact']:.3f}
- Average Odds Difference: {metrics['Average Odds Difference']:.3f}

The results indicate a higher false positive rate for African-American defendants compared to Caucasian defendants. The disparate impact and average odds difference metrics confirm the presence of racial bias in the risk predictions.

### Recommendations

- Regular Algorithmic Auditing: Continuously monitor and audit risk assessment tools for bias.
- Transparency: Clearly communicate how risk scores are calculated and used.
- Bias Mitigation: Consider reweighing, preprocessing, or postprocessing techniques to reduce bias.
- Stakeholder Engagement: Involve affected communities in reviewing and improving AI systems.

Addressing these issues is crucial for ensuring fairness and equity in criminal justice risk assessments.
"""
    return report.strip()
