import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--decision", help="To Choose between the Logical XOR Operations", type=int)
args = parser.parse_args()
decision = args.decision

# Usage 
# python logical_xor.py -d 1
# Change the value of decision to choose between the Logical XOR Operations


def is_odd_or_even(number):
    if number ^ 1 == number + 1:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")


def swap_variables(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


def xor_with_127(string, key=127):
    result = ""
    for char in string:
        result += chr(ord(char) ^ key)
    return result


def one_time_pad_encrypt(plaintext, key):
    ciphertext = ""
    # Repeat the key to match the length of plaintext 
    key = (key * (len(plaintext) // len(key) + 1))[:len(plaintext)]
    for i in range(len(plaintext)):
        ciphertext += chr(ord(plaintext[i]) ^ ord(key[i]))
    return ciphertext


def frequency_analysis(ciphertext):
    freq = {}
    for char in ciphertext:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq


if __name__ == "__main__":
    if decision == 1:
        number = int(input("Enter the number: "))
        is_odd_or_even(number)

    elif decision == 2:
        a = int(input("Enter the value of a: "))
        b = int(input("Enter the value of b: "))
        print(f"Before Swapping: a = {a} and b = {b}")
        a, b = swap_variables(a, b)
        print(f"After Swapping: a = {a} and b = {b}")

    elif decision == 3:
        string = input("Enter the string to be XOR'ed with key: ")
        key = int(input("Enter the key: "))
        print(f"XORing {string} with {key} gives {xor_with_127(string, key=key)}")

    elif decision == 4:
        plaintext = input("Enter the plaintext: ")
        key = input("Enter the key: ")
        print(f"Encrypted Text: {one_time_pad_encrypt(plaintext, key)}")

    elif decision == 5:
        ciphertext = input("Enter the ciphertext: ")
        print(frequency_analysis(ciphertext))

    else:
        print("Invalid Choice")

