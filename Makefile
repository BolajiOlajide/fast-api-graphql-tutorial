NAME?=
ORATOR_ERROR_MESSAGE="Please specify a name for the model to create. e.g make model_create NAME=User"

dev:
	uvicorn main:app --reload

start:
	uvicorn main:app

model_create:
ifeq ($(NAME),)
	@ echo $(ORATOR_ERROR_MESSAGE)
	exit 1
else
	orator make:model $(NAME) -m
endif
