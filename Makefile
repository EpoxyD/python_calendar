COMPONENT=calendar_generator

PYTHON=python3

all : dependencies
	@ fbs run

dependencies:
	@ ${PYTHON} -m pip install --quiet --upgrade pip
	@ ${PYTHON} -m pip install --quiet -r ./requirements.txt

clean:
	@ git clean -fdx

.PHONY: dependencies clean