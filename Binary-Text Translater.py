import time

def string_to_binary(input_string):
    return ''.join(format(ord(i), '08b') for i in input_string)

def binary_to_string(input_binary):
    binary_values = [input_binary[i:i+8] for i in range(0, len(input_binary), 8)]
    return ''.join(chr(int(binary, 2)) for binary in binary_values)

while True:
    # Get user input
    user_input = input("Enter a string to convert to binary, or binary to convert to a string (or 'n' to quit): ")

    if user_input.lower() == 'n':
        exit()

    if set(user_input) == {'0', '1'}:
        print("Input is binary. Converting to string...")
        print("String: ", binary_to_string(user_input))
        time.sleep(60)
    else:
        print("Input is a string. Converting to binary...")
        print("Binary: ", string_to_binary(user_input))
        time.sleep(60)

print("Goodbye!")
