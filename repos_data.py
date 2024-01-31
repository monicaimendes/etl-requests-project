import requests
import pandas as pd
from math import ceil

class RepositoriesData:

    def __init__(self, owner):
        self.owner = owner
        self.api_base_url = 'https://api.github.com'
        self.access_token = ''
        self.headers = {'Authorization': 'Bearer ' + self.access_token, 'X-GitHub-Api-Version': '2022-11-28'}

    def repositories_list(self):
        repos_list = []

        response = requests.get(f'{self.api_base_url}/orgs/{self.owner}', headers=self.headers).json()
        public_repos = response['public_repos']

        total_pages = ceil(public_repos/30)

        for page_num in range(1,total_pages):
            try:
                url = f'{self.api_base_url}/orgs/{self.owner}/repos?page={page_num}'
                response = requests.get(url, headers=self.headers)
                repos_list.append(response.json())
            except:
                repos_list.append(None)

        return repos_list
    

    def repos_names(self, repos_list):
        repo_names = []
        for page in repos_list:
            for repo in page:
                try:
                    repo_names.append(repo['name'])
                except:
                    pass
        return repo_names
    

    def languages(self, repos_list):
        repo_languages = []
        for page in repos_list:
            for repo in page:
                try:
                    repo_languages.append(repo['language'])
                except:
                    pass

        return repo_languages
    
    def languages_dt_create(self):
        repositories = self.repositories_list()
        names = self.repos_names(repositories)
        languages = self.languages(repositories)

        data = pd.DataFrame()
        data['repository_name'] = names
        data['language'] = languages

        return data
    








