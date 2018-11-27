import sys
from PyQt4 import QtGui, QtCore
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

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        #self.setGeometry(520, 660, 341, 32)
        QtGui.QMainWindow.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)
        self.resize(570, 660)
        self.move(341, 32)
        self.setWindowTitle("TraderSA")
        self.setWindowIcon(QtGui.QIcon('TeslaLogo.png'))
        self.home()
    
    def home(self):
        # Stock symbol selection
        lblStockName = QtGui.QLabel("Stock Symbol", self)
        lblStockName.move(30, 40)
        lblStockName.resize(200, 30)
        lblStockName.setObjectName(_fromUtf8("lblStockName"))
        cmbStockSymbol = QtGui.QComboBox(self)
        cmbStockSymbol.setEnabled(True)
        cmbStockSymbol.addItem("TSLA")
        cmbStockSymbol.addItem("AMZN")
        cmbStockSymbol.move(320, 40)
        cmbStockSymbol.resize(120, 30)
        #cmbStockSymbol.activated[str].connect(self.style_choice)
        #cmbStockSymbol.setCurrentText(_fromUtf8(""))
        #cmbStockSymbol.setObjectName(_fromUtf8("cmbStockSymbol"))
        # News/price source
        lblNewsPriceSource = QtGui.QLabel("News and Price Source", self)
        lblNewsPriceSource.move(30, 90)
        lblNewsPriceSource.resize(250, 30)
        lblNewsPriceSource.setObjectName(_fromUtf8("lblNewsPriceSource"))
        cmbNewsPriceSource = QtGui.QComboBox(self)
        cmbNewsPriceSource.addItem("Stocknews.com")
        cmbNewsPriceSource.move(320, 90)
        cmbNewsPriceSource.resize(200, 30)
        #cmbNewsPriceSource.setCurrentText(_fromUtf8(""))
        #cmbNewsPriceSource.setObjectName(_fromUtf8("cmbNewsPriceSource"))
        # Find Chromedriver.exe
        btnFindChromedriver = QtGui.QPushButton("Find chromedriver.exe", self)
        #btnFindChromedriver = QtGui.QPushButton(self, text="Find Chromedriver.exe", command=lambda: self.find_chrome)
        btnFindChromedriver.clicked.connect(self.find_chrome)
        btnFindChromedriver.move(30, 140)
        btnFindChromedriver.resize(260, 30)
        btnFindChromedriver.setObjectName(_fromUtf8("btnFindChromedriver"))
        # Generate a new Scored News/Price dataset
        btnGenerateNewsPriceFile = QtGui.QPushButton("Generate News-Price File", self)
        btnGenerateNewsPriceFile.clicked.connect(self.generate_data_file)
        btnGenerateNewsPriceFile.move(30, 240)
        btnGenerateNewsPriceFile.resize(260, 30)
        btnGenerateNewsPriceFile.setObjectName(_fromUtf8("btnGenerateNewsPriceFile"))
        # Select a CSV data file
        btnSelectExistingFile = QtGui.QPushButton("Select Existing File", self)
        btnSelectExistingFile.clicked.connect(self.select_existing_data_file)
        btnSelectExistingFile.move(30, 190)
        btnSelectExistingFile.resize(260, 30)
        btnSelectExistingFile.setObjectName(_fromUtf8("btnSelectExistingFile"))
        # Train the algorithm - Not used
        btnTrain = QtGui.QPushButton("Train Algorithm", self)
        btnTrain.clicked.connect(lambda: self.msg_box('Training', 'Training not Required.'))
        btnTrain.move(30, 290)
        btnTrain.resize(260, 30)
        btnTrain.setObjectName(_fromUtf8("btnTrain"))
        # Test/Correlate data
        btnTest = QtGui.QPushButton("Execute Correlation Test", self)
        btnTest.clicked.connect(lambda: self.msg_box('Correlation', 'Correlation not Required.'))
        btnTest.move(30, 340)
        btnTest.resize(260, 30)
        btnTest.setObjectName(_fromUtf8("btnTest"))
        # Testing accuracy results
        lblAccuracy = QtGui.QLabel("Training\nAccuracy", self)
        lblAccuracy.move(320, 280)
        lblAccuracy.resize(100, 50)
        lblAccuracy.setObjectName(_fromUtf8("lblAccuracy"))
        txtAccuracy = QtGui.QLineEdit("", self)
        txtAccuracy.move(430, 290)
        txtAccuracy.resize(100, 30)
        txtAccuracy.setObjectName(_fromUtf8("txtAccuracy"))
        # Correlation results multiline textbox
        lblTestResults = QtGui.QLabel("Correlation Results", self)
        lblTestResults.move(30, 400)
        lblTestResults.resize(111, 30)
        lblTestResults.setObjectName(_fromUtf8("lblTestResults"))
        textEdit = QtGui.QTextEdit("", self)
        textEdit.move(30, 440)
        textEdit.resize(500, 120)
        textEdit.setObjectName(_fromUtf8("textEdit"))
        # Dialog control buttons
        # Help
        btnHelp = QtGui.QPushButton("Help", self)
        btnHelp.clicked.connect(self.open_help)
        btnHelp.move(460, 570)
        btnHelp.resize(75, 30)
        btnHelp.setObjectName(_fromUtf8("btnHelp"))
        # Close/Exit
        btnClose = QtGui.QPushButton("Close", self)
        btnClose.clicked.connect(self.close_application)
        btnClose.move(370, 570)
        btnClose.resize(75, 30)
        btnClose.setObjectName(_fromUtf8("btnClose"))
        # Report
        btnReport = QtGui.QPushButton("Report", self)
        btnReport.clicked.connect(self.report)
        btnReport.move(280, 570)
        btnReport.resize(75, 30)
        btnReport.setObjectName(_fromUtf8("btnReport"))
        
        self.show()
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
            #yes_no_msg_box("Do you want to select a custom data set name?")
            # Stuff for this fn, see email
        soup = TraderSA.setChrome(TraderSA.chrome_path, TraderSA.price_news_source_url)
        print('soup generated')
        TraderSA.scrapeIt(soup)
        print('soup SCraped!')
        TraderSA.toCSV()
        print('\nGeneration don and the CSV data set file was named and saved here - ', TraderSA.save_data_path_name)
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
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
    
run()