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

- 2. Run the file `run_script.sh` with:
  - 1. **Graphic dimensions**: Width x Height in format `<num>x<num>`:
    - *Example:* 1000x400
  - 2. **Line weight**: in pixels in format `<num>px`
    - *Example:* 2px
  - 3. **CSV file names, title and CSS color**: the target CSV files, a title and a color for the line:
    - *Example:* cost.csv cost grey results.csv results orange

```shell
./run_script.sh 1000x400 2px cost.csv cost grey results.csv results orange
```
