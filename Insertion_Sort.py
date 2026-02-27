def insertion_sort(arr):
    comparisons = 0
    assignments = 0

    for j in range(1, len(arr)):
        key = arr[j]
        assignments += 1 
        i = j - 1
        while i >= 0:
            comparisons += 1
            if arr[i] > key:
                arr[i + 1] = arr[i]
                assignments += 1
                i -= 1
            else:
                break
        arr[i + 1] = key
        assignments += 1

    print("Відсортований масив (вставками):", arr)
    print("Загальна кількість порівнянь:", comparisons)
    print("Загальна кількість присвоєнь:", assignments)

arr2 = [54, 65, 7, 33, 86, 29, 11, 91, 12]
insertion_sort(arr2)
