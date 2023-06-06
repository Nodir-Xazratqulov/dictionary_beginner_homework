def get_min_age_user_name(data:list) -> str:
    """
    Return the name of the user with the minimum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the minimum age in the dictionary
    """
    max_age=1000
    max_age_name=''
    for user in data:
        if user['age']<max_age:
            max_age=user['age']
            max_age_name=user['name']
    return max_age_name
print(get_min_age_user_name(data=[
  {
    'name': 'John', 
    'age': 56
  }, 
  {
    'name': 'Mary', 
    'age': 42
  }
]))