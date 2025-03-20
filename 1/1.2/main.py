with open("/Users/hongseunghyuk/PycharmProjects/1/42hoseo/1/1.2/mission_computer_main.log", "r", encoding="utf-8") as f:
    datas = f.readlines()

log_list = [line.strip().split(",") for line in datas if "," in line]
log_list = [(timestamp, level, content) for timestamp, level, content in log_list]

# print(log_list[2])
# print(log_list[1])
log_list.sort(reverse=True, key=lambda x: x[0])
# print()

for i in log_list:
    print(i)
print()
log_dict = {str(i): {"timestamp": log_list[i][0], "log": log_list[i][1]} for i in range(len(log_list))}

with open("1.2/mission_computer_main.json", "w", encoding="utf-8") as json_file:
    json_file.write("[\n")
    for i,data in enumerate(log_list):
        if(i == 0):
            continue
        timestamp = data[0]
        event = data[1]
        message = data[2]
        dic = {'timestamp':str(timestamp), 'event':str(event), 'message':str(message)}
        json_file.write("\n{" + "\n\t"+f'"timestamp":"{dic['timestamp']}"'+','+"\n\t"+f'"event":"{dic['event']}"'+','+'\n\t'+f'"message":"{dic['message']}"'+'\n}')
        if(i+1<len(log_list)):
            json_file.write(',')
    json_file.write("]")