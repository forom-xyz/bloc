"""Build index.html (for bloc.forom.xyz) from page.html (the preview version)."""
import pathlib
here = pathlib.Path(__file__).parent
page = (here / 'page.html').read_text(encoding='utf-8')
head, body = page.split('</style>', 1)
out = f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta property="og:title" content="Bloc Couleur">
<meta property="og:description" content="Le parti violet du Québec. On ne promet pas : on construit.">
<meta property="og:url" content="https://bloc.forom.xyz">
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<style>body{{margin:0}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
{head}</style>
</head>
<body>
{body.lstrip()}
</body>
</html>
'''
(here / 'index.html').write_text(out, encoding='utf-8')
print('index.html built')
