known_integer = 13
known_string = "label"
# xor each character of "label" with the integer 13
result = "".join(chr(ord(c) ^ known_integer) for c in known_string)
print(result)