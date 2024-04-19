import csv
import pandas as pd

# def read_data_from_csv(filename):
#     data = []
#     with open("data.csv", 'r', newline='') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             data.append(row)
#     return data

# def generate_html_table(data):
#     html_table = "<table border='1'>"
#     for row in data:
#         html_table += "<tr>"
#         for col in row:
#             html_table += "<td>{}</td>".format(col)
#         html_table += "</tr>"
#     html_table += "</table>"
#     return html_table

# if __name__ == "__main__":
#     # Read data from CSV file
#     data = read_data_from_csv("data.csv")
    
#     # Generate HTML table
#     html_table = generate_html_table(data)
#     df = pd.DataFrame("data.csv")
#     # Write HTML content to file
#     with open("analytics.html", "w") as f:
#         f.write("<html><head><title>Data Display</title></head><body>")
#         f.write("<h1>CSV Data Display</h1>")
#         f.write(df[0])
#         f.write("</body></html>")

import csv

def read_element_from_csv(filename, row_index, col_index):
    with open("data.csv", 'r', newline='') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i == row_index:
                return row[col_index]
    return None

if __name__ == "__main__":
    # Choose the element's position (row and column index)
    row_index = 2  # Index of the row
    col_index = 0  # Index of the column
    
    # Read the element from the CSV file
    element = read_element_from_csv("data.csv", row_index, col_index)
    
    # Write HTML content to file 
    with open("analytics.html", "w") as f:
        f.write("<html><head><title>Data Display</title><style>h1{color:blue;margin-left:10rem}</style></head><body>")
        f.write("<h1>Analytics</h1>")
        f.write("<p>row:{} column:{} Name:{}</p>".format(row_index, col_index, element))
        f.write("</body></html>")

