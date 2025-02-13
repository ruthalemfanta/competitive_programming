#convert to binary 
#compare 


def findComplement(num):
    binary_num = format(num, 'b')
    digits = list(str(binary_num))

    for i in range(len(digits)):
        if digits[i] == '1':
            digits[i] = '0'
        else:
            digits[i] = '1'
    digits = ''.join(digits)
    return int(digits, 2)

num = 5
print(findComplement(num))
