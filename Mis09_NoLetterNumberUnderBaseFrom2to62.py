import datetime

map_list = [0, '0', 1, '1', 2, '2', 3, '3', 4, '4', 5, '5', 6, '6', 7, '7', 8, '8', 9, '9', 10, 'A', 11, 'B', 12, 'C', 13, 'D', 14, 'E', 15, 'F', 16, 'G', 17, 'H', 18, 'I', 19, 'J', 20, 'K', 21, 'L', 22, 'M', 23, 'N', 24, 'O', 25, 'P', 26, 'Q', 27, 'R', 28, 'S', 29, 'T', 30, 'U', 31, 'V', 32, 'W', 33, 'X', 34, 'Y', 35, 'Z', 36, 'a', 37, 'b', 38, 'c', 39, 'd', 40, 'e', 41, 'f', 42, 'g', 43, 'h', 44, 'i', 45, 'j', 46, 'k', 47, 'l', 48, 'm', 49, 'n', 50, 'o', 51, 'p', 52, 'q', 53, 'r', 54, 's', 55, 't', 56, 'u', 57, 'v', 58, 'w', 59, 'x', 60, 'y', 61, 'z']


def key_map_exchange(before_exchange):
    if str(type(before_exchange)) == "<class 'int'>":
        for i in range(0, 124):
            if before_exchange == map_list[i]:
                after_exchange = map_list[i + 1]
                return str(after_exchange)
    elif str(type(before_exchange)) == "<class 'str'>":
        for m in range(0, 124):
            if before_exchange == map_list[m]:
                after_exchange = map_list[m - 1]
                return str(after_exchange)


def from_base10_to_baseN_2to62_arg(baseN, num_in_base10):
    num_in_baseN_string = ''

    while num_in_base10 != 0:
        digit = key_map_exchange(num_in_base10 % baseN)
        num_in_base10 = num_in_base10 // baseN
        num_in_baseN_string = digit + num_in_baseN_string

    return num_in_baseN_string  # str


def check_no_letter_number():
    # for i in range(0, 100000):  # 0-9 13s 11to62
    # for i in range(100000, 1000000):  # none 2m5s 11to62
    # for i in range(1000000, 10000000):  # none 21m15s 11to62
    # for i in range(10000000, 100000000):  # none 3h36m1s 11to62
    # for i in range(100000000, 110000000):  # none 24min 15s 11to36
    for i in range(0, 1000000):
        checker = 1
        for n in range(58, 63):
            num_str = from_base10_to_baseN_2to62_arg(n, i)
            for m in range(0, len(num_str)):
                if num_str[m] in '0123456789':
                    checker *= 1
                else:
                    checker *= 0
                    break
            if checker == 0:
                break

        if checker == 1:
            print('Bingo: %d' % i)
        if i % 500000 == 0:
            print('Now at %d' % i, end="\r")


start_time = datetime.datetime.now()

check_no_letter_number()

end_time = datetime.datetime.now()

runtime = str(end_time - start_time)
print(runtime[0] + ' hour ' + runtime[2:4] + ' min ' + runtime[5:] + ' sec')
