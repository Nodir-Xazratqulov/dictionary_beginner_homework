def sum_float_values(data: dict) -> float:
    '''
    Return the sum of all float values in dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        float: The sum of all float values in the dictionary.
    '''

    list1=[]
    count=0
    for i in data:
        list1.append(data[i])
    
        
    for j in list1:
        
        # if str(j).find(".")!=-1:
        if type(j)==float:
            count+=j  
            
          
    return count
print(sum_float_values(data={
    'a': 1, 
    'b': 2.5,  
    'c': 3.0
}))


#???