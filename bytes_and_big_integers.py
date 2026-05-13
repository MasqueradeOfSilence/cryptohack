# Link: https://cryptohack.org/courses/intro/enc4/
from Crypto.Util.number import long_to_bytes
# Objective: We'd like to encrypt a string messenger, but RSA and other crypto algos only work on
# numbers.

# base10 long
input = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
# 1. Convert this into hex
# 2. Convert hex into bytes
# 3. Convert bytes into string

bytes_conversion = long_to_bytes(input)
print(bytes_conversion)
