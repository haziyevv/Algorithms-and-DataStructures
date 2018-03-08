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



def searchRange(nums, target):
    start = 0
    startPoint = -1
    endPoint = -1
    end = len(nums) - 1
        
    while start <= end:
        middle = start + (end - start) // 2
        if nums[middle] == target:
            startPoint = middle
            endPoint = middle
    
            if middle + 1 < len(nums) and nums[middle + 1] == target:
                i = middle + 1
                while i < len(nums)  and nums[i] == target:
                    endPoint = i
                    i += 1

            if middle - 1 >= 0 and nums[middle - 1] == target:
                j = middle - 1
                while j >= 0 and nums[j] == target:
                    startPoint = j
                    j -= 1
            break
          
        elif nums[middle] > target:
            end = middle - 1
        else:
            start = middle + 1
         
    return [startPoint, endPoint]


#graph algorithms

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


n1 = TreeNode("A")
n2 = TreeNode("B")
n3 = TreeNode("C")
n4 = TreeNode("D")
n5 = TreeNode("E")
n6 = TreeNode("F")
n7 = TreeNode("G")
n8 = TreeNode("H")
n9 = TreeNode("I")
n10 = TreeNode("J")
n11 = TreeNode("K")

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n4.left = n8
n5.left = n9
n5.right = n10
n7.right = n11





def dfs(root, seenList, seenStack):
    #seenList: all the nodes visited by the tree using dfs; 
    #seenStack: ass a node visited, it is added to the stack. When all its child
    #nodes are visited, it is popped out of the stack

    if root != None:
        seenList.append(root.val)
        seenStack.append(root)

        root = seenStack[-1]
        if root.left is None and root.right is not None:
            seenList.append(None)
            
        left = dfs(root.left, seenList, seenStack)
        right = dfs(root.right, seenList, seenStack)

        if left == None and right == None:
            seenStack.pop()
            return None

    else:
        return None

