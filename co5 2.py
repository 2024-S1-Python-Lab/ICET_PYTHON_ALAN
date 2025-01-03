filename = input ("enter file name")
with open(filename, 'r') as file1:
    lines = file1.readlines()
    lines = [line.strip() for line in lines] 
    print("Lines from the file:", lines)
