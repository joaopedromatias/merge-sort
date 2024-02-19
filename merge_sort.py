def merge_sort(array):
    if (len(array) > 1):
        index_to_divide = len(array) // 2
        left = array[:index_to_divide]
        right = array[index_to_divide:]

        merge_sort(left)
        merge_sort(right)

        left_elements_index_to_look_for = 0
        right_elements_index_to_look_for = 0 
        original_arr_modification_index = 0

        while (left_elements_index_to_look_for < len(left) and right_elements_index_to_look_for < len(right)):
            left_value = left[left_elements_index_to_look_for]
            right_value = right[right_elements_index_to_look_for]

            if left_value < right_value:
                array[original_arr_modification_index] = left_value
                left_elements_index_to_look_for += 1
            else:
                array[original_arr_modification_index] = right_value
                right_elements_index_to_look_for += 1
            original_arr_modification_index += 1
        
        while (left_elements_index_to_look_for < len(left)):
            array[original_arr_modification_index] = left[left_elements_index_to_look_for]
            left_elements_index_to_look_for += 1
            original_arr_modification_index += 1
        
        while (right_elements_index_to_look_for < len(right)):
            array[original_arr_modification_index] = right[right_elements_index_to_look_for]
            right_elements_index_to_look_for += 1
            original_arr_modification_index += 1
    return array

arr = [100, -5, 14, -98, 167, 8, 4, 2, 51, 86, 57, 3, 1, -200]
print(merge_sort(arr))
