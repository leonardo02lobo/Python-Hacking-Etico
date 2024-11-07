import base64

def encrypt_pass(password):
    encoded_bytes = base64.b64encode(password.encode())
    print(encoded_bytes)

def decode_pass(password):
    decode_bytes = base64.b64decode(password)
    decode_data = decode_bytes.decode()
    print(f"decoded password {decode_data}")

# password = input("What is your password?: ")

# encrypt_pass(password)

encode_string = input("enter the base64 string: ")

decode_pass(encode_string)
