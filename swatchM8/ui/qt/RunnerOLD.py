# from PySide2 import QtWidgets

import sys
sys.path.append(r'D:\OneDrive - BUas\MGT\Scripts\SwatchM8')


from swatchM8.core.Main import Main
# from swatchM8.core.Main import Main

class Runner:

    def __init__(self):
        pass

    @staticmethod
    def run():
        Main(GUI=True)


Runner.run()





# class OldGUI:
#
#     def __init__(self):
#
#         self.maya = self.checkPythonVersion()
#         self.appCmds = Maya()
#
#         self.splashScreen = None
#         self.mainWindow = None
#
#         self.showSplashScreen()
#
#     def showSplashScreen(self):
#         if self.maya:
#
#             self.splashScreen = SplashScreen(self, parent=self.appCmds.getMayaWindow())
#             self.splashScreen.show()
#
#         else:
#             if __name__ == "__main__":
#                 app = QtWidgets.QApplication(sys.argv)
#                 self.splashScreen = SplashScreen(self)
#                 sys.exit(app.exec_())
#
#     def showMain(self):
#
#         if self.splashScreen is not None:
#             self.splashScreen.close()
#
#         self.mainWindow = MainWindow()
#
#         if self.maya:
#             self.mainWindow.show(dockable=True)
#         else:
#             self.mainWindow.show()
#
#     def checkPythonVersion(self):
#         pythonVersion = sys.version.split(" ")
#         if pythonVersion[0] == "3.8.6":
#             maya = False
#         else:
#             maya = True
#
#         return maya