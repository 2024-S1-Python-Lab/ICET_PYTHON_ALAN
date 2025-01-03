def longestWord(word):
   max_length = len(word[0])
   
   for item in word:
      length = len(item)
      if length > max_length:
          max_length = length
   return max_length
words= input("Enter a list of words separated by spaces: ")
word = words.split()
result = longestWord(word)
print(f"The length of the longest word is: {result}")
