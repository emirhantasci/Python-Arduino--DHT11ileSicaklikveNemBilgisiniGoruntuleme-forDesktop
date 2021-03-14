# -*- coding: utf-8 -*-

import sys
from time import *
#import serial   
import sqlite3    

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMainWindow, QMessageBox, QTableWidgetItem             
from PyQt5 import QtCore # timer için

from girissayfasi import * #giriş sayfası çağırıldı
from kayitol import * #kayıt sayfası çağırıldı
from Arduino_anapen import *  #arduino bağlantı sayfası çağırıldı
from hakkinda import *   #hakkında sayfası çağırıldı

#arduino anasayfası için bağlantılar
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_anapencere()
ui.setupUi(MainWindow)

#giriş sayfası için bağlantılar
app1=QtWidgets.QApplication(sys.argv)
MainWindow1=QtWidgets.QMainWindow()
ui1= Ui_girispenceresi() #Bu satır değişir
ui1.setupUi(MainWindow1)
MainWindow1.show()

#kayıt sayfası için bağlantılar
app2=QtWidgets.QApplication(sys.argv)
MainWindow2=QtWidgets.QMainWindow()
ui2= Ui_kayitoll() #Bu satır değişir
ui2.setupUi(MainWindow2)

#hakkında sayfası için bağlantılar
app3=QtWidgets.QApplication(sys.argv)
MainWindow3=QtWidgets.QMainWindow()
ui3= Ui_hakkinda() #Bu satır değişir
ui3.setupUi(MainWindow3)

#Veritabanı bağlantı kurma
conn=sqlite3.connect('dht11.db') 
curs=conn.cursor() 
curs.execute("CREATE TABLE IF NOT EXISTS dht11 (id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,	saat	TEXT NOT NULL,	sicaklik	TEXT NOT NULL,	nem	TEXT NOT NULL)")
conn.commit() #bağlantıyı commit ediyoruz.

#giriş-kayıt veritabanı bağlantısı
conn2=sqlite3.connect('giris.db') 
curs2=conn2.cursor() 
curs2.execute("CREATE TABLE IF NOT EXISTS giris (id2	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,	username	TEXT NOT NULL UNIQUE,	passwoord	TEXT NOT NULL, email TEXT, adsoyad TEXT)")
conn2.commit() #bağlantıyı commit ediyoruz.


sicak = """
QProgressBar {
     border: 2px solid;
	 border-color: gray;
     border-radius: 5px;
     background-color: rgb(255, 255, 255);	
 }

 QProgressBar::chunk {
     background-color: rgb(255, 0, 0);  
 }
"""

soguk = """
QProgressBar {
     border: 2px solid;
	 border-color: gray;
     border-radius: 5px;
     background-color: rgb(255, 255, 255);	
 }

 QProgressBar::chunk {
     background-color: rgb(0, 0, 255);   
 }
"""
def girisiac():
    MainWindow.close()
    #Giriş sayfası açık, diğer sayfalar kapalı
    MainWindow2.close()
    MainWindow3.close()
    MainWindow1.show()    

def kayitiac():
    MainWindow.close()
    MainWindow1.close()
    #Kayıt sayfası açık, diğer sayfalar kapalı
    MainWindow3.close()
    MainWindow2.show()
    
def hakkindaac():
    MainWindow.close()
    MainWindow1.close()
    MainWindow2.close()
    MainWindow3.show()
    #hakkında sayfası açık, diğer sayfalar kapalı

def kayitol():
    
    ad=ui2.adsoyad.text()
    kullanici=ui2.kullaniciadi.text()
    sifre1=ui2.sifre.text()
    sifre2=ui2.sifretekrar.text()
    mail=ui2.email.text()
    #Bilgiler alındı (hepsi lineedit olduğu için text komutu kullanıldı)
    
    if sifre1==sifre2:
        #eğer kayıt sayfasındaki iki şifre aynıysa kayıtı gerçekleştiriyoruz.
        curs2.execute('INSERT INTO giris (username, passwoord, email, adsoyad) VALUES ( ?, ?, ?, ?)', (kullanici,sifre1,mail,ad) )
        conn2.commit()
        ui2.statusbar.showMessage(" "*5 + " Kayıt gerçekleştirildi.", 1500)
        ui2.adsoyad.clear()  #kayıt gerçekleştikten sonra lineeditleri temizliyoruz
        ui2.kullaniciadi.clear()
        ui2.sifre.clear()
        ui2.sifretekrar.clear()
        ui2.email.clear()        
    else:
        ui2.statusbar.showMessage(" "*5 + " Kayıt gerçekleştirilemedi. Şifre alanları aynı değil. ", 1500)

        
def giris():
    #giriş sayfası kodları
    global username
    username=ui1.lineEdit_2.text()
    passwoord=ui1.lineEdit.text()
    """kullanıcının lineeditlere yazdığı username ve password bilgilerini alıp 2. veritabanı üzerinde
    arama yapıyoruz. curs2 ile."""    
    curs2.execute("SELECT * FROM giris WHERE username='%s' and passwoord='%s'" %(username,passwoord))
    conn2.commit()
    
    if(len(curs2.fetchall())>0):  #hazır komut. Veritabanının içinde otomatik olarak aramayı yapar. 
        ui.statusbar.showMessage(" "*3 + " Giriş yapıldı", 1500) 
        MainWindow1.close()
        MainWindow.show()
        """eğer veritabanı içinde aranan kişi varsa statusbar'a yazı yazıyoruz ve arduino sayfasını açıp, giriş sayfasını kapatıyoruz"""
        
    else:
        ui1.statusbar.showMessage(" "*3 + " Giriş yapılamadı.  Hatalı kullanıcı adı veya şifre", 1500)  
        
        
def sifre_goster():
    """giriş sayfası üzerinde şifre istenilirse görüntülenebilir. Bunu bir checkbox ile sağlıyoruz. ui1 üzerinde
    bulunan checkbox eğer işaretlenirse QLineEdit fonksiyonu olarak normal seçiyoruz."""
    if ui1.checkBox.isChecked():
        ui1.lineEdit.setEchoMode(QLineEdit.Normal)    
    else:
        ui1.lineEdit.setEchoMode(QLineEdit.Password)

def zaman_yaz():
    
    global zaman
    zaman = ctime() # Mon Dec 10 00:25:14 2018
    ui.label_8.setText(zaman[10:19])
    global saat
    saat=zaman[10:19]

#dikkat. timer0 değişkeni fonksiyon içinde değil!
timer0 = QtCore.QTimer()
timer0.start(1000)
timer0.timeout.connect(zaman_yaz)

def port_ac():
    
    port = str(ui.port.currentText())
    baud = str(ui.baudrate.currentText())
    
    global ser
    ser = serial.Serial(port, baudrate=baud, timeout=0)
    
    if ser.is_open:
        ui.statusbar.showMessage(" "*1 + " Port açıldı...", 1500)
    
        global timer1    
        timer1 = QtCore.QTimer()
        timer1.start(1000)
        timer1.timeout.connect(sensoroku)
    
    else:
        ui.statusbar.showMessage(" "*1 + " Port açılamadı !!!", 1500)
    
      
def port_kapat():
    
    if ser.is_open:
        
        ser.close()
        timer1.stop()
        print("Port kapatıldı...")
        
        ui.label_5.setText("")
        ui.label_6.setText("")
        
        ui.progressBar_1.setValue(1)
        ui.progressBar_2.setValue(1)
        
        ui.statusbar.showMessage(" "*1 + " Port kapatıldı...", 1500)
        
    
def sensoroku():
    
    print ("Bekleyen byte sayısı :", ser.in_waiting)
    data = ser.read(10)   # Seri Porttan 10 bytelık veri okunuyor
    print(data)
    
    veri = str(data)
    
    if len(veri) > 3: # b'' değilse...
        print(" Isı: ", veri[2:4]," Nem: ", veri[8:10])
        
        derece = float(veri[2:4])
#        derece = -35.00
        nem = float(veri[8:10])
         
        ui.label_5.setText(veri[2:4])
#        ui.label_5.setText(str(derece))
        ui.label_6.setText(veri[8:10])
        
        global sicak, soguk
        
        if derece > 0:
            ui.progressBar_1.setStyleSheet(sicak)
        
        else:
            ui.progressBar_1.setStyleSheet(soguk)
    
        ui.progressBar_1.setValue(abs(derece))
        ui.progressBar_2.setValue(nem)
        #aldığımız değerleri 1.veritabanımız yani dht veritabanı içine kaydediyoruz. 
        curs.execute('INSERT INTO dht11 (sicaklik, nem, saat ) VALUES (?,?,?)', (derece, nem, saat))
        conn.commit()
        
        listele()
    
def listele():
    #Veritabanına alınan değerleri bir tablewidget üzerinde gösteriyoruz.
    sorgu = "SELECT * FROM dht11"
    curs.execute(sorgu)
    
   
    for row, columnvalues in enumerate(curs):
#        print(row, columnvalues)
        for column, value in enumerate(columnvalues):
#            print(column, value)
            ui.tablWdht11.setItem(row, column, QTableWidgetItem(str(value))) #bu satıra dikkat!
        
def cikis():
    #çıkış sayfası
    try:
        port_kapat()
    except (NameError):  
        sys.exit(app.exec_())
    finally:
        sys.exit(app.exec_())
    
def kapat():
    MainWindow.close()
    MainWindow1.close()
    MainWindow2.close()
    MainWindow3.close()
    #Burada kapat dediğimiz zaman tüm mainwindowları kapatıyoruz.


#Buton bağlantıları
ui.portac.clicked.connect(port_ac)
ui.portkapat.clicked.connect(port_kapat)
ui.pb_cikis.clicked.connect(cikis)
ui1.pushButton.clicked.connect(giris)
ui1.checkBox.clicked.connect(sifre_goster)
ui1.pushButton_2.clicked.connect(kayitiac)

ui2.giris.clicked.connect(girisiac)
ui2.kayitol.clicked.connect(kayitol)

ui.actionHakk_nda.triggered.connect(hakkindaac)
ui1.actionGiri.triggered.connect(girisiac)
ui1.actionHakk_nda.triggered.connect(hakkindaac)
ui1.actionKay_t_Ol.triggered.connect(kayitiac)
ui2.actionGiri_2.triggered.connect(girisiac)
ui2.actionHakk_nda_2.triggered.connect(hakkindaac)
ui3.actionGiri.triggered.connect(girisiac)
ui3.actionKay_t_Ol.triggered.connect(kayitiac)
ui.action_k.triggered.connect(kapat)
ui1.action_k.triggered.connect(kapat)
ui2.action_cikisk.triggered.connect(kapat)
ui3.action_k.triggered.connect(kapat)
ui3.pushButton.clicked.connect(girisiac)
"""değişik mainwindowlar üzerindeki butonları ve actionları anaprogram içerisindeki fonksiyonlara bağladık"""
"""pushbuttonlar .clicked.connect ile bağlantı yapılırken action dediğimiz üst menüde bulunan alanlar .triggered.connect ile bağlantı yapılır."""
sys.exit(app.exec_())