# Makefile to build an AWS Lambda
#
# http://makefiletutorial.com/

PROJECT = 'udemy_api'
VIRTUAL_ENV = 'env'

build:
	@echo "--> Installing dependencies"
	pip install -r requirements.txt
	@echo ""

clean:
	@echo "--> Cleaning pyc files"
	find . -name "*.pyc" -delete
	rm -rf ./package
	@echo ""

.PHONY: clean

package:
	# clean old package dir and zip file
	rm -rf ./package/*/**
	# create new package dir and copy files
	mkdir -p ./package/tmp
	if test -d $(VIRTUAL_ENV)/lib; then \
		cp -a ./env/lib/python2.7/site-packages/. ./package/tmp/; \
	fi
	if test -d $(VIRTUAL_ENV)/lib64; then \
		cp -a ./env/lib64/python2.7/site-packages/. ./package/tmp/; \
	fi
	cp -a ./$(PROJECT)/. ./package/tmp/
	# zip up the package
	cd ./package/tmp && zip -r ../$(PROJECT).zip .
	# delete the tmp dir
	rm -rf ./package/tmp

