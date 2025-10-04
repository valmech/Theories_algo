def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0
    
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            assignments += 3 
    
    print("Відсортований масив (вибором):", arr)
    print("Загальна кількість порівнянь:", comparisons)
    print("Загальна кількість присвоєнь:", assignments)
arr1 = [54, 65, 7, 33, 86, 29, 11, 91, 12]
selection_sort(arr1)
