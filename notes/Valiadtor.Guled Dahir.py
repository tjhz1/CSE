test_num = "3845023879443020"
print(test_num)


def remove_num(string):
    return string[:15]


def reverse_it(string):
    return string[::-1]


def validate(num: str):
    cut_nums = remove_num(test_num[:15])
    # print(cut_nums)
    reversed_nums = reverse_it(cut_nums)
    # print(reversed_nums)
    list_nums = list(reversed_nums)
    print(list_nums)
    for index in range(len(list_nums)):
        list_nums[index] = int(list_nums[index])
    print(list_nums)


def multiply_odd_num(num: list):
    for index in range(len(num)):
        num[index] = int(num[index])
        if index % 2 == 0:
            num[index] *= 3
            if num[index] > 9:
                num[index] -= 9

    print(validate(test_num))
    