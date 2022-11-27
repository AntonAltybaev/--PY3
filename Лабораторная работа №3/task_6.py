array = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

last_max_element_index, last_max_element = -1, float('-inf')
for index, element in enumerate(array):
    if element >= last_max_element:
        last_max_element = element
        last_max_element_index = index
array[last_max_element_index], array[len(array) - 1] = array[len(array) - 1], array[last_max_element_index]

print(array)
