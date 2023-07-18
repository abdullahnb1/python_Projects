n = int(input())
result = 0
result += n // 100
a = n % 100

result += a // 20
b = a % 20

result += b // 10
c = b % 10

result += c // 5
d = c % 5

result += d

print(result)