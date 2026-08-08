def productExceptSelf_unrevised(nums):
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


def productExceptSelf(nums):
    products = [1] * len(nums)
    prefix_prod = 1

    for i in range(len(nums)):
        products[i] = prefix_prod
        prefix_prod *= nums[i]

    posfix_prod = 1

    for j in range(len(nums) - 1, -1, -1):
        products[j] *= posfix_prod
        posfix_prod *= nums[j]


    return products

print(productExceptSelf([1, 2, 3, 4]))
print(productExceptSelf([-1, 1, 0, -3, 3]))
