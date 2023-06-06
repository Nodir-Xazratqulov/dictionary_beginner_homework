def find_max_value(data: dict):
    """
    Return the maximum int or float value in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum value in the dictionary.
    """
    list1=[]
    for value in data:
        if value:
            list1.append(data[value])
    return max(list1)
print(find_max_value(data={
    'a' : -4, 
    'b' : -10, 
    'c' : 0
  }))