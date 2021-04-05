pre-commit:
	pre-commit install
	pre-commit autoupdate

black:
	black .

flake:
	flake8 .

mypy:
	mypy -p truechecker

lint: mypy black flake
