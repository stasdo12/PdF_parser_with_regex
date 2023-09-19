from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors


workers = [
    {"Name": "Ivan", "Date": "2023-02-19", "Salary": "50000"},
    {"Name": "Stanislav", "Date": "2023-04-19", "Salary": "23000"},
    {"Name": "Nikola", "Date": "2023-03-19", "Salary": "14000"},
    {"Name": "Svetlana", "Date": "2023-01-19", "Salary": "2000"},
    {"Name": "Ciril", "Date": "2023-05-19", "Salary": "60000"},
    {"Name": "Bob", "Date": "2023-07-19", "Salary": "130000"},
    {"Name": "Steve", "Date": "2023-01-19", "Salary": "55000"},
    {"Name": "Den", "Date": "2023-04-19", "Salary": "30000"},
    {"Name": "Daria", "Date": "2023-05-19", "Salary": "50000"},
    {"Name": "Evgen", "Date": "2023-01-19", "Salary": "50000"},
    {"Name": "Lola", "Date": "2023-05-19", "Salary": "50000"},
    {"Name": "Kim", "Date": "2023-06-19", "Salary": "50000"},
    {"Name": "Carl", "Date": "2023-13-19", "Salary": "50000"},
    {"Name": "Susana", "Date": "2023-01-19", "Salary": "50000"},
    {"Name": "Irina", "Date": "2023-03-19", "Salary": "50000"},
    {"Name": "Abu", "Date": "2023-09-18", "Salary": "50000"},
    {"Name": "Kola", "Date": "2023-09-18", "Salary": "50000"},
    {"Name": "Luiza", "Date": "2023-09-18", "Salary": "50000"},
    {"Name": "Kris", "Date": "2023-09-11", "Salary": "50000"},
    {"Name": "David", "Date": "2023-01-13", "Salary": "50000"},
    {"Name": "Mark", "Date": "2023-09-14", "Salary": "50000"},
    {"Name": "Lion", "Date": "2023-03-15", "Salary": "50000"},
    {"Name": "Shon", "Date": "2023-09-11", "Salary": "50000"},
    {"Name": "Sergey", "Date": "2023-05-13", "Salary": "50000"},
    {"Name": "Yta", "Date": "2023-06-25", "Salary": "50000"},
    {"Name": "Biker", "Date": "2023-01-31", "Salary": "50000"}

]


headers = list(workers[0].keys())


data = [[worker[header] for header in headers] for worker in workers]

pdf = SimpleDocTemplate('workers_table.pdf', pagesize=letter)


table = Table([headers] + data, colWidths=[100, 100, 100])


style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
])

table.setStyle(style)


pdf.build([table])