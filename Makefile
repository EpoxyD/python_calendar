COMPONENT = "PoolCalendar"

all :
	@echo "Generating binary"
	@pyinstaller --noconsole --onefile -n $(COMPONENT) --log-level ERROR --distpath . *.py
	@echo "Removing temporary files"
	@rm -rf __pycache__ build *.spec
	@echo "You can now run $(COMPONENT)"

clean:
	@rm -rf $(COMPONENT)

check:
	@pylint ./*.py

.PHONY: all clean check