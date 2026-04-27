import base64

hex_str = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
# Decode into bytes:
byte_rep = bytes.fromhex(hex_str)
# Encode into base64:
base64_rep = base64.b64encode(byte_rep)
print(base64_rep)