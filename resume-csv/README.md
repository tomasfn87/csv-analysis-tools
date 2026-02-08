# Resume CSV

## Install dependencies

- 1. Add execution permission to the file `setup.sh`.

```shell
chmod +x setup.sh
```

- 2. Run the file `setup.sh`.

```shell
./setup.sh
```

---

## Execute Script

- 1. Add execution permission to the file `run_script.sh`.

```shell
chmod +x run_script.sh
```

- 2. Run the file `run_script.sh` with the target CSV file name and optional argument `--list-csv-fields-only` to see the list of **fields** alongside their **types**:
  - This will help to decide which operation is needed for each field.

```shell
./run_script.sh ~/CSV_files/data.csv --list-csv-fields-only
```

- 3. Edit the file `resume_csv.py` to suit your CSV file analysis:
  - For each [Data Frame](https://github.com/tomasfn87/csv-analysis-tools/blob/main/resume-csv/resume_csv.py#L37) object inside variable `result_dfs`:
    - a. Select the `desired field titles` as showed in step `ii`;
    - b. Select the [`desired operation`](https://github.com/tomasfn87/csv-analysis-tools/blob/main/resume-csv/resume_csv.py#L23) for each field (`min`, `max`, `mean`, `count`, `nunique`, etc.).

- 4. To see the results, run the file `run_script.sh` with the target CSV file as argument.

```shell
./run_script.sh ~/CSV_files/data.csv
```
