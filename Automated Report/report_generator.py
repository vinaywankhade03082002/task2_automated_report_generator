import csv
from statistics import mean
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 14)
        self.cell(0, 10, "Student Performance Report", ln=True, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def student_table(self, data, col_widths):
        self.set_font("Arial", 'B', 12)
        headers = ["Name", "Subject", "Score", "Grade", "Result"]
        for i, header in enumerate(headers):
            self.cell(col_widths[i], 10, header, 1, 0, "C")
        self.ln()

        self.set_font("Arial", '', 12)
        for row in data:
            self.cell(col_widths[0], 10, row["Name"], 1)
            self.cell(col_widths[1], 10, row["Subject"], 1)
            self.cell(col_widths[2], 10, str(row["Score"]), 1, 0, "C")
            self.cell(col_widths[3], 10, row["Grade"], 1, 0, "C")
            self.cell(col_widths[4], 10, row["Result"], 1, 0, "C")
            self.ln()

def read_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def analyze_data(data):
    scores = [int(row["Score"]) for row in data]
    return {
        "Total Students": len(scores),
        "Average Score": mean(scores),
        "Passed": sum(1 for row in data if row["Result"] == "Pass"),
        "Failed": sum(1 for row in data if row["Result"] == "Fail")
    }

def generate_pdf(data, analysis, output_file):
    pdf = PDF()
    pdf.add_page()

    # Summary section
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Summary", ln=True)
    pdf.set_font("Arial", '', 12)
    for key, value in analysis.items():
        pdf.cell(0, 8, f"{key}: {value}", ln=True)
    pdf.ln(5)

    # Table section
    col_widths = [40, 30, 25, 25, 25]
    pdf.student_table(data, col_widths)

    pdf.output(output_file)
    print(f"PDF report generated: {output_file}")

if __name__ == "__main__":
    data_file = "data.csv"
    output_pdf = "student_report.pdf"

    student_data = read_csv(data_file)
    report_analysis = analyze_data(student_data)
    generate_pdf(student_data, report_analysis, output_pdf)
