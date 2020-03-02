import binascii
"""package does not work well
strings???
"""

print('*****\n')

b1 = binascii.a2b_uu('a')
b2 = binascii.unhexlify('aa')
b3 = bin(235689)
b4 = binascii.a2b_qp('033na')
b5 = binascii.a2b_qp("zaq1xsw2cde3")


print(b1, b2, b3, b4, b5)
print("\n")
