# text = "1E (hex) files are added"
# words = text.split()
# print(words)

# words = ['1E', '(hex)', 'files', 'are', 'added']
# result = " ".join(words)
# print(result)

from transformations import convert_hex, convert_bin, convert_case, fix_punctuation, fix_quotes, fix_a_an

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

# text3 = "python (up)"
# print(convert_case(text3, "up"))

# text4 = "python (cap)"
# print(convert_case(text4, "cap"))

# print(normalize_tags("This is so exciting (up, 2)"))
# print(normalize_tags("go (up)"))

print(convert_case("This is so exciting (up, 2)", "up"))
print(convert_case("go (up)", "up"))

print(fix_punctuation("I was sitting over there ,and then BAMM !!"))

print(fix_quotes("I am exactly how they describe me: ' awesome '"))
print(fix_quotes("As Elton John said: ' I am the most well-known homosexual in the world '"))

print(fix_a_an("There it was. A amazing rock!"))
print(fix_a_an("I need a hero"))
print(fix_a_an("I need a book"))

print(fix_punctuation("I was thinking ... You were right"))
print(fix_punctuation("What is happening !?"))