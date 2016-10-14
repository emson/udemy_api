develop:
	@echo "--> Installing dependencies"
	pip install -r requirements.txt
	@echo ""

clean:
	@echo "--> Cleaning pyc files"
	find . -name "*.pyc" -delete
	rm -rf ./publish
	@echo ""

publish:
	rm -rf ./publish/udemy_api_lambda/
	mkdir -p ./publish/udemy_api_lambda
	cp -r ./udemy_api ./publish/udemy_api_lambda/
	# cp -r ./aws_lambda_libs/. ./publish/udemy_api_lambda/
	cp -r ./udemy_api/config/. ./publish/udemy_api_lambda/udemy_api/config/
	# cd ./publish/udemy_api_lambda && zip -r ../udemy_api_lambda.zip .

.PHONY: develop clean publish

