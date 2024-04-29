# data-tests
An example of how to check data quality using DBT and DuckDB.



## Installation


### Virtual Environment
Install uv to create the virtual environment:

```bash
pip install uv
```

Create the virtual environment and activate it:

```bash
uv venv
source .venv/bin/activate
```

Install the dependencies:

```bash
uv pip install -r requirements.txt
```

### DBT

Initialize the DBT project:

```bash
dbt init data_tests
```
Select duckdb as the database (option 1).

Move your profiles.yml file to the data_tests folder:

```bash
mv ~/.dbt/profiles.yml data_tests/
```