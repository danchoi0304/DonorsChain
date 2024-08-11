import qrcode
from reportlab.lib.pagesizes import mm
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)
    return filename

def create_pdf_with_qrs(links):
    pdf_filename = 'qr_code_pages.pdf'
    c = canvas.Canvas(pdf_filename, pagesize=(40*mm, 30*mm))

    for i, link in enumerate(links):
        qr_image_file = f'temp_qr_code_{i}.png'
        generate_qr_code(link, qr_image_file)

        # Calculate the position to center the QR code on the page
        page_width, page_height = 40*mm, 30*mm
        qr_code_size = 20*mm  # Adjust as necessary to fit the page
        text_height = 5*mm
        margin = 2*mm
        x = (page_width - qr_code_size) / 2
        y = (page_height - qr_code_size - text_height - margin) / 2

        # Add text above the QR code
        c.setFont("Helvetica", 10)
        text_x = page_width / 2
        text_y = y + qr_code_size + text_height
        c.drawCentredString(text_x, text_y, "DonorsChain")

        # Draw the QR code image on the PDF
        c.drawImage(qr_image_file, x, y, qr_code_size, qr_code_size)
        c.showPage()  # Create a new page for the next QR code

    c.save()
    print(f"PDF with QR codes created: {pdf_filename}")

if __name__ == "__main__":
    links = input("Enter the links separated by spaces: ").split()
    create_pdf_with_qrs(links)