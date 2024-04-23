import csv
import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv('diabetes.csv')

row = df.columns
col = df.iloc[[2],[1,2,3,4,5]]
new_var = pd.Series(col.all)


# s = pd.Series(col)
fig, ax = plt.subplots()
new_var.plot.bar()
fig.savefig('my_plot.png')

print(new_var)
def read_element_from_csv(filename, row_index, col_index):
    with open("data.csv", 'r', newline='') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i == row_index:
                return row[col_index]
    return None

if __name__ == "__main__":
    # Choose the element's position (row and column index)
    row_index = 102  # Index of the row
    col_index = 0  # Index of the column
    
    # Read the element from the CSV file
    element = read_element_from_csv("data.csv", row_index, col_index)
    
    # Write HTML content to file 
    with open("analytics.html", "w") as f:
        f.write("<html><head><title>Data Display</title><style>h1{color:blue;position:relative;left:35rem;font-size:2rem;}p{font-size:2rem}body{background-color:#BBE2EC;overflow-x:hidden}</style></head><body>")
        f.write("<h1>Analytics</h1>")
        f.write("<p>Name: {}</p>".format(element))
        f.write("<img src=""my_plot.png></img>")
        f.write("</body></html>")


