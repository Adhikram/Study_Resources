import numpy as np

def main():
    # Initialize an array with 3 zeros
    array = [0] * 3
    # Initialize a 3x3 matrix with all elements as 1
    adj = [[1] * 3 for _ in range(3)]
    print("Initial array:", array)
    print("Initial 3x3 matrix:", adj)

    # Initialize an array with specific values
    array = [1, 2, 3, 4, 5, 6, 7, 8, 5]
    array[0] = 1
    array[1] = 2
    array[2] = 3
    # Access the last element
    print("Last element of array:", array[-1])
    # Reverse the array
    print("Reversed array:", array[::-1])
    # Search for the first occurrence of the value 2
    index = -1
    for i in range(len(array)):
        if array[i] == 2:
            index = i
            break
    print("Index of first occurrence of 2:", index)  # 1

    # Insert a new element at the end of the array
    array.append(4)
    print("Array after appending 4:", array)

    # Delete all occurrences of the value 2 from the array
    value = 2
    array = [x for x in array if x != value]
    print("Array after deleting all occurrences of 2:", array)

    # Sort intervals based on the first element of each sublist
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    intervals.sort(key=lambda x: x[0])
    print("Sorted intervals:", intervals)

    # Initialize an adjacency list with 10 empty lists
    adjList = [[] for _ in range(10)]
    print("Initialized adjacency list:", adjList)

    # Convert a list of lists to a numpy array
    list_of_lists = [[1, 2], [3, 4], [5, 6]]
    res = np.array([np.array(l) for l in list_of_lists])
    print("Numpy array from list of lists:", res)

    # Convert a list of numpy arrays to a numpy array
    list_of_arrays = [np.array([1, 2]), np.array([3, 4]), np.array([5, 6])]
    list_of_arrays = [[1, 2], [3, 4], [5, 6]]
    print("List of arrays:", list_of_arrays)
    res = np.array(list_of_arrays)
    print("Numpy array from list of arrays:", res, end="\n\n")

    data1 = (x  for x in range(10))
    print(data1)
    data2 = [x for x in range(10)]
    print(data2)

    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    # Add Custom sort function
    def custom_sort(x):
        return x[1]
    # Sort the list of lists based on the second element of each sublist
    intervals.sort(key=custom_sort)

    # If the first element of each sublist is the same, sort based on the second element
    intervals.sort(key=lambda x: (x[0], x[1]))
    print("Sorted intervals:", intervals)
if __name__ == "__main__":
    main()