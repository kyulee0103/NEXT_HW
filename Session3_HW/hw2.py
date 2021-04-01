num = 0
average_list = []

while num != -1:
    num = int(input("양의 정수를 입력해주세요: "))
    if num == -1:
        break
    average_list.append(num)


def find_average():
    total = 0
    num_len = len(average_list)
    for i in range(num_len):
        total += average_list[i]
    average = total / num_len
    return average


print(find_average())