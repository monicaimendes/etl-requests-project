import requests
import base64

class RepositoriesManipulation:

    def __init__(self, username):
        self.username = username
        self.api_base_url = "https://api.github.com"
        self.access_token = ''
        self.headers = {'Authorization': 'Bearer ' + self.access_token, 'X-GitHub-Api-Version': '2022-11-28'}

    def create_repo(self, repo_name):
        data = {
            "name": repo_name,
            "description": "Data from some companies' repositories",
            "private": False
        }

        response = requests.post(f"{self.api_base_url}/user/repos", json=data, headers=self.headers)

        print(f"repository creation status_code: {response.status_code}")


    def add_file(self, repo_name, file_name, file_path):
        # file encoding
        with open(file_path, "rb") as file:
            file_content = file.read()
        
        encoded_content = base64.b64encode(file_content)

        # upload
        url = f"{self.api_base_url}/repos/{self.username}/{repo_name}/contents/{file_name}"
        data = {
            "message": "Add new file",
            "content": encoded_content.decode("utf-8")
        }

        response = requests.put(url, json=data, headers=self.headers)
        print(f"upload status_code: {response.status_code}")

# Examples:
        
# new_repo = RepositoriesManipulation("monicaimendes")
# repo_name = "companies-repositories-languages"
# new_repo.create_repo(repo_name)

# new_repo.add_file(repo_name, 'netflix_languages.csv', 'data/netflix_languages.csv')




