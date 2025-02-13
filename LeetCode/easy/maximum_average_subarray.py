def maximumAverage(nums, k):
    window_sum = sum(nums[:k])
    window_av = window_sum / k
    maximum = window_av

    for i in range(len(nums) -  k):
        window_sum = window_sum -nums[i] + nums[i+k]
        window_av = window_sum / k
        maximum = max(window_av, maximum)

    return maximum

