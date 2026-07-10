# text = "1E (hex) files are added"
# words = text.split()
# print(words)

# words = ['1E', '(hex)', 'files', 'are', 'added']
# result = " ".join(words)
# print(result)

from transformations import convert_hex, convert_bin

# text1 = "1E (hex) files were added"
# result = convert_hex(text1)
# print(result)

# text2 =  "It has been 10 (bin) years" 
# result = convert_bin(text2)
# print(result)

text1 = "1E (hex) files were added"
print(convert_hex(text1))

text2 = "It has been 10 (bin) years"
print(convert_bin(text2))

