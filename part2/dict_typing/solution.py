from typing import Dict, Any, Union


# solution 1
def get_postcode_with_any(address: Dict[str, Any]) -> int:
    return int(address.get('postcode'))


# solution 2
def get_postcode_with_union(address: Dict[str, Union[int, str]]) -> int:
    return int(address.get('postcode'))
