# -*- coding: utf-8 -*-
"""
Created on Fri May 21 09:39:36 2021

@author: jkran
"""

#Group 8 Git Practice Excersize

list = [9, 11, 14, 25, 74, 23, 64, 99, 57, 86]

# Feature #1 - Bubble Sort - Luke
def bubbleSort(arr):
    n = len(arr)
  
    # Iterate over all array elements (Except last)
    for i in range(n-1):
  
        # Each iteration adds a correct in place element to the end of the array
        for j in range(0, n-i-1):
  
            # Swap elements if the current element is smaller than the next element
            if arr[j] > arr[j+1] :
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    return arr

# Feature #2 - Quick Sort - Joshua
def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
  
    for j in range(low, high):
  
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
  
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
  
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
# Function to do Quick sort
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
  
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
  
        # Separately sort elements before, partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
        return arr

# Feature #3 - Selection Sort - Devina
def feature3(input):
    #feature here
    return 

# Feature #4 - Merge Sort - Tatiana
def feature4(input):
    #feature here
    return 

# Feature #5 - Insertion Sort - Tasha
def feature5(input):
    #feature here
    return 


# Driver code for quicksort
quick = list
n = len(quick)
quick = quickSort(quick, 0, n-1)
print("Sorted array using quicksort is:", end=' ')
for i in range(n):
    print(quick[i], end=' ')