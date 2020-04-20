def from_base2_to_base10():
    print('*****Convert a number in base 2 to base 10*****')
    num_in_base2 = int(input('Number in base 2: '))
    num_string = str(num_in_base2)
    num_length = len(num_string)
    num_in_base10 = 0

    for i in range(0, num_length):
        if int((num_string[i])) < 2:
            temp = int((num_string[i])) * (2 ** (int(num_length - 1 - i)))
            num_in_base10 += temp
        else:
            print('Wrong input!')
            return

    print('Number in base 10: %d' % num_in_base10)


# from_base2_to_base10()


def from_base10_to_base2():
    print('*****Convert a number in base 10 to base 2*****')
    num_in_base10 = int(input('Number in base 10: '))
    num_in_base2_string = ''

    while num_in_base10 != 0:
        digit = num_in_base10 % 2
        num_in_base10 = num_in_base10 // 2
        num_in_base2_string = str(digit) + num_in_base2_string

    print('Number in base 2: %d' % int(num_in_base2_string))


# from_base10_to_base2()


def from_baseN_to_base10():
    print('*****Convert a number in base 2-10 to base 10*****')
    baseN = int(input('Base system (from 2 to 10): '))
    num_in_baseN = input('Number in base %d: ' % baseN)
    num_string = str(num_in_baseN)
    num_length = len(num_string)
    num_in_base10 = 0

    for i in range(0, num_length):
        if int((num_string[i])) < baseN:
            temp = int((num_string[i])) * (baseN ** (int(num_length - 1 - i)))
            num_in_base10 += temp
        else:
            print('Wrong input!')
            return

    print('Number in base 10: %d' % num_in_base10)


# from_baseN_to_base10()


def from_baseN_to_base10_arg(baseN, num_in_baseN):
    num_string = str(num_in_baseN)
    num_length = len(num_string)
    num_in_base10 = 0

    for i in range(0, num_length):
        if int((num_string[i])) < baseN and baseN <= 10:
            temp = int((num_string[i])) * (baseN ** (int(num_length - 1 - i)))
            num_in_base10 += temp
        else:
            print('Wrong input!')
            return

    return num_in_base10


# from_baseN_to_base10_arg(7, 123456)


def from_base10_to_baseN():
    print('*****Convert a number in base 10 to base 2-10*****')
    baseN = int(input('Base system (from 2 to 10): '))
    num_in_base10 = int(input('Number in base 10: '))
    num_in_baseN_string = ''

    while num_in_base10 != 0:
        digit = num_in_base10 % baseN
        num_in_base10 = num_in_base10 // baseN
        num_in_baseN_string = str(digit) + num_in_baseN_string

    print('Number in base %d: %d' % (baseN, int(num_in_baseN_string)))


# from_base10_to_baseN()


def from_base10_to_baseN_arg(baseN, num_in_base10):
    num_in_baseN_string = ''

    while num_in_base10 != 0:
        digit = num_in_base10 % baseN
        num_in_base10 = num_in_base10 // baseN
        num_in_baseN_string = str(digit) + num_in_baseN_string

    return int(num_in_baseN_string)


# from_base10_to_baseN_arg(7, 22875)


def from_baseN_to_all2_10():
    print('***Convert a number in base 2-10 to numbers in base from 2-10***\n')

    base = int(input('Base of the number: '))
    if not 2 <= base <= 10:
        print('Wrong input')
        return
    else:
        pass

    num_to_convert = int(input('Number under base %d: ' % base))
    num_length = len(str(num_to_convert))
    for a in range(0, num_length):
        if int(str(num_to_convert)[a]) < base:
            num_in_base10 = from_baseN_to_base10_arg(base, num_to_convert)
        else:
            print('Wrong input')
            return

    print('')
    for i in range(2, 11):
        temp = from_base10_to_baseN_arg(int(i), num_in_base10)
        print('%d under base %d is %d' % (num_to_convert, i, temp))
    print('')


from_baseN_to_all2_10()
