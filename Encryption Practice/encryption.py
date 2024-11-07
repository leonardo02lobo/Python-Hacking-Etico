import base64

def encrypt_pass(password):
    encoded_bytes = base64.b64encode(password.encode())
    return encoded_bytes.decode()  # Devuelve la cadena codificada

def decode_pass(encoded_password):
    decode_bytes = base64.b64decode(encoded_password)
    decode_data = decode_bytes.decode()
    print(f"Decoded password: {decode_data}")


# Ejemplo de uso
password = input("What is your password?: ")
encoded_password = encrypt_pass(password)
print(f"Encoded password: {encoded_password}")

# Ahora intenta decodificar
encode_string = input("Enter the base64 string to decode: ")
decode_pass(encode_string)