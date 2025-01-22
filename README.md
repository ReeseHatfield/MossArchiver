# MossArchiver

A tool to archive [MOSS](https://theory.stanford.edu/~aiken/moss/) results.
This tool will only archive the top 30 results, to comply with stanfords rate limit policies.

## Usage:
```bash
./archive.sh --link [moss result link]
```
Just throw in the link returned to you from the official MOSS perl script from stanford.
By default, links expire in two weeks, with MossArchiver, you can save them forever.


If you can't run a shell script, you can also just make a .venv and
```
pip install -r requirements.txt
python3 src/main.py [moss result link]
```
