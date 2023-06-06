def sum_dict_values(data: dict) -> int:
    '''
    Return the sum of all values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of all values in the dictionary
    '''
    list1=[]
    count=0
    for i in data:
        if i:
            list1.append(data[i])
        
    for j in list1:
            count+=j   
            
    return count
print(sum_dict_values(data={
    'a': 1, 
    'b': 2, 
    'c': 3
}))