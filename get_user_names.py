def get_user_names(data:list, country:str) -> list:
    """
    Return a list of users with a given country

    Args:
        data (dict): A dictionary of values
        country (str): The country to search for
    Returns:
        list: A list of users with the given country
    """
    
    max_age_name=[]
    for user in data:
        if user['country']==country:
            country=user['country']
            max_age_name.append(user['name'])
    return max_age_name
print(get_user_names(data=[
  {
    'name': 'John', 
    'country': 'USA'
  }, 
  {
    'name': 'Mary', 
    'country': 'UK'
  }
], country="UK"))