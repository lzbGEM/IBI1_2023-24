
seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'
def repeat_counts(seq):#define a function
   repeat1 = 'GTGTGT'
   repeat2 = 'GTCTGT'
   count= 0  #count is used to count the number      
   for i in range(len(seq)):#i start from every position in seq
       if seq[i:i+6]==repeat1 or seq[i:i+6]==repeat2:#if 6 sequence ==repeat 1,2  count will be count once
          count+=1
    
   return count #return the count

print(f"count totall number repeat of GTGTGT and GTCTGT is {repeat_counts(seq)}") #use this function









