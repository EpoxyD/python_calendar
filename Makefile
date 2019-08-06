COMPONENT=PoolCalendar

all :
	@echo "Generating binary"
	@pyinstaller -c -F -i src/pool.ico -n $(COMPONENT) --log-level ERROR --distpath . src/main.py
	@echo "Removing temporary files"
ifeq ($(OS),Windows_NT)
	@RD /S/Q build > nul 2>&1
	@DEL /F/S/Q $(COMPONENT).spec > nul 2>&1
	@MV $(COMPONENT).exe $(COMPONENT)
else
	@rm -rf build $(COMPONENT).spec
endif
	@echo "You can now run the $(COMPONENT)"

clean:
ifeq ($(OS),Windows_NT)
	@DEL /F/S/Q $(COMPONENT).exe > nul 2>&1
else
	@rm -f $(COMPONENT)
endif

check:
	@pylint ./*.py

.PHONY: all clean check