binStr = input()
dec = int(0)

binStr = '0b' + binStr

# 2진수 -> 10진수
dec = int(binStr, 2)

# 10진수 -> 8진수
print(int(oct(dec)[2:]))