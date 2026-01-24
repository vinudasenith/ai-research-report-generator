import markdown2
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def md_to_pdf(md_text, pdf_path="report.pdf"):
    html = markdown2.markdown(md_text)
    pdf = SimpleDocTemplate(pdf_path)
    styles = getSampleStyleSheet()
    pdf.build([Paragraph(html, styles["Normal"])])