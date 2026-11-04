---
tags: [programming, qt, cpp, qmake]
updated: 2026-11-04
---
# Qt Tips & Pitfalls

> [!summary] Summary
> About 60 short tips for Qt 4 / 5 projects, grouped by topic: **1 qmake & build, 2 Kits & deploying, 3 Widgets & styling, 4 Tables, models & input, 5 Threads, events & memory, 6 Network, files & database, 7 Platform quirks, 8 General habits**.

> [!info] Source and Qt version
> Condensed and rewritten from a much longer list of Qt tips found online (author not recorded). Most tips date from the Qt 4 / Qt 5 era. Where Qt 6 removed something, it is noted. See [[Qt Basics]] for classes, downloads and built-in icons.

---

## 1. qmake & Build

### Useful `.pro` lines

```qmake
VERSION  = 2020.10.25          # exe version number (Qt 5+)
RC_ICONS = main0.ico           # exe icon (Qt 5+)
CONFIG += console              # also open a console window for debug output
CONFIG -= debug_and_release    # don't create empty debug/ and release/ folders
CONFIG += resources_big        # needed for big resources, e.g. font files
```

- **Parallel build:** add `MAKEFLAGS=-j8` to the kit's build environment. New Qt Creator versions already do this.
- **Qt Charts** (ships with Qt since 5.7, minimum Qt 5.4 to build; tick it in the installer, it is off by default): add `QT += charts`, then in code:

```cpp
#include <QChartView>
QT_CHARTS_USE_NAMESPACE
class CustomChart : public QChartView
```

### Run as administrator, run on XP (MSVC only)

```qmake
QMAKE_LFLAGS += /MANIFESTUAC:"level='requireAdministrator' uiAccess='false'"   # always run as administrator
QMAKE_LFLAGS += /SUBSYSTEM:WINDOWS,"5.01"                                       # VS2013: run on Windows XP
```

### Output folder by bitness

```qmake
win32 {
    contains(DEFINES, WIN64) { DESTDIR = $${PWD}/../../bin64 }
    else                      { DESTDIR = $${PWD}/../../bin32 }
}
```

### Check the Qt version and the kit architecture

```qmake
message(qt version: $$QT_VERSION)
QT_VERSION = $$[QT_VERSION]
QT_VERSION = $$split(QT_VERSION, ".")
QT_VER_MAJ = $$member(QT_VERSION, 0)
QT_VER_MIN = $$member(QT_VERSION, 1)
greaterThan(QT_VER_MAJ, 4) {            # Qt 5 or newer
    greaterThan(QT_VER_MIN, 4) { }      # 5.5 or newer
}

# QT_ARCH exists in Qt 5+ only
message($$QT_ARCH)
contains(QT_ARCH, arm)    { }           # ARM kit
contains(QT_ARCH, i386)   { }           # 32-bit kit
contains(QT_ARCH, x86_64) { }           # 64-bit kit
```

### Check whether a module exists or is used

```qmake
qtHaveModule(webenginewidgets) { message("webenginewidgets found") }
!qtHaveModule(webkit)          { message("webkit not found") }
contains(QT, network)          { message("project uses network") }
!contains(QT, widgets)         { message("project does not use widgets") }
```

### Build sub-projects in order

```qmake
TEMPLATE = subdirs
CONFIG  += ordered          # build in the order listed, for sub-projects that depend on each other
SUBDIRS += demo
SUBDIRS += designer
SUBDIRS += examples
```

---

## 2. Kits & Deploying

### Pick the right MSVC kit

- 32-bit Qt: choose a kit starting with `x86`. 64-bit Qt: choose one starting with `amd64`.
- Names **without** an underscore are native (build and run on the same kind of machine). Names **with** an underscore are cross-compilers: the first part is the machine you compile on, the second part is the machine it runs on.

| Toolchain | Compile on | Runs on |
|---|---|---|
| `x86` | 32 / 64-bit OS | 32 / 64-bit OS |
| `x86_amd64` | 32 / 64-bit OS | 64-bit OS |
| `x86_arm` | 32 / 64-bit OS | ARM |
| `amd64` | 64-bit OS | 64-bit OS |
| `amd64_x86` | 64-bit OS | 32 / 64-bit OS |
| `amd64_arm` | 64-bit OS | ARM |

Most PCs are 64-bit, so `amd64` is the usual choice. If you must support 32-bit Windows, use 32-bit Qt: it runs on both.

### Which Qt goes with which MSVC

Common pairs: **Qt 5.7 + VS2013, Qt 5.9 + VS2015, Qt 5.12 + VS2017**. With these, all the usual modules exist. A combination such as Qt 5.12 + MSVC2015 may lack modules like WebEngine, because the official build was made with MSVC2017.

### Setup tips

- **Never install Qt, the compiler, or put projects in folders with non-ASCII (e.g. Chinese) names.** Use English paths, ideally the default install location.
- **Qt Creator acting up?** Delete its settings folder, it is recreated on the next start: `C:\Users\<user>\AppData\Roaming\QtProject`.
- **Older installers ask you to register:** disable the network adapter before starting the installer and the step can be skipped.
- **Deploying to Android from Qt Creator:** first get the same project working in Android Studio, so all the SDK / NDK problems are solved there.

### Package an application

- `windeployqt` (Qt 5+; `linuxdeployqt` on Linux, `macdeployqt` on macOS) does most of the work. But it can add files you don't need, **miss plugins** (especially with QML), and doesn't know third-party libraries (e.g. copy the ffmpeg DLLs yourself).
- Last resort: copy your exe into Qt's `bin` folder, package the whole folder, then delete the components you think are unused one by one until the program stops working.
- Using **WebEngine**: ship `QtWebEngineProcess.exe` plus the `translations` and `resources` folders.

### Runtime errors after packaging

| Message | Cause / fix |
|---|---|
| `This application failed to start because it could not find or load the Qt platform plugin` | The `platforms` plugin folder was not packaged, or is in the wrong place |
| `Fault tolerant heap shim applied to current process. This is usually due to previous crashes.` | In `regedit` open `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers\` and delete the entry with your program's path |
| `Z-order assignment: <name> is not a valid widget` | Open the `.ui` file in a text editor, find the empty entry and delete it |
| `QSettings: failed to set subkey "xxx" (Access is denied.)` | Writing to the registry needs administrator rights: run the program as administrator |

---

## 3. Widgets & Styling

### A `QWidget` subclass ignores its stylesheet

Three fixes, **the first is strongly recommended**:

1. `this->setAttribute(Qt::WA_StyledBackground, true);`
2. Inherit from `QFrame` instead (it already paints stylesheets)
3. Draw it yourself in `paintEvent`:

```cpp
void Widget::paintEvent(QPaintEvent *)
{
    QStyleOption option;
    option.initFrom(this);
    QPainter painter(this);
    style()->drawPrimitive(QStyle::PE_Widget, &option, &painter, this);
}
```

### Changed a property used by a QSS selector? Re-polish

```cpp
style()->unpolish(ui->btn);     // drop the old style
style()->polish(ui->btn);       // apply the new one
```

List all properties of an object:

```cpp
const QMetaObject *mo = object->metaObject();
for (int i = 0; i < mo->propertyCount(); ++i) {
    QMetaProperty p = mo->property(i);
    qDebug() << p.name() << object->property(p.name());
}
```

### Keep all styles in one `.qss` file

Don't scatter `setStyleSheet` calls around the code: one `.qss` file is easier to maintain and uses less memory. Right-click styling in the designer is fine while experimenting.

Read it with `QTextStream`, not `readAll()`: `readAll()` assumes ANSI, so a file re-saved as UTF-8 by Qt Creator may stop loading. `QTextStream` copes with the encoding, including a BOM.

```cpp
QFile file(":/qss/lightblue.css");
if (file.open(QFile::ReadOnly)) {
    QTextStream in(&file);
    qApp->setStyleSheet(in.readAll());
}
```

### Small QSS facts

- Left-align button text: `QPushButton { text-align: left; }`
- Style a `QLCDNumber`: set its `segmentStyle` to `Flat` first
- Remove the dotted focus frame: `setStyleSheet("*{outline:0px;}")`
- Background image at a given position:

```css
QMainWindow > .QWidget {
    background-color: gainsboro;
    background-image: url(:/images/pagefold.png);
    background-position: top right;
    background-repeat: no-repeat
}
```

### Layout & window behaviour

- **`setGeometry: Unable to set geometry`:** Qt 5 is stricter. Make the widget visible *after* it has been added to a layout.
- **Width / height are wrong in the constructor:** read them after the widget is first shown (e.g. in `showEvent` / `resizeEvent`).
- **Window freezes after minimize and restore:**

```cpp
void showEvent(QShowEvent *e)
{
    setAttribute(Qt::WA_Mapped);
    QWidget::showEvent(e);
}
```

- **High-DPI screens (2K / 4K, especially phone apps):** set this *before* the `QApplication` is created (Qt 6 enables it by default):

```cpp
#if (QT_VERSION > QT_VERSION_CHECK(5,6,0))
    QGuiApplication::setAttribute(Qt::AA_EnableHighDpiScaling);
#endif
```

- **Frameless window that can still be resized:** `setWindowFlags(Qt::CustomizeWindowHint);`
- **Keep other windows working while a `QDialog` is open:** set the modality before `exec()`:

```cpp
QDialog dialog;
dialog.setWindowModality(Qt::WindowModal);
dialog.exec();
```

- **Find child widgets:**

```cpp
auto byName  = parent.findChildren<QWidget *>("widgetname");            // by objectName
auto all     = parent.findChildren<QPushButton *>();                     // every QPushButton below
auto direct  = parent.findChildren<QPushButton *>(QString(), Qt::FindDirectChildrenOnly);   // one level only
```

---

## 4. Tables, Models & Input

- **`QSqlTableModel` only loads 256 rows at first.** Load everything:

```cpp
while (model->canFetchMore())
    model->fetchMore();
```

- **Narrow columns ignored (Qt 5.10+):** the default minimum column width changed from 0 to 15. Set it back:

```cpp
ui->tableView->horizontalHeader()->setMinimumSectionSize(0);
```

- **A `setCellWidget` / `setItemWidget` widget is left-aligned and not stretched:** wrap it in a widget with a zero-margin layout:

```cpp
QWidget *w = new QWidget;
QHBoxLayout *layout = new QHBoxLayout(w);
layout->setSpacing(0);
layout->setContentsMargins(0, 0, 0, 0);
layout->addWidget(progress);
ui->tableWidget->setCellWidget(0, 0, w);
```

- **No wrapping and no "..." in cells:** `tableView->setWordWrap(false); tableView->setTextElideMode(Qt::ElideNone);`
- **Custom cell content (buttons, check boxes, combo boxes):** write a delegate (`QItemDelegate`).
- **Pass user data in a combo box:** the second argument of `addItem(text, userData)`, read it with `itemData()`.
- **`QLineEdit` input limits:**

```cpp
ui->lineEdit->setInputMask("000.000.000.000");                      // IP-address style mask
ui->lineEdit->setValidator(new QIntValidator(10, 120));             // integer range

QDoubleValidator *v = new QDoubleValidator(20, 50, 1);
v->setNotation(QDoubleValidator::StandardNotation);                 // without this the range is not enforced
ui->lineEdit->setValidator(v);

// Range -180 to 180 with a regular expression (Qt 6: use QRegularExpression + QRegularExpressionValidator)
QRegExp re("^-?(180|1?[0-7]?\\d(\\.\\d+)?)$");
ui->lineEdit->setValidator(new QRegExpValidator(re, this));
```

- **SQLite without creating a database file** (in-memory database): `db.setDatabaseName(":memory:");`
- **Database in a worker thread:** open the connection **in that same thread**. Opening it in the main thread and running SQL in another thread causes trouble. If you can, keep database work in the main thread.

---

## 5. Threads, Events & Memory

- **Delete objects with `deleteLater()`, not `delete`.** It frees at a safe moment; `delete` frees immediately and may crash. For a whole list: `qDeleteAll(btns);`
- **Wait without freezing the UI:**

```cpp
QEventLoop loop;
connect(reply, SIGNAL(finished()), &loop, SLOT(quit()));
loop.exec();
```

- **Call a function asynchronously (e.g. from a callback, where a direct call fails):**

```cpp
QMetaObject::invokeMethod(obj, "fun", Qt::QueuedConnection);
```

- **Don't throw everything into threads.** Serial and network I/O is already asynchronous, so receiving data does not freeze the UI. A slow UI usually comes from heavy processing or too-frequent painting (e.g. redrawing a curve for every data packet). Threads only help for truly heavy work like encoding or decoding, and the UI can only be touched from the main thread. Without a strict need, don't call the `waitFor*()` functions.
- **Timer accuracy.** The default timer can fire at 59 s instead of 60 s. For better accuracy:

```cpp
timer->setTimerType(Qt::PreciseTimer);
startTimer(interval, Qt::PreciseTimer);        // the QObject built-in timer
```

| Type | Accuracy |
|---|---|
| `Qt::PreciseTimer` | tries to keep millisecond accuracy |
| `Qt::CoarseTimer` (default) | within about 5% of the interval |
| `Qt::VeryCoarseTimer` | whole seconds only |

The OS limits it too: with a 5 ms OS tick you can't get better than 5 ms.

- **`QString::replace()` changes the original string** and also returns it.
- **`QString` to `const char *`:** use `toStdString().c_str()` (UTF-8 in Qt 5+). `toLocal8Bit()` uses the system code page and breaks non-ASCII text, for example in `setProperty()` names.
- **Path separators:** `QDir::toNativeSeparators("C:/temp/test.txt")` gives `C:\temp\test.txt`. To convert back use `QDir::fromNativeSeparators()`.
- **Weak (dynamic) properties** store temporary values: `widget->setProperty("name", value)`, `widget->property("name")`, `widget->dynamicPropertyNames()`.
- **About 80% of crashes and segmentation faults** are an out-of-range index or an uninitialized variable. Check those two first.

---

## 6. Network, Files & Database

### TCP keep-alive (detect a dead peer after a power cut or a killed process)

Linux socket options:

```cpp
int fd = tcpSocket->socketDescriptor();
int keepAlive    = 1;   // turn keep-alive on (default 0 = off)
int keepIdle     = 5;   // start probing after 5 s without data (default 7200 s)
int keepInterval = 2;   // 2 s between probes (default 75 s)
int keepCount    = 2;   // connection is dead after 2 failed probes (default 9)
setsockopt(fd, SOL_SOCKET, SO_KEEPALIVE, (void *)&keepAlive,    sizeof(keepAlive));
setsockopt(fd, SOL_TCP,    TCP_KEEPIDLE, (void *)&keepIdle,     sizeof(keepIdle));
setsockopt(fd, SOL_TCP,    TCP_KEEPINTVL, (void *)&keepInterval, sizeof(keepInterval));
setsockopt(fd, SOL_TCP,    TCP_KEEPCNT,  (void *)&keepCount,    sizeof(keepCount));
```

### `QTcpServer::incomingConnection` never called (Qt 5, 64-bit)

The signature changed from `int` to `qintptr`; override the right one:

```cpp
#if (QT_VERSION > QT_VERSION_CHECK(5,0,0))
    void incomingConnection(qintptr handle);
#else
    void incomingConnection(int handle);
#endif
```

### Other tips

- **HTTP POST with an `&`-joined string:** non-ASCII text arrives garbled unless you URL-encode it:

```cpp
QByteArray note = content.toUtf8().toPercentEncoding();
```

- **Don't open, write and close a file over and over** (e.g. a log line every 5 ms). Keep it open and close it in the destructor, or when the log file rolls over to a new day. Frequent open / close gets slower the bigger the file is.
- **Zip files with no extra library**, using Qt's private classes (add `QT += gui-private`; private APIs can change between Qt versions):

```cpp
#include "QtGui/private/qzipreader_p.h"
#include "QtGui/private/qzipwriter_p.h"

QZipReader reader(zipPath);
reader.extractAll(outDir);                  // unzip everything

QZipWriter writer(zipPath);
writer.addDirectory(dirName);
writer.addFile(fileName, data);             // data is a QByteArray
```

---

## 7. Platform Quirks

- **Android: keep the program from being closed**, with a service entry point:

```cpp
#if defined(Q_OS_ANDROID)
    QAndroidService a(argc, argv);
    return a.exec();
#else
    QApplication a(argc, argv);
    return a.exec();
#endif
```

- **Android logging:** use `qInfo()`, not `qDebug()`. Only `qInfo()` shows up.
- **Embedded Linux:** run with `./HelloQt -qws &` (Qt 4) or `./HelloQt --platform xcb` (Qt 5).
- **Embedded Linux, frameless window whose text box can't get focus:** call `activateWindow()` after `show()`:

```cpp
setWindowFlags(Qt::WindowStaysOnTopHint | Qt::FramelessWindowHint | Qt::X11BypassWindowManagerHint);
w->show();
w->activateWindow();
```

- **`QWebEngineView` shows garbage or a blank screen** (old OpenGL driver). Choose OpenGL ES or software rendering *before* creating the `QApplication` (the default is `AA_UseDesktopOpenGL`):

```cpp
#if (QT_VERSION > QT_VERSION_CHECK(5,4,0))
    QCoreApplication::setAttribute(Qt::AA_UseOpenGLES);
    // or: QCoreApplication::setAttribute(Qt::AA_UseSoftwareOpenGL);
#endif
QApplication a(argc, argv);
```

  Fullscreen plus `QWebEngineView` can also stop the right-click menu from showing. Move the window up by one pixel:

```cpp
QRect rect = qApp->desktop()->geometry();
rect.setY(-1);
rect.setHeight(rect.height());
this->setGeometry(rect);
```

- **`QMediaPlayer` is only a shell around the system's codecs.** On Windows it plays little more than MP4 by default. Install K-Lite or LAV Filters for other formats. For a serious player use libvlc or mpv, or ffmpeg directly.

---

## 8. General Habits

- When you can't find a function, look in the class header, then in its **parent classes** (and their parents). Qt has often already wrapped what you need, so also check each function's overloads.
- If searching for a Qt problem finds nothing, try the same keywords with Java, C# or Android in front: someone has often solved it there.
