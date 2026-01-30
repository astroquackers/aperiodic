def dmcalc(arraysd):
    """
    Calculate the absolute difference between all distinct pairs
    of elements in the input array, excluding self-pairs (i.e., diagonal).

    Input:
		1D array of numerical values.

    Return:
        1D array of absolute differences between all unique pairs.

	References:
		Used in Kalari et al. (2018, A&A, 618), Kalari et al. (2026, A&A)
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




