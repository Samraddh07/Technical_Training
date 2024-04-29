num = list(map(int, input('').split(' ')))
n = int(input(''))

def getMax(sub, nums):
    if nums == []:
        return None
    if max(nums) <= sub:
        return max(nums)
    else:
        nums.remove(max(nums))
        return getMax(sub, nums)
    
max_val = 0
sorted_nums = sorted(num)[::-1]
for i in range(len(sorted_nums)):
    digits = []
    count = 0
    nums = sorted_nums[i:]
    while count < n :
        sub = n - count
        if nums == [] or (len(nums) == 1 and sub < nums[0]):
            break

        max_n = getMax(sub, nums)
        if max_n is None:
            break
        digits.append(max_n)
        count += max_n
        
    max_val = sum(digits) if sum(digits) > max_val else max_val

print(max_val)