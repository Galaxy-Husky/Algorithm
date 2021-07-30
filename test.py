def getLeastNumbers(arr, k):
    def quicksort(arr, left, right):
        print(left, right)
        i, j = left, right
        while i < j:
            while i < j and arr[j] >= arr[left]:
                j -= 1
            while i < j and arr[i] <= arr[left]:
                i += 1
            arr[i], arr[j] = arr[j], arr[i]
        arr[i], arr[left] = arr[left], arr[i]

        if k < i:
            return quicksort(arr, left, i - 1)
        elif k > i:
            return quicksort(arr, i + 1, right)
        else:
            print(arr)
            return arr[:k]

    return quicksort(arr, 0, len(arr) - 1)


arr = [0,0,1,3,4,5,0,7,6,7]
k = 9

print(getLeastNumbers(arr, k))