import csv

print('Hello mars')

try:
    f = open('/Users/hongseunghyuk/PycharmProjects/1/42hoseo/1/1.1/mission_computer_main.log', 'r')
    print("정방향")
    for i in f:
        print(i, end="")
except FileNotFoundError:
    print("file is not exist")