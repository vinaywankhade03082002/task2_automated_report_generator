# task2_automated_report_generator

Company Name : CodTech IT Solutions Pvt. Ltd.  
Name : Vinay Mahendra Wankhade  
Intern ID : CT12UCB  
Domain : Python Programming  
Duration : 8 Weeks  
Mentor : Neela Santosh

# Description
# Automated Report Generator Script

## Overview

The Student Report Generator is a Python-based tool designed to automate the creation of student performance reports. It reads student information from a CSV file, analyzes the data, and generates a clean, professional PDF report using the fpdf2 library. The report includes both a summary of overall performance metrics and a detailed table listing individual student results.

This project is ideal for educators, academic administrators, and developers who want a lightweight, customizable solution for managing and presenting student performance data. It helps eliminate the manual effort involved in report creation and ensures consistent formatting every time.

## Features

* **CSV File Integration :** Reads structured data from a standard .csv file containing   student names, subjects, scores, grades, and pass/fail status.

* **Formatted PDF Report**
  * Generates a polished PDF report that includes:
  * A summary section of key statistics
  * A tabular view of all student records
  * Page headers and footers with automatic page numbers

* **Automated Data Analysis :**
   Calculates useful metrics like:

   * Total number of students
   * Average score
   * Count of passing and failing students

* **Formatted PDF Output:** The script generates a clean and readable PDF report, making it easy to share or print for meetings and presentations.

* **Customizable:** You can easily modify the script to handle different types of data, change the layout of the report, or include additional calculations.

## Requirements

To use this script, you will need:

- **Python 3.x**: The script is written in Python, so make sure you have Python 3.x installed.
- **Libraries**:
  - "fpdf": A lightweight library for creating PDF documents in Python.
  - "pandas": A powerful data manipulation library that simplifies reading CSV files and analyzing the data.

You can install the required libraries using "pip". Run the following command in your terminal or command prompt to install them:

```bash
pip install fpdf pandas
```

## Project structured

Here is the file structure for the project:

```
Automated_Report_Generation/
│
├── data.csv              # The sample CSV file containing Students data
├── report_generator.py   # The Python script for reading, analyzing, and generating the report
```

### data.csv

This is the CSV file that contains the sales data. It should have the following columns:

- **Name**: The name of the student.
- **Subjects**: The subject the student was assessed in.
- **Scores**: The numerical score obtained.
- **Grade**: The grade assigned based on performance.
- **Result**: The final result (e.g., Pass or Fail)

Example: data.csv

```csv
Name,Subject,Score,Grade,Result
Alice,Math,85,B,Pass
Bob,Science,90,A,Pass
Charlie,English,78,C,Pass
David,Math,92,A,Pass
Eva,Science,67,D,Pass
Frank,English,49,F,Fail
```


## How to Use the Script

1. **Prepare your CSV File**:
   - Create or obtain a CSV file similar to "data.csv" with the students data.
   - Make sure it has at least the following columns: Name, Subjects, score, grade, result.

2. **Place the CSV File**:
   - Place your CSV file in the same directory as the "report_generator.py" script.
   - Ensure the file is named correctly in the script ("data.csv"), or update the script to point to your file.

3. **Run the Script**:
   - Open a terminal or command prompt and navigate to the directory where the script is located.
   - Run the following command to execute the script: python report_generator.py

4. **View the Generated PDF**:
   - After running the script, you will see a new PDF file, "student_report.pdf", in the same directory.
   - Open the "student_report.pdf" file to view the generated report.   

## Example of the Generated Report

The generated PDF report will look something like this:

**Student Performance Report**

**Summary:**

- **Total Students** : 6
- **Average Score**  : 76.83
- **Passed**         : 5
- **Failed**       : 1

Student Data:
--------------------------------------------------
| Name    | Subject | Score | Grade | Result     |
|---------|---------|-------|-------|------------|
| Alice   | Math    | 85    | B     | Pass       |
| Bob     | Science | 90    | A     | Pass       |
| Charlie | English | 78    | C     | Pass       |
| David   | Math    | 92    | A     | Pass       |
| Eva     | Science | 67    | D     | Pass       |
| Frank   | English | 49    | F     | Fail       |


Grand Total Students: 6

## Customizing the Report

While the default layout is simple and functional, you can easily customize the script to suit your needs:

- **Change the Formatting**: Modify the font style, size, or color in the "FPDF" library section to customize the report's appearance.
- **Add More Calculations**: If you need to analyze additional metrics, such as average sales, maximum revenue, or other statistics, you can extend the script to include those calculations.
- **Modify the CSV Structure**: If your data contains more columns, you can adapt the script to read and display those columns in the table.

## Troubleshooting

If you encounter any issues while running the script, here are some common problems and solutions:

- **Missing Libraries**: If you see an error related to missing libraries, make sure to install them using "pip install fpdf pandas".
- **File Not Found**: Ensure the CSV file is in the same directory as the script, or update the file path in the script to match your CSV file's location.
- **Permissions Issues**: If you're unable to write the output PDF, ensure the script has permission to write files in the current directory.

## Conclusion

The Student Report Generator is a simple yet powerful tool for automating the creation of academic reports. By reading structured data from a CSV file and producing a formatted PDF, it streamlines the process of data analysis and presentation. This project demonstrates how Python, combined with libraries like `fpdf`, can be used to build practical, real-world automation solutions. It’s easily customizable for different data formats and use cases, making it a versatile addition to any educator's or developer's toolkit.

# Output
