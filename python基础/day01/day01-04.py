"""
正整数的反转 12345-54321
"""
num = int(input('num= '))
reversed = 0
while num > 0:
    reversed = reversed*10 + num % 10
    num //= 10
print(reversed)

