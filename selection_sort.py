
# Selection sort algorithm
Array = [10,3,2,5,7]
  
# loop to Traverse through all the elements in the given array
for i in range(len(Array)):
      
    min_indx = i
    # Loop to iterate over un-sorted array
    for j in range(i+1, len(Array)):
    
    #Finding the minimum element in the unsorted sub-array
        if Array[min_indx] > Array[j]:
            min_indx = j
              
    # swapping the minimum element with the element at min_index to place it at its correct position    
    Array[i], Array[min_indx] = Array[min_indx], Array[i]
print(Array)

