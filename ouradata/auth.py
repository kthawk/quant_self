import requests
import json
from urllib.parse import urlencode
import webbrowser
import Github

# Replace with your GitHub personal access token
GITHUB_TOKEN = "your_personal_access_token"
REPO_NAME = "kthawk/quant_self"

# Authenticate with GitHub
g = Github(GITHUB_TOKEN)

# Get the repository
repo = g.get_repo(REPO_NAME)

# List repository secrets
secrets = repo.get_secrets()
print("Repository Secrets:")
for secret in secrets:
    print(f"- {secret.name}")



# application credentials
  TOKEN = os.get


auth_params = {
  "
}
