# https://www.acmicpc.net/problem/1003
# 풀이) DP

t = int(input())
for _ in range(t):
    n = int(input())
    if n == 0:
        print('1 0')
        continue
    elif n == 1:
        print('0 1')
        continue
    
    dp0, dp1 = [0] * (n+1), [0] * (n+1)
    dp0[0], dp0[1] = 1, 0
    dp1[0], dp1[1] = 0, 1

    for i in range(2, n+1):
        dp0[i] = dp0[i-1] + dp0[i-2]
        dp1[i] = dp1[i-1] + dp1[i-2]
        
    print(dp0[-1], dp1[-1])

