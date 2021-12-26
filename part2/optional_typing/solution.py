from typing import Dict, Optional


class User:
    pass


def get_user_by_id(users: Dict[int, User], user_id: int) -> Optional[User]:
    return users.get(user_id)
