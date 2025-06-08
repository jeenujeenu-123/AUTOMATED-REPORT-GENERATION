import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Function to read and analyze data from a CSV file
def analyze_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    # Example analysis: Summarize numeric data
    summary = {}
    for key in data[0]:  # Assuming the first row has headers
        try:
            values = [float(row[key]) for row in data if row[key].replace('.', '', 1).isdigit()]
            summary[key] = {
                "count": len(values),
                "sum": sum(values),
                "average": sum(values) / len(values) if values else 0,
                "max": max(values) if values else None,
                "min": min(values) if values else None
            }
        except ValueError:
            pass  # Ignore non-numeric data
    return summary

# Function to create a PDF report
def generate_pdf_report(summary, output_path):
    pdf = canvas.Canvas(output_path, pagesize=letter)
    pdf.setTitle("Automated Report")

    # Set up title
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, 750, "Automated Data Analysis Report")

    # Write summary data
    pdf.setFont("Helvetica", 12)
    y_position = 720
    for column, stats in summary.items():
        pdf.drawString(50, y_position, f"Column: {column}")
        y_position -= 20
        for key, value in stats.items():
            pdf.drawString(70, y_position, f"{key.capitalize()}: {value}")
            y_position -= 20
        y_position -= 10  # Extra space between columns

    pdf.save()

# Main function
def main():
    input_file = "data.csv"  # Replace with your data file
    output_file = "report.pdf"

    summary = analyze_data(input_file)
    generate_pdf_report(summary, output_file)

    print(f"Report generated successfully: {output_file}")

if __name__ == "__main__":
    main()
