n = int(input())
# 새의 수를 입력받습니다.
count = 0
# 노래를 부른 수를 저장할 변수를 설정해줍니다.
k = 1
# 부를 숫자를 저장할 변수를 설정해줍니다.
while True:
    if k > n:
        k = 1
        # 부를 노래가 남은 새보다 크다면 1로 초기화해줍니다.
    n -= k
    # 부른 숫자만큼 남은 새를 줄여줍니다.
    k += 1
    count += 1
    # 부를 숫자와 부른 횟수를 1씩 늘려줍니다.
    if n <= 0:
        break
    # n이 0이하면 노래를 멈춥니다.
print(count)
# 노래를 부른 횟수를 출력해줍니다.