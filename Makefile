build:
	poetry build


publish:
	poetry publish --build


outdated:
	poetry show -o


update:
	poetry update
	make freeze

freeze:
	poetry export --without-hashes -f requirements.txt -o requirements.txt


format:
	poetry run black django_qiyu_utils
