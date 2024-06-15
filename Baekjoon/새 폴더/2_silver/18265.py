n = int(input())
# 찾을 수가 몇번째 수인지 받아줍니다.
cycle = [1, 2, 4, 7, 8, 11, 13, 14]
# 3과 5의 배수마다 moo가 오므로 15마다 3과 5의 배수 위치에 moo가 오고 나머지는 수가 옵니다.
print(((n - 1) // 8 ) * 15 + cycle[(n - 1) % 8])
# n번째 오는 수를 출력해줍니다.