def productExceptSelf(nums):
    prefix_product = 1
    suffix_product = 1

    result = [0] * len(nums)

    for i in range(len(nums)):
        result[i] = prefix_product
        prefix_product *= nums[i]

    print(result)

    for j in range(len(nums)-1, -1, -1):
        result[j] *= suffix_product
        suffix_product *= nums[j]

    return result

print(productExceptSelf([1, 2, 3, 4]))
print(productExceptSelf([-1, 1, 0, -3, 3]))
