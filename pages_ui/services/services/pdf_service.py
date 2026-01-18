import io
import pytesseract
from pdf2image import convert_from_bytes
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_resume_pdf(data,template):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)

    width, height = A4
    x = 40
    y = height - 40

    c.setFont("Helvetica-Bold", 16)
    c.drawString(x, y, data["name"])
    y -= 25

    c.setFont("Helvetica", 10)
    c.drawString(x, y, f"Email: {data['email']}")
    y -= 15
    c.drawString(x, y, f"LinkedIn: {data['linkedin']}")
    y -= 15
    c.drawString(x, y, f"GitHub: {data['github']}")
    y -= 25

    def draw_section(title, content):
        nonlocal y
        c.setFont("Helvetica-Bold", 12)
        c.drawString(x, y, title)
        y -= 15

        c.setFont("Helvetica", 10)
        for line in content.split("\n"):
            c.drawString(x, y, line)
            y -= 14
        y -= 10

    draw_section("About", data["about"])
    draw_section("Skills", data["skills"])
    draw_section("Projects", data["projects"])

    c.showPage()
    c.save()
    buffer.seek(0)

    return buffer

def extract_text_from_resume(uploaded_file):
    images = convert_from_bytes(uploaded_file.read())
    text = ""

    for img in images:
        text += pytesseract.image_to_string(img)

    return text
