material = ''
#지름은 10m
diameter = 1000 #cm
thickness = 0
area = 0
weight = 0

#무게에 0.38을 곱한값이 화성 무게
def spehere_area(material='유리', thickness=1):
    if(material == '유리'):
        weight = 2.4*0.38
    elif(material == '알루미늄'):
        weight = 2.7*0.38
    elif(material == '탄소강'):
        weight = 7.85*0.38
    else:
        print('올바른 값을 입력하지 않았기에 유리로 진행됩니다.')
        material = '유리'
        weight = 2.4*0.38
    #겉넓이 => 3*3.14*r^2
    area = 3.141 * (diameter**2) * 3
    print('재질:',material)
    print('지름:',diameter)
    print('두께:',thickness)
    print('면적:',round(area,3))
    print('무게:',round(weight,3))

material = input('재질을 입력해주세요.')
thickness = int(input('두께를 입력해주세요.'))

spehere_area(material, thickness)