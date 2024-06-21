def is_sorted(arr):
    """
    Checks if the given array is sorted in ascending order. (returns True or False)
    """
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

def bogo_sort(arr):
    """
    Bogo Sort: Repeatedly shuffles the array until it becomes sorted.
    """
    while not is_sorted(arr): # While is_sorted is false, it will repeat...
        # Manually shuffle the array
        for i in range(len(arr)):
            j = i + 1  # Choose the next index
            if j < len(arr):
                arr[i], arr[j] = arr[j], arr[i]

# Example usage:
my_list = [8, 2, 6, 4, 5]
bogo_sort(my_list)
print("Sorted array using Bogo Sort:", my_list)

# In essence, Bogo Sort keeps randomly rearranging the elements until it accidentally produces a sorted array. 
# It’s like trying to organize a deck of cards by throwing them in the air and hoping they land in order!
