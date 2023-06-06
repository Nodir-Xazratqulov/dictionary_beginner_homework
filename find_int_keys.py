def find_int_keys(data: dict) -> list:
    """
    Return a list of all keys in a dictionary that are integers.
    Args:
        data (dict): A dictionary of values
    Returns:
        list: A list of all keys in the dictionary that are integers.
    """
    
    list1=[]
    list2=[]
    for i in data:
        list1.append(i)
    
    for k in list1:
        if k.isalpha():
            list1.remove(k)

    return list1
print(find_int_keys(data={
    'a': 1, 
    3 : 2, 
    'c': 3,
    10:'a'
}))