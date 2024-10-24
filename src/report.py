from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO

def create_overlay(header_text, footer_text, page_number, page_size):
    """Create a PDF overlay with a header and footer for a specific page"""
    packet = BytesIO()
    can = canvas.Canvas(packet, pagesize=page_size)
    width, height = page_size
    can.setFont("Helvetica", 10)  # Set header font to Helvetica-Bold, size 14
    can.setFillColorRGB(0.5, 0.5, 0.5)  # Set color to  gray
    # Add header
    can.drawString(20,
        float(height) - 20.0,
        header_text
    )  # Adjust the position of the header

    # Add footer
    can.drawString(20, 20, footer_text)  # Footer text
    can.drawRightString(
        float(width) - 20,
        20,
        f"Page {page_number}")  # Right-aligned page number

    can.save()
    packet.seek(0)
    return packet

def add_header_footer_to_pdf(input_pdf_path, output_pdf_path, header_text, footer_text):
    # Read the existing PDF
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    # Process each page
    for page_number in range(len(reader.pages)):
        # Get the size of the current page
        page = reader.pages[page_number]
        page_size = (page.mediabox.width, page.mediabox.height)

        # Create a header/footer overlay for the current page
        overlay_pdf = create_overlay(header_text, footer_text, page_number + 1, page_size)

        # Read the overlay PDF
        overlay_reader = PdfReader(overlay_pdf)
        overlay_page = overlay_reader.pages[0]

        # Merge the overlay with the original page
        page.merge_page(overlay_page)

        # Add the modified page to the writer
        writer.add_page(page)

    # Write the final output to a new PDF
    with open(output_pdf_path, "wb") as output_file:
        writer.write(output_file)

# Usage example
input_pdf = "S05.04.nginx-sqlite-vue.pdf"  # Path to the original PDF
output_pdf = "output_with_header_footer.pdf"  # Path to the output PDF
header_text = "Document title Docker etc "
footer_text = "Author and links"

add_header_footer_to_pdf(input_pdf, output_pdf, header_text, footer_text)

