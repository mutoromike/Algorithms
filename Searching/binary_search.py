def binarySearch(array, target):
	return binary_search_func(array, target, 0, len(array)-1)

def binary_search_func(array, target, left, right):
	if left > right:
		return -1
	middle = (right + left)//2
	match = array[middle]
	
	if target == match:
		return middle
	elif target < match:
		return binary_search_func(array, target, left, middle-1)
	else:
		return binary_search_func(array, target, middle+1, right)