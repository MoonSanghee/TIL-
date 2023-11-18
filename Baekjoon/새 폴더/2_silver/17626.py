n = int(input())
# n을 받아줍니다.
dp = [0, 1]
# 0과 1을 만드는데 필요한 제곱수를 리스트에 담아줍니다.
for i in range(2, n + 1):
    # 인덱스 n의 값까지 넣어줘야하므로 n + 1까지 실행하여줍니다.
    num = i
    # i를 만드는데 1이 i개 만큼 있는것이 가장 많은 제곱수가 필요하므로 num을 i로 설정해줍니다.
    for j in range(1, i):
        if j ** 2 > i:
            break
        num = min(num, dp[i - j ** 2])
        # i의 제곱근보다 작은 양의 정수 j중
        # i - j의 제곱을 만드는데 가장 적은 제곱수가 필요한 경우를 확인해줍니다.
    dp.append(num + 1)
    # 리스트에 num에 저장된 값을 1 더하여 넣어줍니다.

print(dp[-1])
# 리스트의 마지막에 있는 값을 출력해줍니다.