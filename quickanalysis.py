import time, random
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)

def generate_random_array(size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(size)]

sizes = [1, 10, 20, 100, 1000, 10000]
for size in sizes:
    array = generate_random_array(size, 1, 10000)
    # print(f"Unsorted Array ({size} values): {array}")
    print(f"sizes = {size}")
    start_time = time.time()
    quicksort(array, 0, len(array)-1)
    end_time = time.time()
    # print(f"Sorted Array ({size} values): {array}")
    print("Running Time:", end_time - start_time, "Seconds")
    print()
