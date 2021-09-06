
#Take on all possible values 1-(n-1)
# Function to check whether given
# sequence is Jolly Jumper or not
def isJolly(arr, num):
    # Boolean vector to diffSet set
    # of differences. The vector is
    # initialized as false.
    diffSet = [False] * num

    # Traverse all array elements
    for i in range(0, num - 1):

        # Find absolute difference between
        # current two
        d = abs(arr[i] - arr[i + 1])

        # If difference is out of range or
        # repeated, return false.
        if (d == 0 or d > num - 1 or diffSet[d] == True):
            return False

        # Set presence of d in set.
        diffSet[d] = True

    return True


# Driver Code
arr = [41423]
num = len(arr)

print("Yes") if isJolly(arr, num) else print("No")