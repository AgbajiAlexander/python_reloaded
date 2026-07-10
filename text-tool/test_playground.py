# text = "1E (hex) files are added"
# words = text.split()
# print(words)

# words = ['1E', '(hex)', 'files', 'are', 'added']
# result = " ".join(words)
# print(result)

from transformations import convert_hex

text = "1E (hex) files were added"
result = convert_hex(text)
print(result)
