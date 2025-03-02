
from abc import ABC, abstractmethod
import requests

# Abstract class acting as an Interface
class APIClient(ABC):

    @abstractmethod
    def fetch_data(self, endpoint: str):
        """Fetch data from the API"""
        pass

    @abstractmethod
    def post_data(self, endpoint: str, payload: dict):
        """Send data to the API"""
        pass


class GitHubAPIClient(APIClient):
    def __init__(self, token):
        self.base_url = "https://api.github.com"
        self.headers = {"Authorization": f"Bearer {token}"}

    def fetch_data(self, endpoint: str):
        """Fetch data from GitHub API"""
        response = requests.get(f"{self.base_url}/{endpoint}", headers=self.headers)
        return response.json()

    def post_data(self, endpoint: str, payload: dict):
        """Post data to GitHub API"""
        response = requests.post(f"{self.base_url}/{endpoint}", json=payload, headers=self.headers)
        return response.json()


class TwitterAPIClient(APIClient):
    def __init__(self, token):
        self.base_url = "https://api.twitter.com/2"
        self.headers = {"Authorization": f"Bearer {token}"}

    def fetch_data(self, endpoint: str):
        """Fetch data from Twitter API"""
        response = requests.get(f"{self.base_url}/{endpoint}", headers=self.headers)
        return response.json()

    def post_data(self, endpoint: str, payload: dict):
        """Post data to Twitter API"""
        response = requests.post(f"{self.base_url}/{endpoint}", json=payload, headers=self.headers)
        return response.json()


def test_api(client: APIClient):
    """Generic function that works with any API client"""
    data = client.fetch_data("users/octocat")  # Fetch GitHub user data
    print(data)

def main():
    # Example usage:
    github_client = GitHubAPIClient("your_github_token")
    twitter_client = TwitterAPIClient("your_twitter_token")

    # Call API functions
    test_api(github_client)  # Fetch GitHub user data
    # test_api(twitter_client)  # Fetch Twitter user data (uncomment if using Twitter API)

if __name__=='__main__':
    main()
