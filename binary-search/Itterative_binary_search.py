# Binary Search Algorithm in Python
# Sahil Kumar
# On 15th August, 2021


# Normal version of the binary search algorithm (a.k.a itterative version)

found = False
def binary_search(arr, ele):
    low = 0
    high = len(arr) - 1

    global found
    while low <= high and not found:

        mid = (high + low) // 2

        # Checking to see if the middle item is the element we're looking for.
        if arr[mid] == ele:
            found = True
        if arr[mid] < ele:
            # limiting the range to the left side (higher)
            low = mid + 1
        else:
            # limiting the range to the right side (lower)
            high = mid - 1

        return mid


sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
result = (binary_search(arr=sorted_array, ele=6))
# print(result)

if found:
    print(f"Your element is present and was found at index: {result}")
else:
    print("Your element is not present in the given array")
