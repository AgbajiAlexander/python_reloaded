def convert_hex(text):
    words = text.split()
    result_words =[]

    for i in range(len(words)):
        if words[i] == "(hex)":
            result_words.pop()
            hex_value = words[i-1]
            decimal_value = int(hex_value, 16)
            result_words.append(str(decimal_value))
        else:
            result_words.append(words[i])

    return " ".join(result_words)

def convert_bin(text):
    words = text.split()
    result_words =[]

    for i in range(len(words)):
        if words[i] == "(bin)":
            result_words.pop()
            bin_value = words[i-1]
            decimal_value = int(bin_value, 2)
            result_words.append(str(decimal_value))
        else:
            result_words.append(words[i])

    return " ".join(result_words)