API_NAME=tiny-actuarial-poc-template

# Run FastAPI directly on local machine
dev:
	uvicorn app.main:app --reload

build:
	docker build -t ${API_NAME} .

up:
	docker run -p 8000:8000 ${API_NAME}

down:
	docker stop $$(docker ps -q --filter ancestor=${API_NAME} )

test:
	pytest

format:
	black .

check:
	mypy .


