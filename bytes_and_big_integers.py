# Link: https://cryptohack.org/courses/intro/enc4/
from Crypto.Util.number import *
# Objective: We'd like to encrypt a string messenger, but RSA and other crypto algos only work on
# numbers.
# Thus: Ordinal bytes -> Hex -> Concat

# base10?
input = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
# bytes_conversion = long_to_bytes(input)
