from fpdf import FPDF
import pandas as pd



# Load the Excel file
df = pd.read_excel('C:/Users/hp/PycharmProjects/FirstpythonProject/final.xlsx')

# Create a PDF document
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Set font for the PDF
pdf.set_font("Arial", size=12)

# Add a title to the PDF
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="Biographical Details", ln=True, align='C')
pdf.ln(10)


# Function to format text in the PDF with numbering
def add_line(pdf, number, title, content):
    pdf.set_font("Arial", 'B', 12)
    # Add numbering with name, starting from 1
    numbered_title = f"{number}. {title}"
    pdf.cell(200, 10, txt=numbered_title.encode('latin-1', 'replace').decode('latin-1'), ln=True, align='L')
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=content.encode('latin-1', 'replace').decode('latin-1'))
    pdf.ln(5)


# Loop through the DataFrame and add the data to the PDF with numbering
for index, row in df.iterrows():
    number = index + 1  # Correcting the numbering by starting from 1
    name = f"Name: {row['NAME']}"
    bio = f"Biography: {row['Biography']}"

    # Add details with numbering to the PDF
    add_line(pdf, number, name, bio)

# Save the PDF file
pdf.output('biographical_details(1).pdf')

print("Correctly numbered PDF created successfully!")
