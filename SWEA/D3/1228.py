for test in range(1, 11):
    num = int(input())
    password = list(map(int, input().split()))
    com_cnt = int(input())
    commands = list(map(str, input().split()))



    for i in range(len(commands)):
        if commands[i] =='I':
            pass_h = password[:int(commands[i + 1]):]
            pass_t = commands[i + 3 : i + 3 + int(commands[i + 2]):] + password[int(commands[i + 1])::]
            password = pass_h + pass_t
    print(f'#{test}', end = ' ')
    for i in range(10):
        print(password[i], end = ' ')
    print()