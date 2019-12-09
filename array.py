from sys import maxsize

def subarray_sum(arr, s):
    cur_start=arr[0]
    start=0
    i=1
    n=len(arr)
    while i <= n:
        while cur_start > s and start < i-1:
            cur_start = cur_start - arr[start]
            start+=1

        if cur_start == s:
            print("Indices found " + str(start) + " "+str(i-1))
            return 1

        if i < n:
            cur_start += arr[i]
        i+=1
    print('NO subarray found !!')
    return 0

def count_triplets(arr):
    n = len(arr)
    count=0
    i=0
    processed=[]

    if n==0:
        return 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i]+arr[j] in arr:
                new_arr=[arr[i], arr[j], arr[i]+arr[j]]
                if new_arr not in processed:
                    count+=1
                    processed.append(new_arr)

    return count

def maximum_sum_of_contigous_subarray(arr):
    n=len(arr)
    max_val = -maxsize -1
    max_ending_here = 0

    for i in range(n):
        max_ending_here += arr[i]
        if max_ending_here > max_val:
            max_val = max_ending_here
        if max_ending_here <0:
            max_ending_here = 0

    return max_val


def missing_element(arr):
    n=len(arr)
    for i in range(1,n):
        if i not in arr:
            return i

    return -1


def merge_sorted_arrays(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    i=m-1

    while i>=0:
        elem = arr2[i]
        j=n-2
        rep_elem = arr1[-1]
        while j >=0:
            if arr1[j+1] > elem:
                arr1[j+1] = arr1[j]
            else:
                break
            j-=1
        arr1[j+2] = elem
        arr2[i] = rep_elem
        i-=1

    return arr1, arr2

class Minheapnode:
    def __init__(self, element, i, j):
        self.element = element
        self.i=i
        self.j=j



class Minheap:
    def __init__(self, arr, size):
        self.heap_size=size
        self.heap_arr = arr
        i=(self.heap_size-1)//2
        while i>=0:
            self.min_heapify(i)
            i-=1

    def min_heapify(self, i):
        l = 2*i +1
        r=2*i +2
        smallest=i

        if l < self.heap_size and self.heap_arr[l].element < self.heap_arr[i].element:
            smallest=l
        if r < self.heap_size and self.heap_arr[r].element < self.heap_arr[i].element:
            smallest=r

        if smallest != i:
            self.heap_arr[smallest], self.heap_arr[i] = self.heap_arr[i], self.heap_arr[smallest]
            self.min_heapify(smallest)

    def getmin(self):
        if self.heap_size <= 0:
            print("Heam Empty")
            return None
        return self.heap_arr[0]



def merge_k_sorted_arrays(arr, k):
    h_arr=[]
    res_size=0
    for i in range(len(arr)):
        node = Minheapnode(arr[i][0], i, 1)
        h_arr.append(node)
        res_size+=len(arr[i])

    min_heap = Minheap(h_arr, k)
    result=[0]*res_size

    for i in range(res_size):
        root = min_heap.getmin()
        result[i] = root.element


    min_heap = Minheap(h_arr, k)





#arr = [15, 2, 4, 8, 9, 5, 10, 23]
#sum = 32

#subarray_sum(arr, sum)

#arr2 = [1,5,3,2]
#print(count_triplets(arr2))
#a = [-1, -2, -3, -4]
#print(maximum_sum_of_contigous_subarray(a))

#a = [1,2,3,5,6,7,8,9]
#print(missing_element(a))

a=[1, 5, 9, 10, 15, 20]
b=[2,3,8,13]
print(merge_sorted_arrays(a,b))

