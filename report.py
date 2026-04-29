from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(bmi, score, calories, diet, workout, goal):

    doc = SimpleDocTemplate("health_report.pdf")
    styles = getSampleStyleSheet()

    content = []

    # Title
    content.append(Paragraph("AI Health Report", styles["Title"]))
    content.append(Spacer(1, 10))

    # Basic metrics
    content.append(Paragraph(f"BMI: {round(bmi,2)}", styles["Normal"]))
    content.append(Paragraph(f"Health Score: {score}", styles["Normal"]))
    content.append(Paragraph(f"Calories: {calories}", styles["Normal"]))
    content.append(Paragraph(f"Goal: {goal}", styles["Normal"]))
    content.append(Spacer(1, 10))

    # AI Insight
    if score > 80:
        insight = "Great condition. Maintain your routine."
    elif score > 60:
        insight = "Moderate health. Improve consistency."
    else:
        insight = "Needs improvement. Focus on diet and exercise."

    content.append(Paragraph("AI Insight:", styles["Heading2"]))
    content.append(Paragraph(insight, styles["Normal"]))
    content.append(Spacer(1, 10))

    # Diet
    content.append(Paragraph("Diet Plan:", styles["Heading2"]))
    for k, v in diet.items():
        content.append(Paragraph(f"{k}: {v}", styles["Normal"]))

    content.append(Spacer(1, 10))

    # Workout
    content.append(Paragraph("Workout Plan:", styles["Heading2"]))
    for w in workout:
        content.append(Paragraph(w, styles["Normal"]))

    content.append(Spacer(1, 10))

    # Summary
    content.append(Paragraph("Weekly Recommendation:", styles["Heading2"]))
    content.append(Paragraph("Stay consistent and track your progress daily.", styles["Normal"]))

    doc.build(content)