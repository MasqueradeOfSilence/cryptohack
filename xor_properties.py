from pwn import *
key1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
key2_xor_with_key1 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
key2_xor_with_key3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
result_of_xor_flag_with_keys = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")
# Operator has a .xor method, but decode from hex to bytes first
# TODO: This isn't correct, fix arithmetic
result1 = xor(result_of_xor_flag_with_keys, key2_xor_with_key3)
result2 = xor(result1, key2_xor_with_key1)
result3 = xor(result2, key1)
print(result3)