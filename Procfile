web: python -m SimpleHTTPServer 5000
build: python -u `which pelican` --debug --autoreload -r content -o output -s settings/development.py
css: sass --watch theme/static/css/:theme/static/css/ --watch theme/static/css/:output/theme/css/
