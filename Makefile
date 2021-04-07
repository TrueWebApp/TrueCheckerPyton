pre-commit:
	pre-commit install
	pre-commit autoupdate

isort:
	isort . --profile black

black:
	black .

flake:
	flake8 .

mypy:
	mypy -p truechecker

pydocstyle:
	pydocstyle truechecker

lint: isort mypy black flake pydocstyle

requirements:
	poetry export -E ultra --without-hashes -o requirements.txt
	poetry export -E ultra --without-hashes -o requirements_dev.txt --dev
