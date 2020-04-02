COMPONENT=calendar_generator

all : dependencies
	@ fbs run

dependencies:
	@ python -m pip install --upgrade pip
	@ python -m pip install -r ./requirements.txt

clean:
	@ git clean -fdx

.PHONY: dependencies clean