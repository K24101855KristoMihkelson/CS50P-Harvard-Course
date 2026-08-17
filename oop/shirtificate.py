from fpdf import FPDF

name = input("Name: ")
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(False)
pdf.set_font("Helvetica", "B", 40)
pdf.cell(0, 30, "CS50 Shirtificate", align="C", ln=True)
pdf.image("shirtificate.png", x=10, y=60, w=190)
pdf.set_font("Helvetica", "B", 24)
pdf.set_text_color(255, 255, 255)
pdf.text(55, 140, f"{name} took CS50")
pdf.output("shirtificate.pdf")
