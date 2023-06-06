def sum_age_values(data:list) -> int:
    """
    Return the sum of all age values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of all age values in the dictionary
    """
    list1=[]
    count=0
    for i in data:
        if i['age']:
            list1.append(i['age'])
        
    for j in list1:
            count+=j   
            
    return count
print(sum_age_values(data=[
  {
    'name': 'John', 
    'age': 27
  }, 
  {
    'name': 'Mary', 
    'age': 42
  }
]))