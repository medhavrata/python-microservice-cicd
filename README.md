[![Python application test with Github Actions](https://github.com/medhavrata/python-microservice-cicd/actions/workflows/devops.yml/badge.svg)](https://github.com/medhavrata/python-microservice-cicd/actions/workflows/devops.yml)

# python-microservice-cicd
Deploy Python Microservice to AWS via CI/CD

## Scaffold

![Screenshot 2022-08-29 at 21 50 06](https://user-images.githubusercontent.com/10562673/187296411-7b3b2a4a-2975-453d-8725-7d713d383111.png)


1. Create a Python Virtual Environment 'python3 -m venv ~/.venv' or 'virtualenv ~/.venv'
2. Make empty files: 'requirements.txt', 'Makefile', 'Dockerfile', 'main.py', 'mylib', 'mylib/__init__.py', 'mylib/logic.py'
3. Populate Makefile
4. Setup Continuous Integration i.e. to prevent any errors like lint error


![Lint Error] (https://user-images.githubusercontent.com/10562673/173145170-a12532a1-94e7-4103-a1f0-936422d1dba5.png)

5. Build cli using Python File library ' ./cli-fire.py --help' to test logic
