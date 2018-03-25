# printJob [![GitHub issues](https://img.shields.io/github/issues/limpapud/printJob.svg)](https://github.com/limpapud/printJob/issues) [![GitHub stars](https://img.shields.io/github/stars/limpapud/printJob.svg)](https://github.com/limpapud/printJob/stargazers) [![GitHub forks](https://img.shields.io/github/forks/limpapud/printJob.svg)](https://github.com/limpapud/printJob/network) [![GitHub license](https://img.shields.io/github/license/limpapud/printJob.svg)](https://github.com/limpapud/printJob/blob/master/LICENSE)
![](https://github.com/limpapud/printJob/blob/master/assets/demo/icon.png)


### Qısa məlumat:

**printJob** Windows ƏS üzərində istənilən kompyuterdən istənilən kompyuterə daxili şəbəkə və ya internet üzərindən çap verməyə imkan yaradır. Bu çap olunan sənədi birinci kompyuterdə növbəyə əlavə edib, ikinci kompyuterin özünə aid çap növbəsin periodik yoxlayıb çap verməsinin sayəsində baş verir.

### İstifadə olunan kitabxanalar və dillər:

- [Python 3.6]( https://www.python.org/downloads/release/python-360/) - sadə olduğu qədər güclü programlaşdırma dili.
- [tkinker]( https://docs.python.org/3.0/library/tk.html) - Python üçün Tk QII əsasında qrafik interfeys.
- Python daxilində olan [os]( https://docs.python.org/2/library/os.html) modulu əməliyyat sistemi funksiyalarının istifadəsi üçün nəzərdə tutulmuş modul.
- [base64]( https://docs.python.org/2/library/base64.html) - RFC 3548 əsasında binar məlumatın şifrələmə/deşifrələmə modulu.
- [uuid]( https://docs.python.org/2/library/uuid.html) - RFC 4122 əsasında universal unikal identifikator (UUID) yaradılması üçün modul.
- [MySQLdb]( http://mysql-python.sourceforge.net/MySQLdb.html) - Python üçün MySQL TPİ.
- [schedule]( https://schedule.readthedocs.io/en/stable/) - Prosses daxilində cədvəl üzrə periodik tapşırıqların icrası üçün modul..
- [pythoncom]( http://timgolden.me.uk/pywin32-docs/pythoncom.html) - COM əsaslı interfeyslərin TPİ ilə işləmə üçün modul.
- [threading]( https://docs.python.org/2/library/threading.html) - yüksək səviyyəli axın interfeysi.
- [time]( https://docs.python.org/2/library/time.html) - müxtəlif vaxt ilə bağlı funksional.
- [pywin32]( https://github.com/mhammond/pywin32) - Python üçün Windows əlavələri.
- [pyinstaller]( https://www.pyinstaller.org/) - Python proqramı "donduran" və Windows/Linux/Mac OS X/FreeBSD/Solaris üçün Python-dan aslı olmayan yeqanə icra oluna bilən fayl yaradan modul.

### printJOB ilə hal-hazırda mümkün tapşırıqlar:

- *PDF və Word sənədlərin çapı*
- *İnternet və daxili şəbəkə üzərindən çap*

### İşləmə mexanizmi
- Çap vermək üçün "printJOB Executor.exe" faylın icra edib pəncərədə siyahıdan kompyuteri seçərək faylı seçmək lazımdır. Çap verdikdə sənədin adı, çap olunacaq mağaza adı,çap statusu, tapşırığın yaradılma tarixi və saatı və sənədin özü haqqında məlumat MySQL məlumat bazasına daxil edilir.
- Eyni zamanda işçi kompyuterində işləyən "printJOB CLient" icra faylı müəyyən periodiklik ilə (hər 2 dəqiqə) MySQL məlumat bazasın ona aid çap işlərin olub-olmadığını yoxlayır, öz "son aktiv" tarix-vaxtın yeniləyir. İş olduğu halda fayl həmən sistemdə olan standart printerdən çap olunur.
- Eyni zamanda serverdə işləyən "printJOB Server" icra faylı müəyyən periodiklik ilə (hər 2 dəqiqə) MySQL məlumat bazasında son 5 dəqiqə ərzində aktiv olmamış (yəni branch_list.last_active sütununda özünə aid xananı yeniləməmiş) kompyuterlərin "branch_list.a_status"-un deaktivləşdirir.

### Planlaşdırılan funksional:

- **şəkil çapı** - hal-hazırda yalnız ".PDF"/".DOC"/".DOCX" çap vermək olsa da digər "JPG/JPEG/BMP/PNG" formatların əlavə olunması planlaşdırılır.
- **işçi maşını verifikasiyası** - çap olunacaq maşının daha inkişaf olmuş verifikasiyası.

### *.py* faylın '.exe' faylına PyInstaller vasitəsi ilə keçirilməsi:
```%python.exe_olan_qovluq%>pyinstaller --noconsole --onefile printJOBCLient.py
```

> - *--noconsole* - proqram işləyən zaman konsolu qizlətmək üçün
> - *--onefile* - bir fayla çevirmək

### Nümaiş
----------
![alt text](https://github.com/limpapud/printJob/blob/master/assets/demo/client.PNG)
![alt text](https://github.com/limpapud/printJob/blob/master/assets/demo/executor.PNG)

Fayllar
-------------------
Mövcud faylların və qovluqların açığlaması aşağıdaki kimidir:

Əsas qovluq:

> - *printJOBClient.py* - Kliyent kompyuteri üçün icra faylının kodu.
> - *config.py* - sazlamaların saxlandığı fayl.
> - *printJOBExecutor.py* - İcra edən kompyuter üçün icra faylının kodu.
> - *printJOBServer.py* -  Tapşırıq icra edən server üçün icra faylının kodu.
> - *FunctionsFile.py* -  Əsas funksiyalar olan fayl kodu.
> - *createDB_structure.sql* -  Məlumat bazası strukturu.

İştirak və tövhə vermə
----------------------
Lahiyədə iştirak edib tövhə vermək istəyirsən? Əla! Bunun üçün **Fork** edib lahiyəni öz hesabınıza keçirib tövhələrinizi əlavə edib **Pull** sorğuların edə bilərsiniz.

> **Əlavələr:**
> - Müəllif  istənilən həcmdə tövhəni dəyərləndirir.
> - Təklif və iradları səhifə sonunda qeyd olumuş elektron ünvana və ya **Issues** -ə əlavə ilə qeyd edə bilərsiniz.


İstifadə
-------------
Lahiyə **MIT** lisenziyası ilə yayımlanır.
> **Bu deməkdir ki:**
> - **Kommersiya** məqsədi ilə istifadə etmək **icazəniz var**
> - Dəyişmək **icazəniz var**
> - Yenidən bölüşmək **icazəniz var**
> - Şəxsi məqsədlərdə istifadəyə **icazəniz var**
> - Müəllif heç bir **zəmanət vermir**
> - Müəllif heç bir **məhsuliyyət daşımır**
> - İstifadə olunan zaman istifadə olunan lisenziya və müəllif hüquqları **qeyd olunmalıdır!**


### Əlaqə

Müəllif ilə əlaqə [![](https://www.shareicon.net/data/16x16/2015/11/02/665918_email_512x512.png)](mailto:omarbayramov@hotmail.com) **omarbayramov@hotmail.com** elektron ünvan üzərindən aparıla bilər.
Əlavə olaraq sosial şəbəkə və digər saytlara linklər əlavə olunur.

[Facebook![](https://www.shareicon.net/data/32x32/2016/06/20/606800_facebook_48x48.png)](https://www.facebook.com/Omar.X.Bayramov)
[Wordpress![](https://www.shareicon.net/data/32x32/2016/07/14/606997_wordpress_64x64.png)](https://omarbayramov.wordpress.com/) [LinkedIn![](https://www.shareicon.net/data/32x32/2016/06/20/606446_linkedin_48x48.png)](https://www.linkedin.com/in/omarbayramov/)