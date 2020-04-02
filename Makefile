COMPONENT=calendar_generator

all : dependencies
	@ python -m pip install fbs
	@ fbs run

dependencies:
	@ python -m pip install --upgrade pip
	@ python -m pip install -r ./requirements.txt

clean:
	@ git clean -fdx

.PHONY: dependencies clean