# Q. 양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. 
# 양의 정수number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지

# Input
# 123

# A.
a = int(input())
b = 0
for i in range(1,a):
    if (a // 10**i) != 0:
        b = i + 1
    elif (a // 10) == 0:
        b = 1
print(b)
