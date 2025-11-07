[README.md](https://github.com/user-attachments/files/23416067/README.md)
# app-repo

Simple Flask API for GKE.

## Local run
```bash
pip install -r requirements.txt
python main.py
```

## Build locally
```bash
docker build -t myapp:dev .
docker run -p 8080:8080 myapp:dev
```

## Cloud Build trigger substitutions
- `_REGION` (e.g., us-central1)
- `_AR_REPO` (Artifact Registry repo name, e.g., my-repo)
- `_ENV_REPO` (Cloud Source Repository name for env, e.g., env-repo)
- `_ENV_BRANCH` (branch to update, e.g., main)
