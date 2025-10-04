## Коди на Python до видів сортування

### Selection Sort

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

<img width="573" height="131" alt="image" src="https://github.com/user-attachments/assets/14ff0208-3eb8-450d-b808-c0253a2daa57" /> 

Рис1.1 - скриншот виконання коду

### Insertion Sort 

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

<img width="573" height="131" alt="image" src="https://github.com/user-attachments/assets/56f6afe8-6c22-4bfb-b569-cfac4f6cb953" />

Рис. 1.2 - скриншот виконання коду 
