# import re

# def convert_case(text, mode):
#     text = normalize_tags(text)
#     words = text.split()
#     result_words = []

#     tag_pattern = r'^\(' + mode + r'(,(\d+))?\)$'

#     for word in words:
#         match = re.match(tag_pattern, word)
#         if match:
#             count_str = match.group(2)
#             if count_str:
#                 count = int(count_str)
#             else:
#                 count = 1

#             start = len(result_words) - count
#             for k in range(start, len(result_words)):
#                 result_words[k] = apply_mode(result_words[k], mode)
#         else:
#             result_words.append(word)

#     return " ".join(result_words)

# # def normalize_tags(text):
# #     pattern = r'\(\s*(hex|bin|up|low|cap)\s*(,\s*\d+\s*)?\)'

# #     def replacer(match):
# #         tag_name = match.group(1)
# #         count_part = match.group(2)
# #         if count_part:
# #             count_part = count_part.replace(" ", "")
# #             return f"({tag_name}{count_part})"
# #         else:
# #             return f"({tag_name})"

# #     return re.sub(pattern, replacer, text)

# def convert_hex(text):
#     words = text.split()
#     result_words =[]

#     for i in range(len(words)):
#         if words[i] == "(hex)":
#             result_words.pop()
#             hex_value = words[i-1]
#             decimal_value = int(hex_value, 16)
#             result_words.append(str(decimal_value))
#         else:
#             result_words.append(words[i])

#     return " ".join(result_words)

# def convert_bin(text):
#     words = text.split()
#     result_words =[]

#     for i in range(len(words)):
#         if words[i] == "(bin)":
#             result_words.pop()
#             bin_value = words[i-1]
#             decimal_value = int(bin_value, 2)
#             result_words.append(str(decimal_value))
#         else:
#             result_words.append(words[i])

#     return " ".join(result_words)

# def apply_mode(word, mode):
#     if mode == "up":
#         return word.upper()
#     elif mode == "low":
#         return word.lower()
#     elif mode == "cap":
#         return word.capitalize()
    
# def convert_case(text, mode):
#     tag = f"({mode})"
#     words = text.split()
#     result_words = []

#     for i in range(len(words)):
#         if words[i] == tag:
#             last_word = result_words.pop()
#             new_word = apply_mode(last_word, mode)
#             result_words.append(new_word)
#         else:

#             result_words.append(words[i])
    
#     return " ".join(result_words)

# # def normalize_tags(text):
# #     pattern = r'\(\s*(hex|bin|up|low|cap)\s*(,\s*\d+\s*)?\)'

# #     def replacer(match):
# #         # print("FULL MATCH:", match.group(0))
# #         # print("GROUP 1 (tag):", match.group(1))
# #         # print("GROUP 2 (count):", match.group(2))
# #         tag_name = match.group(1)
# #         count_part = match.group(2)
# #         if count_part:
# #             count_part = count_part.replace(" ","")
# #             return f"({tag_name}{count_part})"
# #         else:
# #             return f"({tag_name})"
# #     return re.sub(pattern, replacer, text)

# # def convert_case(text, mode):
# #     text = normalize_tags(text)
# #     words = text.split()
# #     result_words = []

# #     tag_pattern = r'^\(' + mode + r'(,(\d+))?\)$'

# #     for word in words:
# #         match = re.match(tag_pattern, word)
# #         if match:
# #             count_str = match.group(2)
# #             if count_str:
# #                 count = int(count_str)
# #             else:
# #                 count = 1

# #             start = len(result_words) - count
# #             for k in range(start, len(result_words)):
# #                 result_words[k] = apply_mode(result_words[k], mode)
# #         else:
# #             result_words.append(word)

# #     return " ".join(result_words)

import re


def normalize_tags(text):
    pattern = r'\(\s*(hex|bin|up|low|cap)\s*(,\s*\d+\s*)?\)'

    def replacer(match):
        tag_name = match.group(1)
        count_part = match.group(2)
        if count_part:
            count_part = count_part.replace(" ", "")
            return f"({tag_name}{count_part})"
        else:
            return f"({tag_name})"

    return re.sub(pattern, replacer, text)


def convert_base(text, tag, base):
    words = text.split()
    result_words = []

    for i in range(len(words)):
        if words[i] == tag:
            result_words.pop()
            value = words[i - 1]
            decimal_value = int(value, base)
            result_words.append(str(decimal_value))
        else:
            result_words.append(words[i])

    return " ".join(result_words)


def convert_hex(text):
    return convert_base(text, "(hex)", 16)


def convert_bin(text):
    return convert_base(text, "(bin)", 2)


def apply_mode(word, mode):
    if mode == "up":
        return word.upper()
    elif mode == "low":
        return word.lower()
    elif mode == "cap":
        return word.capitalize()


def convert_case(text, mode):
    text = normalize_tags(text)
    words = text.split()
    result_words = []

    tag_pattern = r'^\(' + mode + r'(,(\d+))?\)$'

    for word in words:
        match = re.match(tag_pattern, word)
        if match:
            count_str = match.group(2)
            if count_str:
                count = int(count_str)
            else:
                count = 1

            start = len(result_words) - count
            for k in range(start, len(result_words)):
                result_words[k] = apply_mode(result_words[k], mode)
        else:
            result_words.append(word)

    return " ".join(result_words)

def fix_punctuation(text):
    text = re.sub(r'\s+([.,!?:;])', r'\1', text)
    text = re.sub(r'([.,!?:;]+)\s*', r'\1 ', text)
    text = text.strip()
    return text

def fix_quotes(text):
    text = re.sub(r"'\s*([^']*?)\s*'", r"'\1'", text)
    return text

def fix_a_an(text):
    words = text.split()
    result_words = []

    for i in range(len(words)):
        word = words[i]
        stripped = word.rstrip(".,!?:;")

        if stripped in ("a", "A") and i + 1 < len(words):
            next_word = words[i + 1].lstrip("'").lower()
            if next_word and next_word[0] in "aeiouh":
                if stripped == "A":
                    word = word.replace("A", "An", 1)
                else:
                    word = word.replace("a", "an", 1)

        result_words.append(word)

    return " ".join(result_words)

def process_text(text):
    text = convert_hex(text)
    text = convert_bin(text)
    text = convert_case(text, "up")
    text = convert_case(text, "low")
    text = convert_case(text, "cap")
    text = fix_a_an(text)
    text = fix_punctuation(text)
    text = fix_quotes(text)
    return text