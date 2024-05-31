import requests
from framework.models.user import User

class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_user(self, user_id: int) -> User:
        response = requests.get(f"{self.base_url}/users/{user_id}")
        response.raise_for_status()
        return User(**response.json())

    def create_user(self, user: User) -> User:
        response = requests.post(f"{self.base_url}/users", json=user.dict())
        response.raise_for_status()
        return User(**response.json())

    def update_user(self, user_id: int, user: User) -> User:
        response = requests.put(f"{self.base_url}/users/{user_id}", json=user.dict())
        response.raise_for_status()
        return User(**response.json())

    def delete_user(self, user_id: int) -> int:
        response = requests.delete(f"{self.base_url}/users/{user_id}")
        response.raise_for_status()
        return response.status_code