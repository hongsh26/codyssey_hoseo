import numpy as np

base_path = "./문제5/"
files = [
    "mars_base_main_parts-001.csv",
    "mars_base_main_parts-002.csv",
    "mars_base_main_parts-003.csv"
]

arr_list = []
for i, file in enumerate(files):
    path = base_path + file
    try:
        data = np.loadtxt(path, delimiter=',', dtype=object, encoding='utf-8-sig')
        print(f"arr{i + 1} type : {type(data)}")
        arr_list.append(data)
    except Exception as e:
        print(f"Error occurred {file}: {e}")

parts = np.vstack([arr_list[0]] + [arr[1:] for arr in arr_list[1:]])

data = parts[1:]
unique_parts = np.unique(data[:, 0])
result = [['parts', 'avg_strength']]

for part in unique_parts:
    mask = data[:, 0] == part
    matched_rows = data[mask]

    # strength 컬럼을 float형으로 변환
    strengths = matched_rows[:, 1].astype(float)

    # 평균 계산
    avg_strength = np.mean(strengths)

    # 결과에 추가 (문자열로 변환하여 저장)
    result.append([part, str(round(avg_strength, 2))])

result_array = np.array(result)

#헤더 제외
data_only = result_array[1:]
avg_values = data_only[:, 1].astype(float)

mask = avg_values < 50
filtered_data = data_only[mask]

final_result = np.vstack([result_array[0], filtered_data])

np.savetxt("parts_to_work_on.csv", final_result, fmt="%s", delimiter=",")
print("CSV 저장 완료")

try:
    data = np.loadtxt('./parts_to_work_on.csv', delimiter=',', dtype=object, encoding='utf-8-sig')
    print(data)
    print(data.shape)
    print()
    transpose = data.T
    print(transpose)
    print(transpose.shape)
except Exception as e:
    print(f"Error occurred './parts_to_work_on.csv': {e}")

