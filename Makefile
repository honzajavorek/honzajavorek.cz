DIR=$(PWD)
DIR_BLOG=$(DIR)/blog
DIR_PRAZENI=$(DIR)/prazeni

install:
	pip install -r requirements.txt

lint:
	flake8 $(DIR) --exclude=env*

test: lint

deploy:
	$(DIR)/scripts/deploy.sh

serve:
	cd $(DIR)/output && python -m http.server

new:
	$(DIR_BLOG)/scripts/new.py

develop:
	$(DIR_BLOG)/scripts/develop.sh

prazeni-import:
	$(DIR_PRAZENI)/scripts/import.sh

prazeni-develop:
	$(DIR_PRAZENI)/scripts/develop.sh
