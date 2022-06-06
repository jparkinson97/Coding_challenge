
import string

def numDuplicates(name, price, weight):
    
    lowercaseLetters = set(string.ascii_lowercase)
    
    if not len(name)==len(price)==len(weight):                              #check validity of inputs                   
        raise ValueError("List lengths not equal.")                                 # a value error is raised to terminate the code
    elif len(name)<1:                              
        raise ValueError("Length of products less than 1.") 
    elif len(name)>105:                                      
        raise ValueError("Length of products greater than 105.")
    for i in range(len(name)):
        for j in range(len(name[i])):
            if name[i][j] not in lowercaseLetters:
                raise TypeError("Product of index {} name incorrectly formatted.".format(i))    # a type error is used to terminate the code of a name is not all lowercase
        if len(name[i])>10 or len(name[i])<1:
            raise ValueError("Product of index {} name incorrectly formatted.".format(i))
    for i in range(len(price)):
        if price[i]<1:
            raise ValueError("Product of index {} price less than one.".format(i)) 
    for i in range(len(weight)):
        if price[i]>1000:
            raise ValueError("Product of index {} weight greater than than one thousand.".format(i)) 


    attributeSet = set()                            #this code uses a set of 3-tuples to determine whether a product is a duplicate
    duplicates = 0
    for i in range(len(name)):
        attribute = (name[i], price[i], weight[i])
        if attribute in attributeSet:               #set membership is used to determine the presence of a duplicate
            duplicates +=1
        attributeSet.add(attribute)                 #products are always added to the set, duplicates in the set are removed automatically py python
    return duplicates