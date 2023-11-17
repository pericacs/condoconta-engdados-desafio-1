import requests
import json


def get_github_commits(token):
    repo_url = "https://api.github.com/repos/openai/openai-python/commits"
    headers = {'Authorization': f'token {token}'}

    # Parâmetros para filtrar os commits por data
    params = {
        'since': '2023-05-01T00:00:00Z',
        'until': '2023-05-31T23:59:59Z',
    }

    response = requests.get(repo_url, headers=headers, params=params)

    if response.status_code == 200:
        commits_data = response.json()
        return commits_data
    else:
        print(
            f"Falha na solicitação à API do GitHub. Código de status: {response.status_code}")
        return None


def save_commits_to_json(commits_data):
    if commits_data:
        with open('commits_data.json', 'w') as json_file:
            json.dump(commits_data, json_file, indent=4)
        print("Dados de commits salvos com sucesso em 'commits_data.json'")
    else:
        print("Não foi possível salvar os dados de commits.")
