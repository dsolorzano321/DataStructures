#lab01
#Daniel Solorzano
#CS2302

var = False
#Question1=====================================================================
def select_bubble(arr, k):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    for i in range(len(arr)):
        if k == arr[i]:
            print("K is in positon:", i)
            return i



#Question2=====================================================================

# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than the pivot 
        if   arr[j] < pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
        
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,low,high, k):
    global var
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1,k) 
        quickSort(arr, pi+1, high,k) 
        
    
    if var == False:
        for i in range(len(arr)):
            if k == arr[i]:
                var = True
                print("K is in positon:", i)
    
#Question3=====================================================================
#do with only one recursive call
def quick_modified_sort(arr,low,high, k): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        
        quickSort(arr, pi+1, high) 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]
 
select_bubble(arr, 25)
 
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]), 
        
    
        
    
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1, 8) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])
