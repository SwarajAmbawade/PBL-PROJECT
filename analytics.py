import csv
import pandas as pd
import matplotlib.pyplot as plt




df = pd.read_csv('diabetes.csv')
row = df.columns
col = df.iloc[5,1:6]
new_var = pd.Series(col.values.flatten())



# s = pd.Series(col)
fig, ax = plt.subplots()
new_var.plot.bar(color=['red','black','yellow','green','brown'])
plt.xlabel('Attributes') 
plt.ylabel("Intensity")
plt.xticks(range(len(new_var.index)), row[1:6], rotation=45)
plt.tight_layout()
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
    row_index = 12  # Index of the row
    col_index = 0  # Index of the column
    
    # Read the element from the CSV file
    element = read_element_from_csv("data.csv", row_index, col_index)
    
    # Write HTML content to file 
    with open("analytics.html", "w") as f:
        f.write("<html><head><title>Data Display</title><style>h1{color:blue;position:relative;left:35rem;font-size:2rem;}p{font-size:1.5rem;margin-left:10rem;margin-top:6rem;border:2px solid black;background-color:white;width:20rem;padding-left:2rem;align-items:center;border-radius:1rem}body{background-color:#BBE2EC;overflow-x:hidden}img{margin-left:10rem;margin-top:3rem}div{position:fixed;height:5rem;width:100%;background-color:#BBE2EC}a{font-size:1.2rem;text-decoration:none;color:white;background-color:black;padding:0.35rem;margin-top:1rem;border-radius:1rem;}</style></head><body>")
        f.write("<div class=margin-left:5rem><a href=./index.html>Home</a></div>")
        f.write("<h1>Analytics</h1>")
        f.write("<p>Name: {}</p>".format(element))
        f.write("<img src=""my_plot.png></img>")
        f.write("<h2 style=position:relative;left:15rem;top:2rem;>Keep Your Medical Data Secured with Medikeeps</h2>")
        f.write("</body></html>")

