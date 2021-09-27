from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QObject, Qt, pyqtSignal
from pynput import keyboard
import generators
import pyperclip

keyboard_controller = keyboard.Controller()
def copy(str):
  pyperclip.copy(str)
def type(str):
  keyboard_controller.type(str)

class Opener(QObject):
  open = pyqtSignal()
  close = pyqtSignal()

def get_label(text):
  label = QLabel(text)
  font = QFont(label.font().family(), 25)
  label.setFont(font)
  return label

class HotkeysWindow(QWidget):
  def __init__(self, **kwargs) -> None:
    super().__init__(**kwargs)
    layout = QVBoxLayout()
    self.hotkeys = [
      ['e', 'E', 'E-mail', lambda: type(generators.random_email())],
      ['p', 'P', 'E-mail próprio', lambda: type(generators.randon_self_email('bananas@bananas.com'))],
      ['c', 'C', 'CPF', lambda: type(generators.random_cpf())],
      ['T', 'T', 'Telefone', lambda: type(generators.random_brazilian_phone_number())],
    ]
    for sc in self.hotkeys:
      layout.addWidget(get_label(sc[1] + ': ' + sc[2]))
    layout.addWidget(get_label('Esc: cancelar'))
    self.setLayout(layout)
    self.setWindowFlag(Qt.FramelessWindowHint)
    self.listener = None
  
  def center(self):
    frameGm = self.frameGeometry()
    screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
    centerPoint = QApplication.desktop().screenGeometry(screen).center()
    centerPoint.setY(int(centerPoint.y() / 2))
    frameGm.moveCenter(centerPoint)
    self.move(frameGm.topLeft())

  def close(self):
    super().close()
    self.listener.stop()


  def show_and_focus(self):
    self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
    self.show()

    def hotkey_callback(cmd):
      def run_hotkey(cmd):
        self.close()
        keyboard_controller.press(keyboard.Key.backspace)
        cmd()
      return lambda: run_hotkey(cmd)

    hotkeys_obj = {}
    for sc in self.hotkeys:
      hotkeys_obj[sc[0]] = hotkey_callback(sc[3])
    
    self.listener = keyboard.GlobalHotKeys(hotkeys_obj)
    self.listener.start()

def main():

  def show_faker_shortcuts():
    window.show_and_focus()
    window.center()

  def hide_faker_shortcuts():
    window.close()

  def on_activate():
    opener.open.emit()

  def on_hide():
    opener.close.emit()
  
  listener = keyboard.GlobalHotKeys({
    '<ctrl>+<alt>+h': on_activate,
    '<esc>': on_hide,
  })
  listener.start()

  app = QApplication([])

  window = HotkeysWindow()
  
  opener = Opener(parent=window)
  opener.open.connect(show_faker_shortcuts)
  opener.close.connect(hide_faker_shortcuts)
  
  app.setQuitOnLastWindowClosed(False)
  app.exec()

  listener.stop()
  if window.listener is not None:
    window.listener.stop()

if __name__ == '__main__':
  main()