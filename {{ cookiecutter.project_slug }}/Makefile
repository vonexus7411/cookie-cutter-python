# Define the directories
APPLICATION_NAME := {{ cookiecutter.project_slug }}
NOTEBOOK_DIR := notebooks
SCRIPTS_DIR := src
NOTEBOOK_FILES := $(wildcard $(NOTEBOOK_DIR)/*.ipynb)

convert:
	$(NOTEBOOK_FILES:$(NOTEBOOK_DIR)/%.ipynb=$(SCRIPTS_DIR)/%.py)
	$(SCRIPTS_DIR)/%.py: $(NOTEBOOK_DIR)/%.ipynb
		jupyter nbconvert --to script --output-dir $(SCRIPTS_DIR) $<

build:
	docker build -t $(APPLICATION_NAME) .

run:
	docker run $(APPLICATION_NAME)