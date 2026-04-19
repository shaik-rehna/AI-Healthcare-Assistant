from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime

filename = (
f"health_report_"
f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
)

def generate_pdf(report_data):

    pdf = SimpleDocTemplate(
        "health_report.pdf"
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "Healthcare Report",
            styles["Title"]
        )
    )

    content.append(
        Paragraph(
            f"Urgency: {report_data['urgency']}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            "Possible Concerns:",
            styles["Heading2"]
        )
    )

    for item in report_data["possible_concerns"]:
        content.append(
            Paragraph(
                f"- {item}",
                styles["BodyText"]
            )
        )

    content.append(
        Paragraph(
            "Recommended Next Steps:",
            styles["Heading2"]
        )
    )

    for step in report_data["recommended_next_steps"]:
        content.append(
            Paragraph(
                f"- {step}",
                styles["BodyText"]
            )
        )

    pdf.build(content)