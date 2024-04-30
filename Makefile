
data-tests: data_tests/data.duckdb
	cd data_tests; dbt run; dbt test

data_tests/data.duckdb: load_db.py
	python load_db.py

install: requirements.txt
	uv pip install -r requirements.txt