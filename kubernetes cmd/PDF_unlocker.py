from PyPDF2 import PdfReader, PdfWriter

# Input and output file paths
input_pdf = "D:\workspace\kubernetes cmd\Mutual_Funds_ELSS_Statement_01-04-2024_31-03-2025.pdf"
output_pdf = "unlocked.pdf"
password = "IIOPK5430C"

# Read the encrypted PDF
reader = PdfReader(input_pdf)
reader.decrypt(password)

# Write to a new PDF without password
writer = PdfWriter()
for page in reader.pages:
    writer.add_page(page)

with open(output_pdf, "wb") as output_file:
    writer.write(output_file)

print("Password removed and new PDF saved!")
