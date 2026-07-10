# text = "1E (hex) files are added"
# words = text.split()
# print(words)

# words = ['1E', '(hex)', 'files', 'are', 'added']
# result = " ".join(words)
# print(result)

from transformations import convert_hex, convert_bin, convert_case, normalize_tags

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

# word  = "HELLO"
# print(word.lower())

# word2 = "hello"
# print(word2.upper())

# word3 = "hello alexander"
# print(word3.capitalize())

text3 = "python (up)"
print(convert_case(text3, "up"))

text4 = "python (cap)"
print(convert_case(text4, "cap"))

print(normalize_tags("This is so exciting (up, 2)"))
print(normalize_tags("go (up)"))
