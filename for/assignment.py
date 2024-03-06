# bt8
# Define the input string
input_string = "Today is Sunday and we don't need to wake up at 6 am"

# Split the string into words
words = input_string.split()

# Initialize counters
word_count = len(words)
number_count = 0
number_positions = []

# Iterate through the words
for idx, word in enumerate(words):
    # Check if the word contains a number
    if any(char.isdigit() for char in word):
        number_count += 1
        number_positions.append(idx)

# Print the number of words and whether numbers are present
print("Number of words in the string:", word_count)
if number_count > 0:
    print("Numbers are present in the string.")
    print("Positions of numbers in the string:", number_positions)
else:
    print("Không có số trong chuỗi.")
