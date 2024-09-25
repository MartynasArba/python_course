from typing import Union, Optional

def add_element_to_collection(element: Union[int, float, str], \
                              collection: Union[list, tuple, set, dict]) -> Optional[Union[list, tuple, set, dict]]:
  if isinstance(collection, list): 
    # if type(collection) == list:
    return collection + [element]
  elif isinstance(collection, tuple):
    return tuple(list(collection) + [element])
  elif isinstance(collection, set):
    return set(list(collection) + [element])
  elif isinstance(collection, dict):
    return dict(list(collection.items()) + [(element, None)])
  else:
    print('Unsupported collection / not a collection!')

def euros_to_dollars(amount_euros: float, exchange_rate: float = 1.1):
    return amount_euros * exchange_rate