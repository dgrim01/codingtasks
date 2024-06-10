def alternate_word_uppercase(input_string):
    words = input_string.split()  # Split the input string into words
    result = ""
    for i in range(len(words)):
        if i % 2 == 0:  # Check if the index is even
            result += words[i].upper()
        else:
            result += words[i]
        result += " "  # Add a space between words
    return result.strip()  # Remove trailing space

# Example usage:
input_string = "this is a test sentence to demonstrate the functionality"
output_string = alternate_word_uppercase(input_string)
print(output_string)  # Output: "THIS is A test SENTENCE to DEMONSTRATE the FUNCTIONALITY"


print("Example 4: ")

fact2 = "          The$first$electronic$computer$ENIAC$weighed$more$than$27$tons.          "
fact2 = fact2.replace("$", "WOW!")
print(fact2)
fact2 = fact2.strip()
print(fact2)
fact2 = fact2.split("WOW!")
print(fact2)