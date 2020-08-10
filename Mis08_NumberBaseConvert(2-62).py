map_list = [0, '0', 1, '1', 2, '2', 3, '3', 4, '4', 5, '5', 6, '6', 7, '7', 8, '8', 9,
            '9', 10, 'A', 11, 'B', 12, 'C', 13, 'D', 14, 'E', 15, 'F', 16, 'G', 17, 'H',
            18, 'I', 19, 'J', 20, 'K', 21, 'L', 22, 'M', 23, 'N', 24, 'O', 25, 'P', 26,
            'Q', 27, 'R', 28, 'S', 29, 'T', 30, 'U', 31, 'V', 32, 'W', 33, 'X', 34, 'Y',
            35, 'Z', 36, 'a', 37, 'b', 38, 'c', 39, 'd', 40, 'e', 41, 'f', 42, 'g', 43,
            'h', 44, 'i', 45, 'j', 46, 'k', 47, 'l', 48, 'm', 49, 'n', 50, 'o', 51, 'p',
            52, 'q', 53, 'r', 54, 's', 55, 't', 56, 'u', 57, 'v', 58, 'w', 59, 'x', 60,
            'y', 61, 'z']


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


def from_baseN_2to62_to_base10_arg(baseN, num_in_baseN):
    num_string = str(num_in_baseN)
    num_length = len(num_string)
    num_in_base10 = 0
    
    for i in range(0, num_length):
        digit = int(key_map_exchange(num_string[i]))
        temp = digit * (baseN ** (int(num_length - 1 - i)))
        num_in_base10 += temp
    
    return num_in_base10  # int


def from_base10_to_baseN_2to62_arg(baseN, num_in_base10):
    num_in_baseN_string = ''
    
    while num_in_base10 != 0:
        digit = key_map_exchange(num_in_base10 % baseN)
        num_in_base10 = num_in_base10 // baseN
        num_in_baseN_string = digit + num_in_baseN_string
    
    return num_in_baseN_string  # str


def from_baseN_to_all_2to62():
    print('***Convert a number in base 2-62 to numbers in base from all 2-62***\n')
    
    base = int(input('Base of the number, 2 to 62 : '))
    if not 2 <= int(base) <= 62:
        print('Wrong input\n')
        return
    else:
        pass
    
    avail_char_list = ''
    for s in range(0, base):
        avail_char = str(map_list[2 * s + 1]) + ' '
        avail_char_list += avail_char
    
    print('\nAvailable numbers and letters are : %s\n' % avail_char_list)
    
    num_to_convert = input('Number under base %d: ' % base)
    num_length = len(str(num_to_convert))
    for a in range(0, num_length):
        digit = int(key_map_exchange(num_to_convert[a]))
        if digit < base:
            num_in_base10 = from_baseN_2to62_to_base10_arg(
                base, num_to_convert)
        else:
            print('Wrong input\n')
            return
    
    print('')
    for i in range(2, 63):
        result = from_base10_to_baseN_2to62_arg(i, num_in_base10)
        print('%s under base %d is %s' % (num_to_convert, i, result))
    print('')


while True:
    from_baseN_to_all_2to62()
