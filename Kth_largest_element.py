"""
Given an array of integers arr and an integer k, find the kth largest element
"""

import heapq

num_array = [4, 2, 9, 7, 5, 6, 7, 1, 3]

k = 4

#First solution
def kth_largest(arr, k):
    for i in range(k-1):
        arr.remove(max(arr))
    return(max(arr))

        
print(kth_largest(num_array, k))



#second solution
def kth_largest2(arr, k):
    n = len(arr)
    arr.sort()
    return arr[n-k]

print(kth_largest2(num_array, k))



#3rd solution

def kth_largest3(arr, k):
    arr = [-elem for elem in arr]
    heapq.heapify(arr)
    for i in range (k-1):
        heapq.heappop(arr)
    return - heapq.heappop(arr)

print(kth_largest3(num_array, k))
