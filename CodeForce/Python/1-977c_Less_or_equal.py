n, k = map(int, input().split())
nums = sorted(list(map(int, input().split())))

if k == 0:
    print(nums[0] - 1 if nums[0] > 1 else -1)
elif k == n:
    print(nums[-1] if nums[-1] <= 10**9 else -1)
else:
    print(nums[k - 1] if nums[k - 1] != nums[k] else -1)

