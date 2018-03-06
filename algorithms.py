import pdb

def merge_sort(list_given):
    if len(list_given) < 2:
        return list_given
    
    mid = len(list_given) // 2
    left = list_given[0:mid]
    right = list_given[mid:]
    
    s_left = merge_sort(left)
    s_right = merge_sort(right)

    result = merge(s_left, s_right)
    return result
 

def merge(lf, ls):
    liste = []
    i = 0
    j = 0
    
    while i < len(lf) and j < len(ls):
        if lf[i] < ls[j]:
            liste.append(lf[i])
            i += 1
            
        elif lf[i] > ls[j]:
            liste.append(ls[j])
            j += 1
                
        else:
            liste.extend([lf[i], ls[j]])
            i += 1
            j += 1
    else:
        if i < len(lf):
            while i < len(lf):
                liste.append(lf[i])
                i+=1
        elif j < len(ls):
            while j < len(ls):
                liste.append(ls[j])
                j+=1            

    return liste


def partition(A, start, end):
    pivot = A[end]
    p_index = start


    for i in range(start, end):
        if A[i] <= pivot:
            A[i], A[p_index] = A[p_index], A[i]
            p_index += 1

    A[end], A[p_index] = A[p_index], A[end]

    return p_index


def quicksort(A, start, end):
    if start < end:
        p_index = partition(A, start, end)
        quicksort(A, start, p_index - 1)
        quicksort(A, p_index+1, end)



def isAnagram(s, t):
    s = list(s)
    t = list(t)

    quicksort(s, 0, len(s)-1)
    quicksort(t, 0, len(t)-1)
      
    if s == t:
        return True
    
    else:
        return False
        

def binarySearch(A, target):
    start = 0
    end = len(A) - 1
    while start < end:
        middle = (start + end) // 2
        if A[middle] == target:
            return middle
        elif A[middle] < target:
            start = middle + 1
        else:
            end = middle - 1
    else:
        return False
