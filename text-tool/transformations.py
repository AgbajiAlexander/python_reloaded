import re

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

def apply_mode(word, mode):
    if mode == "up":
        return word.upper()
    elif mode == "low":
        return word.lower()
    elif mode == "cap":
        return word.capitalize()
    
def convert_case(text, mode):
    tag = f"({mode})"
    words = text.split()
    result_words = []

    for i in range(len(words)):
        if words[i] == tag:
            last_word = result_words.pop()
            new_word = apply_mode(last_word, mode)
            result_words.append(new_word)
        else:

            result_words.append(words[i])
    
    return " ".join(result_words)

def normalize_tags(text):
    pattern = r'\(\s*(hex|bin|up|low|cap)\s*(,\s*\d+\s*)?\)'

    def replacer(match):
        print("FULL MATCH:", match.group(0))
        print("GROUP 1 (tag):", match.group(1))
        print("GROUP 2 (count):", match.group(2))
        tag_name = match.group(1)
        count_part = match.group(2)
        if count_part:
            count_part = count_part.replace(" ","")
            return f"({tag_name}{count_part})"
        else:
            return f"({tag_name})"
    return re.sub(pattern, replacer, text)
