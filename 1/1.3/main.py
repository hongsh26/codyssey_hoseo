try:    
    with open('./1.3/Mars_Base_Inventory_List.csv', 'r') as file:
        datas = file.readlines()
        data_list = [line.strip().split(",") for line in datas if "," in line]
        data_list = [(Substanse, Weight, Specific_Gravity, Strength, Flammability) for Substanse, Weight, Specific_Gravity, Strength, Flammability in data_list]

        data_list.sort(reverse=True, key=lambda x: x[4])
        print("data_list의 타입:",type(data_list))
        csv_list = [data_list[0]]

        for i in data_list:
            print(i)
            try:
                if(float(i[4]) >= 0.7):
                    csv_list.append(i)
            except:
                continue
        print()
        print("인화성 지수 0.7 이상 리스트")
        with open('./1.3/classified_List.csv', 'a') as csv:
            for i in csv_list:
                contents = i[0]+','+i[1]+','+i[2]+','+i[3]+','+i[4]+'\n'
                print(i)
                csv.write(contents)



except FileNotFoundError as e:
    print("오류 발생:",e)
