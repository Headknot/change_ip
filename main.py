import subprocess
from ui_files import change_ip

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import sys

si = subprocess.STARTUPINFO()
si.dwFlags = subprocess.STARTF_USESTDHANDLES | subprocess.STARTF_USESHOWWINDOW

class MainWindow(QMainWindow, change_ip.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        adapter_names = get_network_adapter_names()

        for adapter in adapter_names:
            self.comboBox_interface.addItem(adapter)

        self.pushButton_clear.clicked.connect(self.clear)
        self.pushButton_quit.clicked.connect(self.quit)
        self.pushButton_current_config.clicked.connect(self.show_current_config)
        self.pushButton_set_static.clicked.connect(self.pre_set_static)

        self.comboBox_template.currentIndexChanged.connect(self.templates)

    def templates(self):
        if self.comboBox_template.currentText() == "Clavister G2": 
            self.QLineEdit_ip.setText("169.254.0.100")
            self.QLineEdit_mask.setText("255.255.0.0")
            self.QLineEdit_gw.setText("169.254.0.1")

        elif self.comboBox_template.currentText() == "Clavister GS":
            self.QLineEdit_ip.setText("192.168.1.2")
            self.QLineEdit_mask.setText("255.255.255.0")
            self.QLineEdit_gw.setText("192.168.1.1")

        elif self.comboBox_template.currentText() == "VirtualAccess":
            self.QLineEdit_ip.setText("192.168.100.2")
            self.QLineEdit_mask.setText("255.255.255.0")
            self.QLineEdit_gw.setText("192.168.100.1")
        
        elif self.comboBox_template.currentText() == "Choose...":
            self.QLineEdit_ip.setText("")
            self.QLineEdit_mask.setText("")
            self.QLineEdit_gw.setText("")

        elif self.comboBox_template.currentText() == "DHCP":
            self.QLineEdit_ip.setText("0.0.0.0")
            self.QLineEdit_mask.setText("0.0.0.0")
            self.QLineEdit_gw.setText("0.0.0.0")

        else:
            self.textEdit.append("Something went wrong!")
        
    def set_dhcp(self, adapter):
        """set chosen adapter to use dhcp"""
        cmd=subprocess.Popen('netsh interface ipv4 set address name="{}" source=dhcp'.format(adapter), shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE, stdout=subprocess.PIPE, startupinfo=si, creationflags=0x08000000)
        output, errors =  cmd.communicate()
        if errors: 
            self.textEdit.append("Error! {}".format(errors))

        elif output == b'The requested operation requires elevation (Run as administrator).\n\r\n':
            self.textEdit.append("Error - Rerun the application as administrator")

        elif output == b'DHCP is already enabled on this interface.\r\n\r\n':
            self.textEdit.append("Info - DHCP is already enabled on this interface.")

        else:
            self.textEdit.append("Info - IP Successfully changed!")

    def set_static(self, adapter, ip, mask, gw):
        """set chosen adapter to use static IP"""
        if self.comboBox_template.currentText() == "DHCP":
            self.pre_set_dhcp()

        else:
            cmd=subprocess.Popen('netsh interface ipv4 set address name="{}" source=static {} {} {}'.format(adapter, ip, mask, gw), shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE, stdout=subprocess.PIPE, startupinfo=si, creationflags=0x08000000)
            output, errors =  cmd.communicate()
            if errors: 
                self.textEdit.append("Error! {}".format(errors))

            elif output == b'The requested operation requires elevation (Run as administrator).\n\r\n':
                self.textEdit.append("Error - Rerun the application as administrator") 

            else:
                self.textEdit.append("Info - IP Successfully changed!")

    def pre_set_static(self):
        """checks all QLineEdits before calling set_static"""
        ip = self.QLineEdit_ip.text()
        mask = self.QLineEdit_mask.text()
        gw = self.QLineEdit_gw.text()
        adapter = self.comboBox_interface.currentText() 
        self.set_static(adapter, ip, mask, gw)

    def pre_set_dhcp(self):
        adapter = self.comboBox_interface.currentText()
        self.set_dhcp(adapter)

    def show_current_config(self):
        adapter = self.comboBox_interface.currentText()
        current_config = subprocess.Popen('netsh interface ipv4 show address name="{}"'.format(adapter), shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE, stdout=subprocess.PIPE, startupinfo=si, creationflags=0x08000000).stdout.read()
        current_config = str(current_config)
        current_config_splitted = current_config.split("\\r\\n")
        ip = current_config_splitted[3].split(" ")
        ip = ip[-1]

        self.textEdit.append("Info - Current adapter IP: {}".format(ip))

    def clear(self):
        self.QLineEdit_ip.setText("")
        self.QLineEdit_mask.setText("")
        self.QLineEdit_gw.setText("")
        self.textEdit.setText("")
        self.comboBox_template.setCurrentIndex(0)
        self.comboBox_interface.setCurrentIndex(0)

    def quit(self):
        sys.exit(0)

def get_network_adapter_names():
        """Lists network adapter names from ipconfig output"""
        adapter_names = []
        adapters = subprocess.Popen("ipconfig | findstr adapter", shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE, stdout=subprocess.PIPE, startupinfo=si, creationflags=0x08000000).stdout.read()
        adapters = str(adapters)
        adapters = adapters.split("\\r\\n")

        for adapter in adapters:
            adapter = adapter.replace("b'", "")
            adapter = adapter.replace("Ethernet adapter ", "")
            adapter = adapter.replace("Wireless LAN adapter ", "")
            adapter = adapter.replace(":", "")
            adapter = adapter_names.append(adapter)

        adapter_names.remove("'")
        return adapter_names

def main():
    QT_app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    QT_app.exec_()

if __name__ == "__main__":
    main()