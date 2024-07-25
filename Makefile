tests:
	pytest

tests_details:
	pytest -v

tests_coverage:
	pytest -v --cov=tests --cov-report html