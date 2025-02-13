def merge(num1, m, num2, n):
    num1_pointer = m-1
    num2_pointer = n-2
    total_pointer = m+n-1

    while num1_pointer > 0 and num2_pointer > 0:
        if num1[num1_pointer] > num2[num2_pointer]:
            num1[total_pointer] = num1[num1_pointer]
            num1_pointer -= 1
        else:
            num1[total_pointer] = num2[num2_pointer]
            num2_pointer -= 1

        total_pointer -= 1

    while num2_pointer > 0 :
        num1[total_pointer] = num2[num2_pointer]
        num2_pointer -= 1
        total_pointer -= 1
