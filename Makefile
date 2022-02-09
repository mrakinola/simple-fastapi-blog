.PHONY: up-api
up-api: ## Start API Locally
		uvicorn app.main:app --reload --port 8080

requirements: ## Install the requirements
	pip install -r requirements.txt

_git-pull: ## Pull the latest changes from git
	git pull

update-env: _git-pull requirements ## Make environment up to date
