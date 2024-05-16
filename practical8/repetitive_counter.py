seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'
def count_repeats(seq, repeat):#set a function
    count = 0
    start = 0
    while True:
        start = seq.find(repeat, start)  #find the index of the repeat sequence from the start place(initially,start=0)
        if start == -1:#if can't find the repeat sequence,we can finish
            break
        else:
          count += 1
          start += 1  # Move to the next position to allow overlapping matches
    return count

seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'
repeat1 = 'GTGTGT'
repeat2 = 'GTCTGT'

count_repeat1 = count_repeats(seq, repeat1)
count_repeat2 = count_repeats(seq, repeat2)

total_count = count_repeat1 + count_repeat2

print(f"Total number of repeat elements in the sequence: {total_count}")









