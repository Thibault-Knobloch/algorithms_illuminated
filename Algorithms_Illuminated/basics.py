
#RECURSIVE INTEGER MULTIPLICATION
#assumes than x and y have the same length, and have length of a power of 2
def RecIntMult(x, y):
    sx = str(x)
    sy = str(y)
    if len(sx) == 1 & len(sy) == 1:
        return x * y
    else:
        a = int(sx[:int(len(sx)/2)])
        b = int(sx[int(len(sx)/2):])
        c = int(sy[:int(len(sx)/2)])
        d = int(sy[int(len(sx) / 2):])

        ac = RecIntMult(a, c)
        ad = RecIntMult(a, d)
        bc = RecIntMult(b, c)
        bd = RecIntMult(b, d)

        return 10**(len(sx)) * ac + 10**(int(len(sx)/2))*(ad + bc) + bd

print(RecIntMult(1234, 5678))
print(1234*5678)

#to make this RecIntMult better, make cases for uneven length (add leading zeros)
#and make cases for unequal length of the inputs


#MERGE SORT ALGORITHM

tosort = [1, 6, 8, 16, 7, 9, 4, 2, 3, 5, 12]

def MergeSort(array):
    if len(array) == 0 or len(array) == 1:
        return array
    else:
        first_half = array[:int(len(array)/2)]
        second_half = array[int(len(array)/2):]

        C = MergeSort(first_half)
        D = MergeSort(second_half)

        return Merge(C, D)

def Merge(C, D):
    i = 0
    j = 0
    output = []
    for k in range(len(C) + len(D)):
        if C[i] < D[j]:
            output.append(C[i])
            if len(C[i:]) == 1:
                output = output + D[j:]
                return output
            else:
                i += 1
        else:
            output.append(D[j])
            if len(D[j:]) == 1:
                output = output + C[i:]
                return output
            else:
                j += 1
    return output


print(MergeSort(tosort))


#COUNTING INVERSIONS IN AN ARRAY (basics of collaborative filtering)
#returns number of inversions in an array and the corresponding sorted array

#recursive call to make it run in O(nlog(n))
def SortCountInv(array):
    if len(array) == 0 or len(array) == 1:
        return (array, 0)
    else:
        first_half = array[:int(len(array)/2)]
        second_half = array[int(len(array)/2):]

        (C, leftInv) = SortCountInv(first_half)
        (D, rightInv) = SortCountInv(second_half)
        (B, splitInv) = MergeCountSplitInv(C, D)

        return(B, leftInv + rightInv + splitInv)

def MergeCountSplitInv(X, Y):
    i = 0
    j = 0
    output = [] #sorted array
    numSplitInv = 0
    for k in range(len(X) + len(Y)):
        if X[i] < Y[j]:
            output.append(X[i])
            if len(X[i:]) == 1:
                output = output + Y[j:]
                return (output, numSplitInv)
            else:
                i += 1
        else:
            output.append(Y[j])
            numSplitInv += len(X[i:])
            if len(Y[j:]) == 1:
                output = output + X[i:]
                return (output, numSplitInv)
            else:
                j += 1
    return (output, numSplitInv)

#test array from book, should have 3 inversions
test_array = [1, 3, 5, 2, 4, 6]

#print(SortCountInv(test_array))


