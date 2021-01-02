inkpad: ui qrc

ui: src/assets/main.ui
	pyuic5 -o src/main_ui.py src/assets/main.ui

qrc: src/assets/main.qrc
	pyrcc5 -o src/main_rc.py src/assets/main.qrc

test:
	pytest -svv tests

clean:
	rm src/main_ui.py
	rm src/main_rc.py
