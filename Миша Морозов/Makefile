build:
	docker build -t cloud_ru_image .

run:
	docker run -d --name cloud_ru_container -p 8000:8000 --env-file .env cloud_ru_image

