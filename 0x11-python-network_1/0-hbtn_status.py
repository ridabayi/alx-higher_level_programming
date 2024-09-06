#!/usr/bin/python3
import requests

def fetch_github_user(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        user_data = response.json()
        print("User Data:")
        print(f"\t- Login: {user_data.get('login')}")
        print(f"\t- ID: {user_data.get('id')}")
        print(f"\t- Name: {user_data.get('name')}")
        print(f"\t- Public Repos: {user_data.get('public_repos')}")
    else:
        print(f"Failed to retrieve data: {response.status_code}")

if __name__ == "__main__":
    username = "ridabayi"  
    fetch_github_user(username)
