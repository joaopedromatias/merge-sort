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

        for i in range(len(array)): 
            if left_elements_index_to_look_for < len(left) and right_elements_index_to_look_for < len(right): 
                if(left[left_elements_index_to_look_for] < right[right_elements_index_to_look_for]):
                    array[i] = left[left_elements_index_to_look_for]
                    left_elements_index_to_look_for += 1
                else: 
                    array[i] = right[right_elements_index_to_look_for]
                    right_elements_index_to_look_for += 1
                original_arr_modification_index += 1
            elif left_elements_index_to_look_for == len(left):
                array[i] = right[right_elements_index_to_look_for]
                right_elements_index_to_look_for += 1
            else: 
                array[i] = left[left_elements_index_to_look_for]
                left_elements_index_to_look_for += 1
        
        return array
