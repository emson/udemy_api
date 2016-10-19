# Makefile to build an AWS Lambda
#
# https://www.tutorialspoint.com/makefile/makefile_quick_guide.htm
# http://makefiletutorial.com/

PROJECT = 'udemy_api'
VIRTUAL_ENV = 'env'

# Default make command
all: clean build package

clean:
	@echo "--> Cleaning pyc files"
	find . -name "*.pyc" -delete
	rm -rf ./package
	@echo ""

build:
	@echo "--> Installing dependencies"
	pip install -r requirements.txt
	@echo ""

build_package:
	# clean old package dir and zip file
	rm -rf ./package/*/**
	# create new package dir and copy files
	mkdir -p ./package/tmp
	cp -a ./$(PROJECT)/. ./package/tmp/

copy_python: build_package
	if test -d $(VIRTUAL_ENV)/lib; then \
		cp -a $(VIRTUAL_ENV)/lib/python2.7/site-packages/. ./package/tmp/; \
	fi
	if test -d $(VIRTUAL_ENV)/lib64; then \
		cp -a $(VIRTUAL_ENV)/lib64/python2.7/site-packages/. ./package/tmp/; \
	fi

# zip up the package
zip: copy_python
	cd ./package/tmp && zip -r ../$(PROJECT).zip .

clean_tmp:
	# rm -rf ./package/tmp

package: zip clean_tmp



.PHONY: clean build package
