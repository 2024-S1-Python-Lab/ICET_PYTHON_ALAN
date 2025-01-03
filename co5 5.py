import csv

data_dict = {
    "Name": ["John", "Jane", "Alice", "Bob"],
    "Age": [28, 34, 25, 30],
    "City": ["New York", "Los Angeles", "Chicago", "Miami"]
}
filename = "output.csv" 
with open(filename, mode='w', newline='') as file: 
    writer = csv.DictWriter(file, fieldnames=data_dict.keys())
    writer.writeheader() 
    for i in range(len(data_dict["Name"])): 
        writer.writerow({key: data_dict[key][i] for key in data_dict})
print(f"Dictionary written to {filename}.")
with open(filename, mode='r') as file: 
    csvreader = csv.reader(file)
    for row in csvreader: 
        print(row)
