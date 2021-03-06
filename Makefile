NAME?=
ORATOR_ERROR_MESSAGE="Please specify a name for the model to create. e.g make model_create NAME=User"

dev:
	uvicorn main:app --reload

start:
	uvicorn main:app

model_create:
ifeq ($(NAME),)
	@ echo $(ORATOR_ERROR_MESSAGE)
else
	orator make:model $(NAME) -m
endif

migrate:
	orator migrate -c src/db.py

migration_create:
ifeq ($(NAME),)
	@ echo $(ORATOR_ERROR_MESSAGE)
else
	orator make:migration $(NAME)
endif

rollback:
	orator migrate:rollback

rollback_all:
	orator migrate:reset

run_test:
	python -m pytest -s test
