SHELL := /bin/sh

COMPONENT=PoolCalendar

all :
	@echo "Generating binary"
	@mkdir -p output
	@pyinstaller -c -F -i src/pool.ico -n $(COMPONENT) --log-level ERROR --distpath output src/main.py
	@echo "Removing temporary files"
ifeq ($(OS),Windows_NT)
	@RD /S/Q build > nul 2>&1
	@DEL /F/S/Q $(COMPONENT).spec > nul 2>&1
else
	@rm -rf build $(COMPONENT).spec
endif
	@echo "RUN ./$(COMPONENT)"

clean:
ifeq ($(OS),Windows_NT)
	@DEL /F/S/Q $(COMPONENT).exe > nul 2>&1
else
	@rm -rf $(COMPONENT) new_calendar.csv src/__pycache__
endif

check:
	@pylint ./*.py

virtual-env:
	@echo "Installing virtualenv package"
	@python3 -m pip install --quiet virtualenv
	@echo "Creating virtual environment"
	@python3 -m virtualenv --quiet ${PWD}

.PHONY: all clean check virtual-env