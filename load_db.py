import glob
from pathlib import Path
import duckdb
import pandas as pd

DUCKDB = "data_tests/data.duckdb"


def main():
    """
    Load csv files into duckdb database.
    """

    conn = duckdb.connect(database=str(DUCKDB), read_only=False)

    files = glob.glob("data/*.csv")

    for file in files:
        table_name = Path(file).stem
        df = pd.read_csv(file)
        conn.register(table_name, df)
        try:
            conn.execute(
                f"CREATE TABLE {table_name} AS SELECT * FROM {table_name}"
            )
            print(f"Table {table_name} created successfully.")
        except Exception as e:
            print(e)

    conn.close()


if __name__ == "__main__":
    main()
