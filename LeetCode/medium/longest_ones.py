def longestOnes(nums, k):
        window = 0
        max_size = 0 
        zeros = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1

            while zeros > k:
                if nums[window] == 0:  
                    zeros -= 1
                window += 1 
            curr_window = i - window + 1
            max_size = max(curr_window, max_size)

        return max_size