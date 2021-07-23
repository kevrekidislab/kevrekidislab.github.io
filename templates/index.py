from sys import argv
notebooks_list = argv[1:]

from os.path import basename

title = "Kevrekidis Lab"
notebooks_list_html = "<ul>"
for notebook_ipynb in notebooks_list:
    notebook_ipynb = basename(notebook_ipynb)
    notebook_html = notebook_ipynb.replace(".ipynb", ".html")
    notebook_base = basename(notebook_ipynb).replace(".ipynb", "")
    notebooks_list_html += (
        "\n    <li>"
        + f"<a href='notebooks_html/{notebook_html}'>{notebook_base}</a>"
        + f" | (<a href='notebooks/{notebook_ipynb}' download='{notebook_ipynb}''>{notebook_ipynb}</a>)"
        + "</li>"
    )
notebooks = f"<h2>Notebooks</h2>{notebooks_list_html}"

print(f"""
<!DOCTYPE html>
<html>
<head>
<title>{title}</title>
<style type="text/css">
body{{
    margin: 40px auto;
    max-width: 650px;
    line-height: 1.6;
    font-size: 18px;
    color: #444;
    padding: 0 10px;
}}
h1,h2,h3{{
    font-family: Helvetica, Arial, sans-serif;
    line-height: 1.2;
}}
</style>
</head>
<body>
<h1>{title}</h1>
{notebooks}
</body>
</html>
""")