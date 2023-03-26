export CURRENT_DIR=$(shell pwd)
export PYTHONPATH=${CURRENT_DIR}
export PYTHONWARNINGS=ignore::UserWarning

dev-setup:
	cp misc/pre-push .git/hooks/pre-push
	chmod 755 .git/hooks/pre-push
	docker-compose up -d postgres redis
	pip install -U -r requirements/local.txt

dev-setup-down:
	docker-compose down

run-makemigrations:
	alembic -c server/migrations/alembic.ini revision --autogenerate

run-migrations:
	alembic -c server/migrations/alembic.ini upgrade head

run-server:
	python3 server/main.py

run-celery-worker:
	celery -A server worker --beat --loglevel=info

run-celery-beat-with-flower:

code-formatting:
	black --config .black.cfg ./server ./tests

run-pre-push:
	git diff --stat --name-only --diff-filter=d origin/master | grep .*.py$ | xargs black --check --config .black.cfg
