def merge_sort(unsorted_array):
    if (len(unsorted_array) > 1):
        index_to_divide = len(unsorted_array) // 2
        left = unsorted_array[:index_to_divide]
        right = unsorted_array[index_to_divide:]

        merge_sort(left)
        merge_sort(right)

        left_elements_index_to_look_for = 0
        right_elements_index_to_look_for = 0 
        original_arr_modification_index = 0

        for i in range(len(unsorted_array)): 
            if left_elements_index_to_look_for < len(left) and right_elements_index_to_look_for < len(right): 
                if(left[left_elements_index_to_look_for] < right[right_elements_index_to_look_for]):
                    unsorted_array[i] = left[left_elements_index_to_look_for]
                    left_elements_index_to_look_for += 1
                else: 
                    unsorted_array[i] = right[right_elements_index_to_look_for]
                    right_elements_index_to_look_for += 1
                original_arr_modification_index += 1
            elif left_elements_index_to_look_for == len(left):
                unsorted_array[i] = right[right_elements_index_to_look_for]
                right_elements_index_to_look_for += 1
            else: 
                unsorted_array[i] = left[left_elements_index_to_look_for]
                left_elements_index_to_look_for += 1
        
        return unsorted_array


print(merge_sort([101,100,3,1,1,8,2,5,9,9,10,100,7,-9,39]))
# [1,3,8,2,5,9,10,7]