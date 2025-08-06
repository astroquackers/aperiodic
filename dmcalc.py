def dmcalc(arraysd):
    """
    Calculate the absolute difference between all distinct pairs
    of elements in the input array, excluding self-pairs (i.e., diagonal).

    Parameters:
        arraysd (array-like): 1D array of numerical values.

    Returns:
        numpy.ndarray: 1D array of absolute differences between all unique pairs.
    """
	arr = np.array(arraysd)
    	# Create a 2D array of absolute differences between every pair
    	# Equivalent to |arr[i] - arr[j]| for all i, j
	# against all elements to give us a 2D array
	sub_arr = np.abs(arr[:,None] - arr)
	# Get diagonal indices for the 2D array
	N = arr.size
	rem_idx = np.arange(N)*(N+1)
	# Remove the diagonal elements to exclude zero self-differences
	out = np.delete(sub_arr,rem_idx)
	return out




