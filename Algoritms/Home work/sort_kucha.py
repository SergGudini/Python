def heap (array, size_heap, root_index):
    #определение корня, правого и левого элемента
    largest_index = root_index
    left_index = root_index + 1
    right_index = root_index + 2
    
    if left_index < size_heap and array[left_index] > array[largest_index]:
        largest_index = left_index
    
    if right_index < size_heap and array[right_index] > array[largest_index]:
        largest_index = right_index
        
    if largest_index != root_index:
        array[root_index], array[largest_index] = array[largest_index], array[root_index]
        heap(array, size_heap, largest_index)

def sortirovka(array):  
    n = len(array)
    for i in range(n, -1, -1):
        heap(array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heap(array, i, 0)

array = [35, 12, 43, 8, 51]  
sortirovka(array)  
print(array)

