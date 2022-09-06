install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#format code
	black *.py mylib/*.py
lint:
	#flake8 or #pylint
	pylint --disable=R,C *.py mylib/*.py
test:
	#test
	python -m textblob.download_corpora
	python -m pytest -vv --cov=mylib --cov=main test_*.py
build:
	#build a container
	docker container build -t my-app .
deploy:
	#deploy
all: install format lint test deploy