import sys
from PyQt5.QtWidgets import QApplication, QFileDialog


def open_dir():
    return QFileDialog.getExistingDirectory()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    print(open_dir())
    app.quit()
    # sys.exit(app.exec_())
