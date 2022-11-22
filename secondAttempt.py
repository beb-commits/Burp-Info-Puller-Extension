from burp import IBurpExtender
from burp import ITab
from burp import IMessageEditorController
from javax import swing
from java import awt
from java.awt import BorderLayout;
from java.awt import GridLayout;
from java.awt import FlowLayout;
from javax.swing import JSplitPane;
from javax.swing import JTabbedPane;
from javax.swing import JButton;
from javax.swing import JFrame;
from javax.swing import JTable;
from javax.swing import JScrollPane;
from javax.swing import JPanel;
from javax.swing import JLabel;
from javax.swing import JTextArea;

class BurpExtender(IBurpExtender, ITab, IMessageEditorController):

    def registerExtenderCallbacks(self, callbacks):
        self.callbacks = callbacks
        self.callbacks.setExtensionName("Payload Paster")
        self.callbacks.printOutput("Welcome to my first Burp Extension. Please enjoy!")
        
        
        frame = JFrame("Payload Paster")
        frame.setSize(500, 900)
        frame.setLayout(BorderLayout())
        
        
        #Buttons and button panels
        b = JButton("Copy")
        bPanel = JPanel()
        bPanel.setLayout(FlowLayout(FlowLayout.CENTER))
        bPanel.add(b)
        b2 = JButton("Copy")
        bPanel2 = JPanel()
        bPanel2.setLayout(FlowLayout(FlowLayout.CENTER))
        bPanel2.add(b2)
        b3 = JButton("Copy")
        bPanel3 = JPanel()
        bPanel3.setLayout(FlowLayout(FlowLayout.CENTER))
        bPanel3.add(b3)
        b4 = JButton("Copy")
        bPanel4 = JPanel()
        bPanel4.setLayout(FlowLayout(FlowLayout.CENTER))
        bPanel4.add(b4)
   
       #Tabbed pane for different payloads
        tabPane = JTabbedPane(JTabbedPane.TOP)
        
        #scrollPane.setVerticalScrollBarPolicy(VERTICAL_SCROLLBAR_ALWAYS)
   
   #FIRST TAB

        textArea = JTextArea(60, 60)
        textArea.append("This is a test This is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testis a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testis a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testis a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testis a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testis a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testis a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testis a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testis a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testis a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testis a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testis a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testis a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testis a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testis a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testis a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testis a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testis a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testis a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testis a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testis a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testis a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testis a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testis a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testis a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testis a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testis a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testis a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testis a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testis a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testis a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testis a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testis a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testis a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testis a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a test")
        textPanel = JPanel()
        textPanel.setLayout(BorderLayout())
        scrollPane = JScrollPane(textArea)
        textPanel.add(scrollPane, BorderLayout.NORTH)
        textPanel.add(bPanel, BorderLayout.SOUTH)
        #textPanel.add(bPanel)
        #textPanel.add(textArea)
        #panel1 = JPanel()
        #panel1.setLayout(BorderLayout())
        #scrollPane = JScrollPane(textPanel)
        #panel1.add(textArea)
        #panel1.add(bPanel, BorderLayout.SOUTH)
        #scrollPane.add(panel1)
        tabPane.addTab("XSS", textPanel)
   
   #SECOND TAB
          
        textArea2 = JTextArea(60, 60)
        textArea2.append("This is another test \nThis is another test\nThis is another test\nThis is another test\nThis is another testThis is another test\nThis is another test\nThis is another test\nThis is another testThis is another test\nThis is another test\nThis is another test\nThis is another testThis is another test\nThis is another test\nThis is another test\nThis is another testThis is another test\nThis is another test\nThis is another test\nThis is another testThis is another test\nThis is another test\nThis is another test\nThis is another testThis is another test\nThis is another test\nThis is another test\nThis is another test")
        textPanel2 = JPanel()
        textPanel2.setLayout(BorderLayout()) 
        scrollPane2 = JScrollPane(textArea2)
        textPanel2.add(scrollPane2, BorderLayout.NORTH)
        textPanel2.add(bPanel2, BorderLayout.SOUTH)
        tabPane.addTab("SQL", textPanel2)
        
    #THIRD TAB
        
        textArea3 = JTextArea(60, 60)
        textArea3.append("This is another test" \n "This is another test")
        textPanel3 = JPanel()
        textPanel3.setLayout(BorderLayout()) 
        scrollPane3 = JScrollPane(textArea3)
        textPanel3.add(scrollPane3, BorderLayout.NORTH)
        textPanel3.add(bPanel3, BorderLayout.SOUTH)
        tabPane.addTab("Another", textPanel3)
        
    #FOURTH TAB
        
        textArea4 = JTextArea(60, 60)
        textArea4.append("This is another test" \n "This is another test")
        textPanel4 = JPanel()
        textPanel4.setLayout(BorderLayout()) 
        scrollPane4 = JScrollPane(textArea4)
        textPanel4.add(scrollPane4, BorderLayout.NORTH)
        textPanel4.add(bPanel4, BorderLayout.SOUTH)
        tabPane.addTab("MORE PAYLOADS", textPanel4)
        

        #TEXT AREA SETTINGS
        textArea.setLineWrap(True)
        textArea2.setLineWrap(True)
        textArea3.setLineWrap(True)
        textArea4.setLineWrap(True)
        textArea.setEditable(False)
        textArea2.setEditable(False)
        textArea3.setEditable(False)
        textArea4.setEditable(False)
   

        frame.add(tabPane)
        #frame.add(scrollPane)
        #frame.add(textArea)
        #frame.add(textAreaTwo)
        frame.setVisible(True)