# GroupGitExercise

This repo is a group exercise for COSC499. We start with a list of integers and each develope a sorting feature for it based on sorting algorithms.

### Bubble Sort
Bubble Sort can be called using `bubbleSort(unsortedArray)`. This will take an unsorted array as input and return a sorted array in O(n^2) time.

### Quicksort
To run the quicksort on the list simply call `quickSort(quick, 0, n-1)` where n-1 is the last element of the list. The function will return a sorted list using the quicksort algorithm.

### Insertion Sort
The fifth feature utilizes the Insertion Sort algorithm. Calling the function `feature5(list)`, where list is the unsorted list of integers, returns a sorted list from the insertion sort algorithm.

## Unit Testing in Python
[Check the official documentation here](https://docs.python.org/3/library/unittest.html)

1. Open terminal
2. Navigate using `cd` to the directory that contains the class you want to test and your test class.
3. Enter the command below to run the unit test. The "test_class" text is replaced with the name of your test file.
`python -m unittest test_class`
