def rail_fence_encrypt(plain_text, num_rails):
    # Create a list of empty strings for each rail
    rails = ['' for _ in range(num_rails)]

    # Distribute the characters of the plain text to the rails in a round-robin fashion
    for i, char in enumerate(plain_text):
        rails[i % num_rails] += char

    # Concatenate the rails to form the cipher text
    cipher_text = ''.join(rails)
    return cipher_text

def rail_fence_decrypt(cipher_text, num_rails):
    # Calculate the length of each rail
    rail_lengths = [len(cipher_text) // num_rails + (1 if i < len(cipher_text) % num_rails else 0) for i in range(num_rails)]

    # Distribute the characters of the cipher text to the rails
    rails = []
    start = 0
    for length in rail_lengths:
        rails.append(cipher_text[start:start+length])
        start += length

    # Collect the characters from the rails in a round-robin fashion to form the plain text
    plain_text = ''
    for i in range(len(cipher_text)):
        rail = i % num_rails
        plain_text += rails[rail][0]
        rails[rail] = rails[rail][1:]

    return plain_text

if __name__ == "__main__":
    plain_text = input("Enter plain text: ")
    num_rails = int(input("Enter number of rails: "))

    cipher_text = rail_fence_encrypt(plain_text, num_rails)

    print(f"Cipher text: {cipher_text}")
    print(f"Decrypted plain text: {rail_fence_decrypt(cipher_text, num_rails)}")