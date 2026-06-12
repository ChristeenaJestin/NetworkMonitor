from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

def generate_pdf_report(
    alerts,
    filename="reports/security_report.pdf"
):

    doc = SimpleDocTemplate(
        filename
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "NetSentry AI Security Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1,12)
    )

    if alerts:

        for alert in alerts:

            content.append(
                Paragraph(
                    str(alert),
                    styles["BodyText"]
                )
            )

    else:

        content.append(
            Paragraph(
                "No alerts detected.",
                styles["BodyText"]
            )
        )

    doc.build(content)

    return filename