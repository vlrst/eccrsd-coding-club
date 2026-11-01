nums = list(map(int, input().split()))




leftovers = nums[0] % nums[1]

if leftovers == 0:
    print(f"{nums[0]//nums[1]} 0 NO leftovers")
else:

    print(f"{nums[0]//nums[1]} {nums[0]%nums[1]} Leftovers ")
