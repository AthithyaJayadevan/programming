def insertion_sort(arr):
    for i in range(len(arr)):
        k = arr[i]
        j=i-1
        while j>=0 and k < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = k
    return arr


def selection_sort(arr):
    for i in range(len(arr)):
        min_ind = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[min_ind], arr[i] = arr[i], arr[min_ind]
    return arr


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr


def sort_string(strings):

    for i in range(len(strings)):
        min_ind = i
        for j in range(i+1, len(strings), 1):
            if strings[j] < strings[min_ind]:
                min_ind = j

        strings[min_ind], strings[i] = strings[i], strings[min_ind]
    return strings


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist)//2
        left = alist[:mid]
        right = alist[mid:]

        mergeSort(left)
        mergeSort(right)

        i=j=k=0

        while i < len(left) and j<len(right):
            if left[i] < right[j]:
                alist[k] =left[i]
                k+=1
                i+=1
            else:
                alist[k] = right[j]
                k+=1
                j+=1

        while i<len(left):
            alist[k] = left[i]
            k+=1
            i+=1
        while j<len(right):
            alist[k] = right[j]
            k+=1
            j+=1

    return alist


def quicksort_split(arr, low, high):
    i=low-1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <pivot:
            i+=1
            arr[i],arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i+1

def quicksort(arr, low, high):
    if low < high:

        pivo = quicksort_split(arr, low, high)

        quicksort(arr, low, pivo-1)
        quicksort(arr, pivo+1, high)


def heapify(arr, n, i):

    largest = i
    l=2*i+1
    r=2*i+2

    if l <n and arr[i] < arr[l]:
        largest=l

    if r <n and arr[largest] < arr[r]:
        largest=r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)

def heapsort(arr):
    n=len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n ,i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)




Arr=[45,67,2,34,1,256,78,5]
print('Bubble sort')
result = bubble_sort(Arr)
print(result)
Arr=[7,4,5,2,7,2,4,65,7,8,4,2]
print('Selection sort')
result = bubble_sort(Arr)
print(result)
Arr=[23,12,2,54,87,4,3,9]
print('Insertion sort')
result = insertion_sort(Arr)
print(result)

strings = ['hello', 'maxsdjvbjw', 'wrfg', 'iuefhv']
new_strings = sort_string(strings)
print(new_strings)