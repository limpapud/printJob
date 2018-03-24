# printJob [![GitHub issues](https://img.shields.io/github/issues/limpapud/printJob.svg)](https://github.com/limpapud/printJob/issues) [![GitHub stars](https://img.shields.io/github/stars/limpapud/printJob.svg)](https://github.com/limpapud/printJob/stargazers) [![GitHub forks](https://img.shields.io/github/forks/limpapud/printJob.svg)](https://github.com/limpapud/printJob/network) [![GitHub license](https://img.shields.io/github/license/limpapud/printJob.svg)](https://github.com/limpapud/printJob/blob/master/LICENSE)
<<<<<<< HEAD
###  [Məqaləni Azərbaycanca oxumaq]( https://github.com/limpapud/printJob/blob/master/README_AZ.md)
![](https://github.com/limpapud/printJob/blob/master/assets/demo/icon.png)
=======
![](https://github.com/limpapud/printJob/blob/master/assets/demo/icon.png)

>>>>>>> 741804a01f906ab5f061cd122a2de54dc04791f7


### Brief information:

**printJob** is a MS Windows supported software for printing from any PC to any PC across network and internet. It is possible as a result of queeing print job on from first PC , and periodically fetching and printing queued printing jobs from second PC.

### Languages and libraries used:

- [Python 3.6]( https://www.python.org/downloads/release/python-360/) - high-level programming language for general-purpose programming... but I do not think that this language needs any introduction.
- [tkinker]( https://docs.python.org/3.0/library/tk.html) - Graphical interface for Python based on Tk GUI.
- [os]( https://docs.python.org/2/library/os.html) - module provides a portable way of using operating system dependent functionality.
- [base64]( https://docs.python.org/2/library/base64.html) - RFC 3548  based binary data encoding/decoding module.
- [uuid]( https://docs.python.org/2/library/uuid.html) - RFC 4122 based UUID creating module.
- [MySQLdb]( http://mysql-python.sourceforge.net/MySQLdb.html) - MySQL API for Python.
- [schedule]( https://schedule.readthedocs.io/en/stable/) - In-process job schedulling module.
- [pythoncom]( http://timgolden.me.uk/pywin32-docs/pythoncom.html) - Module for working with COM based interfaces.
- [threading]( https://docs.python.org/2/library/threading.html) - high level threading interface.
- [time]( https://docs.python.org/2/library/time.html) - various functions for operations with time.
- [pywin32]( https://github.com/mhammond/pywin32) - Windows Extensions for Python.
- [pyinstaller]( https://www.pyinstaller.org/) -Program that freezes (packages) Python programs into stand-alone executables, under Windows, Linux, Mac OS X, FreeBSD, Solaris and AIX.

### Tasks accomplished by bot:

- *PDF və Word document print*
- *Print over internet and network*

### Bot features:
- Execute ***printJOB Executor.exe*** and select target PC, then browse file to print. After that filename,target PC name,print status,print job creation timestamp and file itself are placed in MySQL DB.
- At the same time, executed ***"prinJOB Client.exe"*** will periodically (2 min by default) querry DB for jobs on computer runned on and updates *branch_list.last_active* column, and if there is some job, prints it on default printer.
- Executed ***"printJOB Server.exe"*** with 2 minute period disables PC's what was inactive for more than 5 minutes (*branch_list.last_active* and *"branch_list.a_status"*).

### Planned functionality:

- **image print** - by now only ".PDF"/".DOC"/".DOCX" files are supported to print, "JPG/JPEG/BMP/PNG" format files are in planed functionality.
- **workstation verification** - client workstation extended verification.


### Demo
----------
![alt text](https://github.com/limpapud/printJob/blob/master/assets/demo/client.PNG)
![alt text](https://github.com/limpapud/printJob/blob/master/assets/demo/executor.PNG)

Files
-------------------
Existing filed and descriptions are as below:

Main folder:

> - *printJOBClient.py* - Client for printing and pooling jobs.
> - *config.py* - Configuration file.
> - *printJOBExecutor.py* - CLient for creating print jobs.
> - *printJOBServer.py* -  Server side executable for schedulled jobs execution.
> - *FunctionsFile.py* -  File with essential functions
> - *createDB_structure.sql* -  DB Structure.

Contributions
----------------------
Want to contribute? That is great! Please **Fork** and **Pull** to main branch.

> **Notes:**
> - Author appreciates any size of contribution.
> - Have some **Issues** or thoughts to share? You can share it via opening *Issue* or sending an  email that is mentioned in the end of page to author.

Usage and Licencing
-------------
Project is distributed with **MIT** licence.
> **That mean that:**
> - This software and derivatives **may be used for commercial purposes**
> - This software **may be modified**
> - This software **may be distributed**
> - This software **may be used and modified in private**
> - This licence includes a **limitation of liability**
> - This licence explicitly states that it **DOES NOT provide any warranty**
> - A copy of the licence and copyright notice must be included with the software.


### Contact

You can contact with author through [![](https://www.shareicon.net/data/16x16/2015/11/02/665918_email_512x512.png)](mailto:omarbayramov@hotmail.com) **omarbayramov@hotmail.com** mail.
Additionaly I am adding links to social network accounts and blog.

<<<<<<< HEAD
[Facebook![](https://www.shareicon.net/data/32x32/2016/06/20/606800_facebook_48x48.png)](https://www.facebook.com/Omar.X.Bayramov) [Wordpress![](https://www.shareicon.net/data/32x32/2016/07/14/606997_wordpress_64x64.png)](https://omarbayramov.wordpress.com/) [LinkedIn![](https://www.shareicon.net/data/32x32/2016/06/20/606446_linkedin_48x48.png)](https://www.linkedin.com/in/omarbayramov/)
=======
[Facebook![](https://www.shareicon.net/data/32x32/2016/06/20/606800_facebook_48x48.png)](https://www.facebook.com/Omar.X.Bayramov)
[Wordpress![](https://www.shareicon.net/data/32x32/2016/07/14/606997_wordpress_64x64.png)](https://omarbayramov.wordpress.com/) [LinkedIn![](https://www.shareicon.net/data/32x32/2016/06/20/606446_linkedin_48x48.png)](https://www.linkedin.com/in/omarbayramov/)
>>>>>>> 741804a01f906ab5f061cd122a2de54dc04791f7
