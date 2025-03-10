print('Hello mars')

try:
    f = open('1/1.1/mission_computer_main.log', 'r')
    contents = f.readlines()
    print('정방향')
    for i in contents:
        print(i, end="")
    print('역방향')
    for j in contents[::-1]:
        print(j, end="")
    f.close()
except FileNotFoundError as e:
    print('file is not exist')
    f1 = open('1/42hoseo/1/1.1/error.txt', 'w')
    f1.write(str(e))
    f1.close()
    