def searchMatrix(matrix, target):

    def searchInnerRow(inner_row, target):
        # print("inner_search")
        inner_start = 0
        inner_stop = len(inner_row)

        while inner_start <= inner_stop:
            inner_mid = inner_start + (inner_stop - inner_start) // 2

            if inner_row[inner_mid] == target:
                return True

            elif inner_row[inner_mid] < target:
                inner_start = inner_mid + 1

            else:
                inner_stop = inner_mid - 1

        return False
 
    lenM = len(matrix)

    start = 0
    stop = lenM - 1

    while start <= stop:
        mid = start + (stop - start) // 2

        if target < matrix[mid][0]:
            stop = mid - 1      

        elif target > matrix[mid][-1]:
            start = mid + 1     

        else:
            return searchInnerRow(matrix[mid], target)

    return False


print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))

print(searchMatrix([[1]], 1))