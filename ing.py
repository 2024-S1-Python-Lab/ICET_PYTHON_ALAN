def modifyStr(str1):
    if str1.endswith("ing"):
        return str1 + "ly"
    else:
        return str1 + "ing"
str1 = input("Enter a string: ")
result = modifyStr(str1)
print(result)
