"""
Encodes an XML file to base64 and saves it to a text file.

Setup:
1. Create a folder and place this Python script inside.
2. Create a file named 'decoded.xml' in the same folder containing the XML data.
"""

import base64
from urllib.parse import quote

try:
    # Open the XML file for reading, ensuring UTF-8 encoding is used.
    with open("decoded.xml", "r", encoding="utf-8") as file:
        xml_string = file.read()  # Read the XML data into a string

except FileNotFoundError:
    print("Error: 'decoded.xml' not found in the current directory.")
    exit()  # Exit the script if the file is not found

# Encode the XML data to base64.
try:
    xml_bytes = xml_string.encode('utf-8') # Encode the XML string to UTF-8 bytes.
    base64_bytes = base64.b64encode(xml_bytes) # Base64 encode the UTF-8 bytes.
    base64_string = base64_bytes.decode('utf-8') # Decode the base64 bytes to a string.
    encoded_string = quote(base64_string) # URL-encode the base64 string.

except Exception as e:
    print(f"Error encoding to base64: {e}")  # Handle potential encoding errors

# Write the URL-encoded base64 string to a text file.
try:
    # Open the output file for writing, using UTF-8 encoding.
    with open("encoded.txt", "w", encoding="utf-8") as outfile:
        outfile.write(encoded_string)  # Write the encoded string to the file
        print("Base64 encoded data written to 'encoded.txt'")  # Confirmation message
        # print(decoded_string)  # Optional print in consol 

except Exception as e:
    print(f"Error writing to 'encoded.txt': {e}")  # Handle file writing errors