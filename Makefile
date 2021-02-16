build:
	poetry build


collect-rst-static-files:CWD=$(shell pwd)
collect-rst-static-files:VDIR=$(shell poetry env info | grep Path | awk '{print $$2}')
collect-rst-static-files:DOCUTILS_DIR=$(VDIR)/lib/python3.9/site-packages/docutils
collect-rst-static-files:
	mkdir -p $(CWD)/django_qiyu_utils/static/css/rst
	cd $(DOCUTILS_DIR)/writers/html5_polyglot/ && cp *.css $(CWD)/django_qiyu_utils/static/css/rst/
