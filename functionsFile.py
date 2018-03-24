import base64
import os
import uuid
import MySQLdb
import schedule
import config
import pythoncom
pythoncom.CoInitialize()
from win32com import client
import time

def fileUpload(filePath):
    """Function takes path to file as an input, encodes in Base64 and returns blob of a file"""
    with open(filePath, 'rb') as f:
        blob = base64.b64encode(f.read())
    return blob

def QuerryUI(querry,a):
    """Update/Insert DB function.

    Takes Querry and parameters as an input and executes query"""
    try:
        conn = MySQLdb.connect(config.mysql_host,config.mysql_username,config.mysql_password,config.mysql_db,charset = config.mysql_encode)
        c = conn.cursor()
        c.execute(querry, a)
        conn.commit()
        conn.close()
    except:
        print("Something went wrong right in inserting into DB")

def QuerryS(querry,a):
    """SELECT DB function.

    Takes Querry and parameters as an input and executes query. Returns querry output as a result"""
    try:
        conn = MySQLdb.connect(config.mysql_host,config.mysql_username,config.mysql_password,config.mysql_db,charset = config.mysql_encode)
        c = conn.cursor()
        c.execute(querry, a)
        login = c.fetchall()
        conn.close()
        return login
    except:
        print("Something went wrong right in selecting from DB")

def insertJob(ShopName,fileLocation):
    """Print Job inserting function

    Takes PC name and File location in input, turns file to a blob and inserts 'fileLocation`,`ShopName`,`printStatus`,`creationDate`,`fileBlob' to DB
    """
    blobfile=fileUpload(fileLocation)
    a=(fileLocation,ShopName,blobfile)
    qry="""INSERT INTO `printQueue`(`fileLocation`,`ShopName`,`printStatus`,`creationDate`,`fileBlob`) VALUES (%s,%s,'0',CURRENT_TIMESTAMP,%s)"""
    QuerryUI(qry,a)

def deactShopJob():
    """PC deactivation Function
    Executes deactivationd of PCs that are inactive for more that active timeout treshhold
    """
    a=(config.client_deact_timeout,)
    qry="""UPDATE branch_list SET a_status = 0 WHERE last_active < DATE_SUB(NOW(),INTERVAL %s MINUTE_SECOND)"""
    QuerryUI(qry,a)

def updateJob(ShopName,fileLocation): #ToDO add filter for Today date, maybe BLOB also
    a=(ShopName,fileLocation)
    qry=("""UPDATE printQueue set printStatus = 1 where ShopName = %s and fileLocation = %s""")
    QuerryUI(qry,a)

def ListActiveShops(dig):
    """Function recieves status type and outputs all PCs that are in that filter. Used to show active PC list"""
    list=[]
    try:
        a=(dig,)
        qry="""SELECT branch_name FROM branch_list WHERE a_status = %s"""
        for each in QuerryS(qry,a):
            list.append(each[0])
        return list
    except:
        print('It happens')

def mass_job():
    import pythoncom
    pythoncom.CoInitialize()
    updateShopActive()
    printAndCheckJob()

def updateShopActive():
    a=(os.environ['COMPUTERNAME'],)
    qry="""UPDATE branch_list SET last_active = CURRENT_TIMESTAMP,a_status='1'  WHERE branch_name = %s"""
    QuerryUI(qry,a)


def checkJob(dig):
    try:
        list=[]
        a=(dig,os.environ['COMPUTERNAME'],)
        qry="""SELECT fileLocation,fileBlob FROM printQueue WHERE printStatus = %s and ShopName = %s"""
        for each in QuerryS(qry,a):
            list.append([each[0],each[1]])
        return list
    except:
        print('It happens')

def fileFetch(code,extention):
    filename=config.clientFolder + uuid.uuid4().hex[0:10]+ extention
    with open(os.path.expanduser(filename), 'wb') as dest:
        dest.write(base64.decodestring(code))
        print('For u: ' + filename)
        return filename


def printWord(finepath):
    import pythoncom
    pythoncom.CoInitialize()
    word = client.Dispatch("Word.Application")
    word.Documents.Open(finepath)
    word.ActiveDocument.PrintOut()
    time.sleep(2)
    word.ActiveDocument.Close()
    word.Quit()
    time.sleep(3)


def printAndCheckJob(): #add PDF and WORD file check
    import pythoncom
    pythoncom.CoInitialize()
    for each in checkJob(0):
        blob=each[1]
        ext=os.path.splitext([each[0]][0])[1]
        if ext == '.pdf':
            printPDF(fileFetch(blob,ext))
            print('print PDF')
        elif ext == '.docx':
            printWord(fileFetch(blob,ext))
            print('print WORD')
        elif ext == '.doc':
            printWord(fileFetch(blob,ext))
            print('print WORD')
        else:
            print('xuy znayet')
        updateJob(os.environ['COMPUTERNAME'],each[0])

def printPDF(finepath):
    ie = client.Dispatch("InternetExplorer.Application")
    ie.Navigate(finepath)
    if ie.Busy:
        time.sleep(1)
    ie.Document.printAll()
    time.sleep(2)
    ie.Quit()

def run_schedule():
    import pythoncom
    pythoncom.CoInitialize()
    schedule.every(150).seconds.do(mass_job)
    while True:
        schedule.run_pending()
        time.sleep(120)
