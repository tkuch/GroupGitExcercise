# -*- coding: utf-8 -*-
"""
Created on Fri May 21 09:39:36 2021

@author: jkran
"""

#Group 8 Git Practice Excersize

list = [9, 11, 14, 25, 74, 23, 64, 99, 57, 86]


# Feature #1 - Bubble Sort - Luke
def feature1(input):
    #feature here
    return 

# Feature #2 - Quick Sort - Joshua
def feature2(input):
    #feature here
    return 

# Feature #3 - Selection Sort - Devina
def feature3(input):
    #feature here
    return 

# Feature #4 - Merge Sort - Tatiana
def mergeSort(input):
    #feature here
    if len(input)>1:
        mid=len(input)//2
        L=input[:mid]
        R=input[mid:]

        mergeSort(L)
        mergeSort(R)

        merge(input,L,R)
    return
# Helper merge method
def merge(input,L,R):
    i=j=k=0
    while i<len(L) and j<len(R):
        if L[i]<R[i]:
            input[k]=L[i]
            i+=1
        else:
            input[k]=R[j]
            j+=1
        k+=1
    while i<len(L):
        input[k]=L[i]
        i+=1
        k+=1
    while j<len(R):
        input[k]=R[j]
        j+=1
        k+=1
    return
# Print array method
def printList(input):
    for i in range(len(input)):
        print(input[i],end=" ")
    print()

# Feature #5 - Insertion Sort - Tasha
def feature5(input):
    #feature here
    return 

