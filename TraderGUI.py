import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QComboBox, QPushButton, QLineEdit, QTextEdit
from PyQt5.QtCore import QSize, QRect, Qt
#import tkinter
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
from tkinter import Tk
import os 
import TraderSA

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        #QMainWindow.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.resize(570, 660)
        self.move(341, 32)
        self.setWindowTitle("TraderSA")
        self.setWindowIcon(QtGui.QIcon('TeslaLogo.png'))
        self.home()
    
    def home(self):
        centralWidget = QWidget(self)          
        self.setCentralWidget(centralWidget)   
        # Stock symbol selection
        lblStockName = QtWidgets.QLabel("Stock Symbol", self)
        lblStockName.setGeometry(QRect(30, 40, 200, 30))
        lblStockName.setObjectName(_fromUtf8("lblStockName"))
        cmbStockSymbol = QComboBox(centralWidget)
        cmbStockSymbol.setGeometry(QRect(320, 40, 120, 30)) #int x, int y, int width, int height
        cmbStockSymbol.setEnabled(True)
        cmbStockSymbol.setObjectName(_fromUtf8("cmbStockSymbol"))
        cmbStockSymbol.addItem("TSLA")
        cmbStockSymbol.addItem("AMZN")
        # News/price source
        lblNewsPriceSource = QtWidgets.QLabel("News and Price Source", self)
        lblNewsPriceSource.setGeometry(QRect(30, 90, 250, 30))
        lblNewsPriceSource.setObjectName(_fromUtf8("lblNewsPriceSource"))
        cmbNewsPriceSource = QComboBox(self)
        cmbNewsPriceSource.addItem("Stocknews.com")
        cmbNewsPriceSource.setGeometry(QRect(320, 90, 200, 30)) 
        # Find Chromedriver.exe
        btnFindChromedriver = QPushButton("Find chromedriver.exe", self)
        btnFindChromedriver.setToolTip('To find the location of the chromedriver executable file')
        btnFindChromedriver.clicked.connect(self.find_chrome)
        btnFindChromedriver.setGeometry(QRect(30, 140, 260, 30)) 
        # Generate a new Scored News/Price dataset
        btnGenerateNewsPriceFile = QPushButton("Generate News-Price File", self)
        btnGenerateNewsPriceFile.clicked.connect(self.generate_data_file)
        btnGenerateNewsPriceFile.setGeometry(QRect(30, 240, 260, 30)) 
        # Select a CSV data file
        btnSelectExistingFile = QPushButton("Select Existing File", self)
        btnSelectExistingFile.clicked.connect(self.select_existing_data_file)
        btnSelectExistingFile.setGeometry(QRect(30, 190, 260, 30)) 
        # Train the algorithm - Not used
        btnTrain = QPushButton("Train Algorithm", self)
        btnTrain.clicked.connect(lambda: self.msg_box('Training', 'Training not Required.'))
        btnTrain.setGeometry(QRect(30, 290, 260, 30)) 
        # Test/Correlate data
        btnTest = QPushButton("Execute Correlation Test", self)
        btnTest.clicked.connect(lambda: self.msg_box('Correlation', 'Correlation not Required.'))
        btnGenerateNewsPriceFile.setGeometry(QRect(30, 340, 260, 30)) 
        btnTest.move(30, 340)
        btnTest.resize(260, 30)
        btnTest.setObjectName(_fromUtf8("btnTest"))
        # Testing accuracy results
        lblAccuracy = QtWidgets.QLabel("Training\nAccuracy", self)
        lblAccuracy.setGeometry(QRect(320, 280, 100, 50))
        lblAccuracy.setObjectName(_fromUtf8("lblAccuracy"))
        txtAccuracy = QLineEdit(self)
        txtAccuracy.setGeometry(QRect(430, 290, 100, 30))
        # Correlation results multiline textbox
        lblTestResults = QtWidgets.QLabel("Correlation Results", self)
        lblTestResults.setGeometry(QRect(30, 400, 111, 30))
        lblTestResults.setObjectName(_fromUtf8("lblTestResults"))
        textEdit = QTextEdit(self)
        textEdit.setGeometry(QRect(30, 440, 500, 120))
        # Dialog control buttons
        # Help
        btnHelp = QPushButton("Help", self)
        btnHelp.clicked.connect(self.open_help)
        btnHelp.setGeometry(QRect(460, 570, 75, 30))
        btnHelp.setObjectName(_fromUtf8("btnHelp"))
        # Close/Exit
        btnClose = QPushButton("Close", self)
        btnClose.clicked.connect(self.close_application)
        btnClose.setGeometry(QRect(370, 570, 75, 30))
        btnClose.setObjectName(_fromUtf8("btnClose"))
        # Report
        btnReport = QPushButton("Report", self)
        btnReport.clicked.connect(self.report)
        btnReport.setGeometry(QRect(280, 570, 75, 30))
        btnReport.setObjectName(_fromUtf8("btnReport"))
        
        #self.show()
        return Window
        
    def find_chrome(self):
        print('The default Chromedriver is located here - ', TraderSA.chrome_path)
        TraderSA.chrome_path = self.open_data_file("Executable", "*.exe")
        print('Chromedriver is located here - ', TraderSA.chrome_path)
        return
    
    def select_existing_data_file(self):
        print('\nThe default CSV data set is located here - ', TraderSA.open_data_path_name)
        TraderSA.open_data_path_name = self.open_data_file("Comma Separated", "*.csv")
        print('\nThe Existing CSV data set is located here - ', TraderSA.open_data_path_name)
        return
    
    def generate_data_file(self):
        print('\nIn the generate_data_file function, CSV data set file before if/then - ', TraderSA.save_data_path_name)
        if (TraderSA.save_data_path_name == 'stock_records.csv'):
            TraderSA.save_data_path_name = self.save_data_file
            print('Save Data File used')
        else:
            print('Save Data File NOT used!')
        soup = TraderSA.setChrome(TraderSA.chrome_path, TraderSA.price_news_source_url)
        print('soup generated')
        TraderSA.scrapeIt(soup)
        print('soup SCraped!')
        TraderSA.toCSV()
        print('\nGeneration done and the CSV data set file was named and saved here - ', TraderSA.save_data_path_name)
        return
    
    def select_save_data_file(self):
        print('\nThe default CSV data set file before choosing - ', TraderSA.save_data_path_name)
        TraderSA.save_data_path_name = self.save_data_file
        print('\nThe CSV data set file will be named/saved here - ', TraderSA.save_data_path_name)
        return
    
    def report(self):
        print('\nIn the generate_data_file function, CSV data set file before if/then - ', TraderSA.save_data_path_name)
        if (TraderSA.open_data_path_name == 'stock_records.csv'):
            TraderSA.open_data_path_name = self.open_data_file("Comma Separated", "*.csv")
        print('Starting CSV conversion to DataFrame.')
        data_frame = TraderSA.setDataframe(TraderSA.open_data_path_name)
        print('DataFrame loaded. Beginning Matplotlib plot generation.')
        try:
            TraderSA.correlate(data_frame)
        except:
            print('matplotlib error. Possibly not loaded or correct version.')
            self.msg_box('matplotlib', 'matplotlib error.')
    
    def open_data_file(self, file_type, file_suffix):
        root = Tk()
        root.filename =  filedialog.askopenfilename(initialdir = "C:\\", title = "Select file", filetypes = ((file_type, file_suffix),))
        print ('open_data_file subfunction test note ', root.filename)
        return root.filename

    def save_data_file(self):
        root = Tk()
        root.filename =  filedialog.asksaveasfilename(initialdir = "C:\\", title = "Select data set", filetypes = (("Comma Separated", "*.csv"),))
        print ('save_data_file subfunction test note ', root.filename)
        return
    
    def msg_box(self, title, message):
        messagebox.showinfo(title, message)
        return

    # May need to genericize this for business logic-ness
    def yesno_msgbox(self):
        if tkMessageBox.askyesno("Dataset Name", "Select New Dataset Name?"):
            return self.save_data_file(self)
            
    def close_application(self):
        sys.exit()
    
    def open_help(self):
        print("Open Help file.")
        chm_file = r'TraderSA.chm'
        os.system(chm_file)
        return
    
def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    GUI.show()
    sys.exit(app.exec_())
    
run()