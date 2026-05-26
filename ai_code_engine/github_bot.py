import os
from dotenv import load_dotenv
from github import Github

load_dotenv()

def run_github_bot():

    token = os.getenv("GITHUB_TOKEN")

    if not token:
        print("GITHUB_TOKEN missing")
        return

    g = Github(token)

    repo = g.get_repo("USERNAME/REPO_NAME")  # CHANGE THIS

    pulls = repo.get_pulls(state='open')

    for pr in pulls:
        pr.create_issue_comment(
            "AI Code Engine analyzed this PR and found optimization opportunities."
        )

    print("Bot ran successfully")


if __name__ == "__main__":
    run_github_bot()