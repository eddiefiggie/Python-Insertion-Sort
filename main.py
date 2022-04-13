# Insertion Sort time complexity is O(n^2)


def insertion_sort(base_array):
    for k in range(1, len(base_array)):
        cur = base_array[k]
        j = k
        while j > 0 and base_array[j - 1] > cur:
            base_array[j] = base_array[j - 1]
            j -= 1
        base_array[j] = cur
    return base_array


if __name__ == '__main__':
    sample_array = [9, 8, 7, 6, 12, 55, 150, 2000]

    print("This is the base array which is unsorted:")
    for i in sample_array:
        print(i)

    sorted_array = insertion_sort(sample_array)

    print("This is the sorted array:")
    for i in sorted_array:
        print(i)
