import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                "../src")))
import inkpad
import pytest
from PyQt5 import QtCore


@pytest.fixture
def inkpad_app(qtbot):
    test_inkpad_app = inkpad.Inkpad()
    qtbot.addWidget(test_inkpad_app)

    return test_inkpad_app

def test_default_tab(inkpad_app):
    assert inkpad_app.content_tab.currentIndex() == 0
    assert inkpad_app.content_tab.tabText(0) == "Untitled*"


def test_new_file_trigger(inkpad_app, qtbot):
    prev_tab_count = inkpad_app.content_tab.count()
    inkpad_app.show()
    qtbot.waitForWindowShown(inkpad_app)

    qtbot.keyClick(inkpad_app.content_tab.currentWidget(),
                   QtCore.Qt.Key_N, modifier=QtCore.Qt.ControlModifier)

    curr_tab_count = inkpad_app.content_tab.count()
    assert curr_tab_count - prev_tab_count == 1
    assert inkpad_app.content_tab.tabText(1) == "Untitled*"

# def test_remove_tab(inkpad_app, qtbot):
#     inkpad_app.content_tab.tab


# def test_open_file_trigger(inkpad_app, qtbot):
#     prev_tab_count = inkpad_app.content_tab.count()
#     inkpad_app.show()
#     qtbot.waitForWindowShown(inkpad_app)

#     qtbot.keyClick(inkpad_app.content_tab.currentWidget(),
#                    QtCore.Qt.Key_O, modifier=QtCore.Qt.ControlModifier)

#     curr_tab_count = inkpad_app.content_tab.count()
#     assert curr_tab_count - prev_tab_count == 1
