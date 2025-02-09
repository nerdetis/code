"""
Decodes a base64 encoded text file, UTF-8 encodes it, and exports it as XML.

Setup:
1. Create a folder and place this Python script inside.
2. Create a file named 'encoded.txt' in the same folder and place the base64 encoded text within.
"""

import base64
from urllib.parse import unquote

# Attempt to open and read the encoded file.
try:
    with open("encoded.txt", "r") as file:  
        base64_string = unquote(file.read().strip())  # Remove leading/trailing whitespace.
except FileNotFoundError:
    print("Error: 'encoded.txt' not found in the current directory.")
    exit()

# Handle potential padding issues in the base64 string.
try:
    missing_padding = len(base64_string) % 4
    if missing_padding != 0:  
        base64_string += '=' * (4 - missing_padding)
        print("Info: Padding added to base64 string.")
    else:
        print("Info: No padding needed.")
except Exception as e:
    print(f"Error checking/adding padding: {e}")  

# Decode the base64 string and then decoding using UTF-8 encoding.
try:
    decoded_bytes = base64.b64decode(base64_string)
    decoded_string = decoded_bytes.decode('utf-8', errors='replace') # Handle decoding errors by replacing invalid characters.

except Exception as e:
    print(f"Error decoding base64: {e}")

# Write the decoded string to an XML file.
try:
    with open("decoded.xml", "w", encoding="utf-8") as outfile:  # Explicitly use UTF-8 encoding for writing.
        outfile.write(decoded_string)
        print("Base64 decoded data written to 'decoded.xml'") 
        # print(decoded_string)  # Optional print in consol 

except Exception as e:
    print(f"Error writing to 'decoded.xml': {e}")