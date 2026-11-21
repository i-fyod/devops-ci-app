# devops-ci-app

Educational Flask service. Endpoints: `/` identifies the service; `/health` returns `{"status":"ok"}`.

```sh
python -m pip install -r requirements-dev.txt
python -m pylint app tests --score=no
python -m pytest -v
docker build -t devops-ci-app:local .
docker run --rm -p 127.0.0.1:18080:5000 devops-ci-app:local
```

CI executes lint → test → image build → smoke-test. Only verified pushes to main publish `ghcr.io/i-fyod/devops-ci-app:latest` and a tag containing the full commit SHA. Pull requests never receive registry write credentials or publish an image.

Intentionally failing PR commits demonstrate a broken health response and a broken Gunicorn entry point. This repository contains no production configuration.
