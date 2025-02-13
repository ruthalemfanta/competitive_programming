def twoArrays(nums1, nums2):
    answer = [[], []]

    for i in nums1:
        if  i not in answer[0]:
            if i not in nums2:
                answer[0].append(i)

        
    for i in nums2:
        if i not in answer[1]:
            if i not in nums1:
                answer[1].append(i)

    return answer

print(twoArrays([1,2,3,3], [1,1,2,2]))