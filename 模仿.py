N = int(input())
nums = list(map(int, input().split()))
count = 0

for i in range(len(nums) - 2 , -1, -1):
    if nums[i] < nums[i+1]:
        nums[i] = nums[i+1]
        count += 1
print(sum(nums), count)

