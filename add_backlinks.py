# Load html file, add links just after <body>, and write back to file.

from sys import argv
html_path = argv[1]
with open(html_path) as f:
    html = f.readlines()

backlinks_html = """
<div style="padding: 40px;">
    <p style="font-style: italic;">
        <a href="https://kevrekidislab.github.io/">Back to kevrekidislab.github.io index.</a>
    </p>
</div>
""".strip() + '\n'

for i, line in enumerate(html):
    if line.startswith('<body'):
        html[i] = line + backlinks_html
        break

out = ''.join(html)
with open(html_path, 'w') as f:
    f.write(out)

print('Added backlinks to %s.' % html_path)