import sys
from transformations import process_text

if len(sys.argv) != 3:
    print("Usage: python3 main.py <input_file> <output_file>")
    sys.exit(1)

input_path = sys.argv[1]
output_path = sys.argv[2]

with open(input_path, "r") as file:
    text = file.read()

result = process_text(text)

with open(output_path, "w") as file:
    file.write(result)

print("Done!")

# import sys

# if len(sys.argv) != 3:
#     print("Usage: python3 main.py <input_file> <output_file>")
#     sys.exit(1)

# input_path = sys.argv[1]
# output_path = sys.argv[2]

# #file = open(input_path, "r")
# #text = file.read()
# #file.close()

# with open(input_path, "r") as file:
#     text = file.read()

# with open(output_path, "w") as file:
#     file.write(text)

# print("Done!")

# # print("input file:", input_path)
# # print("output file:", output_path)