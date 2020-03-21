COMPONENT=calendar_generator

all : dependencies
	@ python -m pip install fbs

run: dependencies
	@ python src/main.py

gui: dependencies
	@ python src/gui/main.py

build: dependencies
	@ python -m pip install fbs

dependencies:
	@ python -m pip install --upgrade pip
	@ python -m pip install -r .\requirements.txt

start: 
	@ python -m venv $(CURDIR)
ifeq ($(OS),Windows_NT)
	@ echo enable development enviroment with: ./Scripts/Activate.ps1 (Powershell)
else
	@ echo enable development enviroment with: source ./bin/activate (bash)
endif

clean:
	@ git clean -fd

.PHONY: all clean dependencies start run gui