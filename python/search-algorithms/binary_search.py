def binary_search(li, target, is_sorted=False):

    if not is_sorted:
        li = sorted(li)

    left_ptr = 0
    right_ptr = len(li) - 1

    while left_ptr < right_ptr:
        mid_index = (right_ptr - left_ptr) // 2

        if li[mid_index] == target:
            return mid_index

        if target < li[mid_index]:
            right_ptr = mid_index - 1
        else:
            left_ptr = mid_index + 1
