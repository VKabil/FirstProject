nums = [0,1,4,6,7,10]
diff = 3
count =0
for i in range(len(nums)):
    for j in range(len(nums)):
        for k in range(len(nums)):
            if(nums[j] - nums[i] == diff) and (nums[k] - nums[j] == diff):
                count +=1 

print(count)