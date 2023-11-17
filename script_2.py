import csv
from datetime import datetime


def process_commits(commits_data):
    commit_counts = {}

    for commit in commits_data:
        author_name = commit['commit']['author']['name']
        # Pega apenas a data no formato 'AAAA-MM-DD'
        commit_date = commit['commit']['author']['date'][:10]

        if commit_date not in commit_counts:
            commit_counts[commit_date] = {}

        if author_name not in commit_counts[commit_date]:
            commit_counts[commit_date][author_name] = 0

        commit_counts[commit_date][author_name] += 1

    return commit_counts


def save_commits_to_csv(processed_data):
    csv_filename = 'commits_table.csv'
    with open(csv_filename, 'w', newline='') as csv_file:
        fieldnames = ['Surrogate Key', 'Date', 'Author', 'Commit Count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        surrogate_key = 1
        for date, author_counts in processed_data.items():
            for author, count in author_counts.items():
                writer.writerow({'Surrogate Key': surrogate_key,
                                'Date': date, 'Author': author, 'Commit Count': count})
                surrogate_key += 1

    print(f'Dados tratados e salvos em "{csv_filename}"')
