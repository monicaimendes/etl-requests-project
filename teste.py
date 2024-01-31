import requests

resp = requests.get("https://api.github.com/users/monicaimendes")

status = resp.status_code
conteudo = resp.json()
url = resp.url

print(f"Nome: {conteudo['name']}")
print(f"Usuário: {conteudo['login']}")
print(f"Repos: {conteudo['public_repos']}")
print(f"Criada em: {conteudo['created_at']}")