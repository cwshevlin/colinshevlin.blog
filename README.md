# colinshevlin.blog

Based on [blog base](https://github.com/cwshevlin/blog-base). 

## To add a page

0. Create a [venv](https://docs.python.org/3/library/venv.html)
1. `python3 -m pip install "pelican[markdown]"`
2. `pelican-quickstart`
3. Create a file in content/
4. Copy the metadata fields from one of the existing files in content/
5. Write your thing
6. `make html`
7. `make serve` and navigate to localhost to view your thing
