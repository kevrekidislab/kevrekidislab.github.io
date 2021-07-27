from glob import glob
from os.path import dirname, basename, join
HERE = dirname(__file__)

notebooks_list = glob(join(HERE, '..', 'notebooks', '*.ipynb'))


title = "Kevrekidis Lab Tutorial Notebooks"
notebooks_list_html = "<ul>"
for notebook_ipynb in notebooks_list:
    notebook_ipynb = basename(notebook_ipynb)
    notebook_html = notebook_ipynb.replace(".ipynb", ".html")
    notebook_base = basename(notebook_ipynb).replace(".ipynb", "")
    notebooks_list_html += (
        "\n    <li>"
        + f"<a href='notebooks_html/{notebook_html}'>{notebook_base}</a>"
        + f" | (<a href='notebooks/{notebook_ipynb}' download='{notebook_ipynb}''>notebook</a>)"
        + "</li>"
    )
notebooks = f"{notebooks_list_html}"

style = """
body{
    margin: 40px auto;
    max-width: 650px;
    line-height: 1.6;
    font-size: 18px;
    color: #444;
    padding: 0 10px;
}
a:link {
    color: #003;
}
/* visited link */
a:visited {
    color: #303;
}
/* mouse over link */
a:hover {
    color: #008;
}
/* selected link */
a:active {
    color: #00f;
}
h1,h2,h3{
    font-family: Lato, Helvetica, Arial, sans-serif;
    line-height: 1.2;
}
p{
    font-family: Lato, Helvetica, Arial, sans-serif;
}
.paper-body{
    background-color: #fff;
    box-shadow: 1px 1px 5px rgba(0,0,0,0.1);
    padding: 40px;
}
"""

print(f"""
<!DOCTYPE html>
<html>
<head>
<title>{title}</title>
<style type="text/css">
{style}
</style>
</head>
<body>
<div class="paper-body">
    <h1>{title}</h1>
    {notebooks}
</div>
</body>
</html>
""")