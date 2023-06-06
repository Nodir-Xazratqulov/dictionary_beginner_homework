def find_max_key(data: dict):
    """
    Return the maximum int or float key in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum key in the dictionary.
    """
    list1=[]
    for key in data:
            list1.append(key)
        
    return max(list1)
print(find_max_key(data={
    1: 'a', 
    2: 'b', 
    3: 'c'
  }))