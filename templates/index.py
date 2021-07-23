from sys import argv
notebooks_list = argv[1:]

from os.path import basename

title = "Kevrekidis Lab"
notebooks_list_html = "<ul>"
for notebook_ipynb in notebooks_list:
    notebook_ipynb = basename(notebook_ipynb)
    notebook_html = notebook_ipynb.replace(".ipynb", ".html")
    notebooks_list_html += (
        "\n    <li>"
        + f"<a href='notebooks_html/{notebook_html}'>{notebook_html}</a>"
        + f" | (<a href='notebooks/{notebook_ipynb}'>{notebook_ipynb}/a>)"
        + "</li>"
    )
notebooks = f"<h2>Notebooks</h2>{notebooks_list_html}"

print(f"""
<!DOCTYPE html>
<html>
<head>
<title>{title}</title>
</head>
<body>
<h1>{title}</h1>
{notebooks}
</body>
</html>
""")