def predict_health_risk(age, bmi):
    
    if bmi >= 30:
        obesity_risk = "High"
    elif bmi >= 25:
        obesity_risk = "Moderate"
    else:
        obesity_risk = "Low"

    if age > 50 and bmi > 28:
        heart_risk = "High"
    elif age > 40:
        heart_risk = "Moderate"
    else:
        heart_risk = "Low"

    if bmi > 27:
        diabetes_risk = "Moderate"
    elif bmi > 30:
        diabetes_risk = "High"
    else:
        diabetes_risk = "Low"

    return obesity_risk, heart_risk, diabetes_risk