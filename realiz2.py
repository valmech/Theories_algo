def merge_sort_recursive(arr):
    comparisons = 0
    assignments = 0
    recursive_calls = 0
    if len(arr) <= 1:
        return arr, comparisons, assignments, recursive_calls
    mid = len(arr) // 2
    assignments += 1
    recursive_calls += 2
    left_half, c1, a1, r1 = merge_sort_recursive(arr[:mid])
    right_half, c2, a2, r2 = merge_sort_recursive(arr[mid:])
    comparisons += c1 + c2
    assignments += a1 + a2
    recursive_calls += r1 + r2
    merged_arr, c_merge, a_merge = merge(left_half, right_half)
    comparisons += c_merge
    assignments += a_merge
    return merged_arr, comparisons, assignments, recursive_calls

def merge(left, right):
    merged_arr = []
    comparisons = 0
    assignments = 0
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] <= right[j]:
            merged_arr.append(left[i])
            i += 1
        else:
            merged_arr.append(right[j])
            j += 1
        assignments += 1
    while i < len(left):
        merged_arr.append(left[i])
        i += 1
        assignments += 1
    while j < len(right):
        merged_arr.append(right[j])
        j += 1
        assignments += 1
    return merged_arr, comparisons, assignments

my_list = [54, 65, 7, 33, 86, 29, 11, 91, 12]
print("Оригінальний список:", my_list)
sorted_list, total_comparisons, total_assignments, total_recursive_calls = merge_sort_recursive(my_list)
print("Відсортований список:", sorted_list)
print(f"Загальна кількість порівнянь: {total_comparisons}")
print(f"Загальна кількість присвоювань: {total_assignments}")
print(f"Загальна кількість рекурсивних викликів: {total_recursive_calls}")
