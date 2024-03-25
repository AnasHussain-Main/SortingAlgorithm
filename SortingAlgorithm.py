import os
import time

def beep():
    # Play sound on macOS
    os.system('afplay /System/Library/Sounds/Ping.aiff')

def merge(arr, left, mid, right):
    # Temporary arrays to hold the left and right halves
    n1 = mid - left + 1
    n2 = right - mid
    L = [0] * n1
    R = [0] * n2

    for i in range(0, n1):
        L[i] = arr[left + i]
    for j in range(0, n2):
        R[j] = arr[mid + 1 + j]

    i = j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
            beep()  # Play sound for each merge operation
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
        beep()  # Play sound for each merge operation

def merge_sort(arr, left, right):
    if left < right:
        mid = left + (right - left) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        merge(arr, left, mid, right)

        print(f"Current state: {arr[left:right+1]}")
        time.sleep(0.5)

def main():
    arr = [11, 1, 30, 2, 51, 6, 29, 7, 67, 15, 118, 4, 89, 23]
    print("Original array:", arr)
    merge_sort(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)

if __name__ == "__main__":
    main()