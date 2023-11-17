from script_1 import get_github_commits, save_commits_to_json
from script_2 import process_commits, save_commits_to_csv

if __name__ == '__main__':
    github_token = input("Digite sua token de acesso ao GitHub: ")
    commits_data = get_github_commits(github_token)
    if commits_data:
        save_commits_to_json(commits_data)
        processed_data = process_commits(commits_data)
        save_commits_to_csv(processed_data)
    else:
        print("Falha ao carregar os dados de commits da API do GitHub.")
