# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    l1 = len(arrA)
    l2 = len(arrB)
    l = 0
    r = 0
    merged_arr = []

    while (l < l1) and (r < l2):
        if arrA[l] < arrB[r]:
            merged_arr.append(arrA[l])
            l += 1
        else:
            merged_arr.append(arrB[r])
            r += 1
    while l < l1:
            merged_arr.append(arrA[l])
            l += 1
    while r < l2:
            merged_arr.append(arrB[r])
            r += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:  # base case
        return arr

    # divide arr in half and merge sort recursively
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

# # STRETCH: implement the recursive logic for merge sort in a way that doesn't
# # utilize any extra memory
# # In other words, your implementation should not allocate any additional lists
# # or data structures; it can only re-use the memory it was given as input


# def merge_in_place(arr, start, mid, end):
#     # Your code here
#     pass


# def merge_sort_in_place(arr, l, r):
#     # Your code here
#     pass
