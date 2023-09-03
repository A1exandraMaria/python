nums = [1,4,2,5,24,134,23,2356,20,43,53,152,86]
l_c = [x for x in nums if x%2==0]
print(l_c)

filtering = filter(lambda x: x%2==0,nums)
print(list(filtering))

mapped = map(lambda x: x if x % 2 == 0 else None, nums)
print(list(mapped))