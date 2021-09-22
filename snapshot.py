import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt, QUrl, QTimer
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
import uuid
from urlvoid import urlvoid_url
class Screenshot(QWebEngineView):

    def capture(self, url, output_file):
        self.output_file = output_file
        self.load(QUrl(url))
        self.loadFinished.connect(self.on_loaded)
        # Create hidden view without scrollbars
        self.setAttribute(Qt.WA_DontShowOnScreen)
        self.page().settings().setAttribute(
            QWebEngineSettings.ShowScrollBars, False)
        self.show()

    def on_loaded(self):
        size = self.page().contentsSize().toSize()
        self.resize(size)
        # Wait for resize
        QTimer.singleShot(1000, self.take_screenshot)

    def take_screenshot(self):
        self.grab().save(self.output_file, b'PNG')
        self.app.quit()

def snap(url):
    app = QApplication(sys.argv)
    file_name = str(uuid.uuid1())+'.png'
    s = Screenshot()
    s.app = app
    s.capture(url, file_name)
    sys.exit(app.exec_())
    return file_name

print(snap(urlvoid_url('http://lcloud-singin.com/cgi-sys/movingpage.cgi')))
# print(snap('https://www.virustotal.com/gui/url/57059516ae70ab48ec8eef032f5eb1740925832a06088db98054fc4e24e29eb1/detection'))

# https://stackoverflow.com/questions/55231170/taking-a-screenshot-of-a-web-page-in-pyqt5


