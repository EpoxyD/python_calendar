COMPONENT=calendar_generator

all : dependencies
	@ fbs run

dependencies:
	@ python -m pip install --quiet --upgrade pip
	@ python -m pip install --quiet -r ./requirements.txt

clean:
	@ git clean -fdx

.PHONY: dependencies clean