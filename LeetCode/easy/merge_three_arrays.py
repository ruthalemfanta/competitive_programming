def mergeThreeArrays(num1, num2, num3):
    i = len(nums1) - len(nums2) - len(nums3) - 1
    j = len(num2) - 1
    k = len(num3) - 1
    total = len(num1) - 1

    while i >= 0 and j >= 0 and k >= 0:
        if num1[i] >= num2[j] and num1[i] >= num3[k]:
            num1[total] = num1[i]
            i -= 1
        elif num2[j] >= num1[i] and num2[j] >= num3[k]:
            num1[total] = num2[j]
            j -= 1
        else:
            num1[total] = num3[k]
            k -= 1

        total -= 1
    return nums1


nums1 = [1,4,7,0,0,0,0,0,0]
nums2 = [2,5,8]
nums3 = [3,6,9]

print(mergeThreeArrays(nums1, nums2, nums3))