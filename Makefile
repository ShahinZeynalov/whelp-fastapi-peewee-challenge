init:
	docker-compose up --build

down:
	docker-compose down

test:
	docker-compose exec django py.test
