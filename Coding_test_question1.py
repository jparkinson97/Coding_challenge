
def getMaximumOutfits(outfits, money):
    if len(outfits)<1:                                      #check the sizes of arrays and money are valid
        raise ValueError("Length of outfits less than 1.")          # a value error is raised to temrinate the code if incorrectly inputted
    elif len(outfits)>100:
        raise ValueError("Length of outfits greater than 106.")
    elif money < 1:
        raise ValueError("Money less than 1.")
    elif money >106:
        raise ValueError("Money greater than 106.")
    
    longest = []                                            #longest is the current longest sub array of clothes prices
    for i in range(len(outfits)):
        if len(outfits)-i >len(longest):                    #check the next sub array produced can be longer than the current          
                                                            #longest set of clothes. This could save some computation time. 
            index = 0                                       
            subarray = []
            while i+index<len(outfits):
                if sum(subarray)+outfits[i+index]<= money:  #if adding the next item in the outfits list does not cause the sum
                                                            #to be greater than money, then append to the list 
                    subarray.append(outfits[i+index])
                    index +=1
                else:
                    break
            if len(subarray)>len(longest):
                longest = subarray
    return len(longest)