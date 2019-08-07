COMPONENT=PoolCalendar

all :
	echo "Generating binary"
	pyinstaller -c -F -i src/pool.ico -n $(COMPONENT)_$(PLATFORM) --log-level ERROR --distpath . src/main.py
	rm -rf build $(COMPONENT)*.spec
	echo "You can now run the $(COMPONENT)"

clean:
	rm -f $(COMPONENT)

check:
	pylint ./*.py

.PHONY: all clean check