import pytest
from MyQUIForCalc import Ui_Dialog
import pytestqt.qtbot

@pytest.fixture
def App(qtbot):
    test_app = Ui_Dialog()
    qtbot.addWidget(test_app)
    return test_app

def test_correct_answer(App):
    App.textEdit.setText("6")
    App.textEdit_2.setText("100000")
    App.textEdit_3.setText("360")
    App.textEdit_4.setText("12")
    App.CalcButton.click()
    assert "num_payment 12 c 600 princ 105 Int 495 balance 98772"==App.textEdit_5.toPlainText()
def test_failed_validation(App):
    App.textEdit.setText("6")
    App.textEdit_2.setText("100000")
    App.textEdit_3.setText("12")
    App.textEdit_4.setText("360")
    App.CalcButton.click()
    assert "ValueError"==App.textEdit_5.toPlainText()
def test_get_answer(App):
    App.textEdit.setText("6")
    App.textEdit_2.setText("100000")
    App.textEdit_3.setText("360")
    App.textEdit_4.setText("12")
    App.CalcButton.click()
    App.textEdit_5.setText("")
    App.pushButton_2.click()
    assert "num_payment 12 c 600 princ 105 Int 495 balance 98772" == App.textEdit_5.toPlainText()
def test_get_answer_which_is_not_in_database(App):
    App.textEdit.setText("6")
    App.textEdit_2.setText("100000")
    App.textEdit_3.setText("360")
    App.textEdit_4.setText("12")
    App.pushButton_2.click()
    assert "None" == App.textEdit_5.toPlainText()
