import random
import time

def selection_sort(alist):
    comparisons = 0
    for i in range(len(alist)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, i+1):
            comparisons += 1
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        temp = alist[i]
        alist[i] = alist[positionOfMax]
        alist[positionOfMax] = temp
    return comparisons
    
def insertion_sort(alist):
    comparisons = 0
    for i in range(1, len(alist)):
        value = alist[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if value < alist[j]:
                alist[j + 1] = alist[j]
                alist[j] = value
                j = j - 1
            else:
                break
    return comparisons
   

def main():
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234) 
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 32000)
    start_time = time.time() 
    comps = insertion_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)

if __name__ == '__main__': 
    main()

