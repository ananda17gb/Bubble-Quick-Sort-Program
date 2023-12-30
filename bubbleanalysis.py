import time, random
def generate_random_array(size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(size)]
def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
sizes = [1, 10, 20, 100, 1000, 10000]
for size in sizes:
    array = generate_random_array(size, 1, 10000)
    # print(f"Unsorted Array ({size} values): {array}")
    print(f"sizes = {size}")
    start_time = time.time()
    bubbleSort(array)
    end_time = time.time()
    # print(f"Sorted Array ({size} values): {array}")
    print("Running Time:", end_time - start_time, "Seconds")
    print()