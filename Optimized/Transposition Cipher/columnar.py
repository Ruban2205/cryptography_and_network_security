def encrypt(message, key):
    # Remove any spaces from the message
    message = message.replace(" ", "")
    
    # Calculate the number of rows required
    rows = len(message) // len(key)
    if len(message) % len(key) != 0:
        rows += 1
    
    # Add padding to the message if necessary
    padding = len(key) - len(message) % len(key)
    message += "X" * padding
    
    # Create the matrix
    matrix = []
    for i in range(rows):
        row = []
        for j in range(len(key)):
            if i * len(key) + j < len(message):
                row.append(message[i * len(key) + j])
            else:
                row.append("X")
        matrix.append(row)
    
    # Sort the key and get the column order
    sorted_key = sorted(key)
    column_order = [key.index(x) for x in sorted_key]
    
    # Build the ciphertext
    ciphertext = ""
    for i in range(len(key)):
        for j in range(rows):
            ciphertext += matrix[j][column_order.index(i)]
    
    return ciphertext

def decrypt(ciphertext, key):
    # Calculate the number of rows required
    rows = len(ciphertext) // len(key)
    
    # Create the matrix
    matrix = []
    for i in range(rows):
        row = []
        for j in range(len(key)):
            row.append("")
        matrix.append(row)
    
    # Sort the key and get the column order
    sorted_key = sorted(key)
    column_order = [key.index(x) for x in sorted_key]
    
    # Fill in the matrix
    index = 0
    for i in range(len(key)):
        for j in range(rows):
            matrix[j][column_order[i]] = ciphertext[index]
            index += 1
    
    # Build the plaintext
    plaintext = ""
    for i in range(rows):
        for j in range(len(key)):
            plaintext += matrix[i][j]
    
    # Remove any padding from the plaintext
    plaintext = plaintext.replace("X", "")
    
    return plaintext

if __name__ == "__main__":
    message = input("Enter message: ")
    key = input("Enter key: ")
    
    ciphertext = encrypt(message, key)
    
    print(f"Ciphertext: {ciphertext}")
    print(f"Decrypted plaintext: {decrypt(ciphertext, key)}")