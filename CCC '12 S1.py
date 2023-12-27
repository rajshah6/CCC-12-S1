n = int(input())

N = n
sum = 0
for i in range(2, N+1):
    sum += (n-i)*(n-i-1)

print(sum//2)
