# Binary Search Algorithm in Python
# Sahil Kumar
# On 15th August, 2021


# Recursive version of the binary search algorithm:

def rec_bin_search(arr, ele):
    # Base Case - if the length of the array goes down to 0, we know we haven't found it.
    if len(arr) == 0:
        return False

    # Recursive Case
    else:

        mid = len(arr) // 2

        # If the match is found:
        if arr[mid] == ele:
            return True

        else:

            # Call again on the second half
            if ele < arr[mid]:
                return rec_bin_search(arr[:mid], ele)

            # Or call on the first half
            else:
                return rec_bin_search(arr[mid + 1:], ele)


sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
if rec_bin_search(arr=sorted_array, ele=6):
    print("your element was found in the given array")
