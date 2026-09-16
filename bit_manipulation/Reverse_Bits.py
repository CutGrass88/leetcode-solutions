def reverseBits(n):
    return int(format(n, '32b')[::-1], 2)

b = format(12, '032b')
print(f"Binary:{b}, Reversed:{b[::-1]}")

