# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QStatusBar,
    QTableView, QToolBar, QVBoxLayout, QWidget)

from sp_editor import icons_rc


class Ui_mw_Main(object):
    def setupUi(self, mw_Main):
        if not mw_Main.objectName():
            mw_Main.setObjectName(u"mw_Main")
        mw_Main.resize(1366, 771)
        mw_Main.setMinimumSize(QSize(1366, 768))
        font = QFont()
        font.setPointSize(12)
        mw_Main.setFont(font)
        mw_Main.setIconSize(QSize(24, 24))
        mw_Main.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.action_New = QAction(mw_Main)
        self.action_New.setObjectName(u"action_New")
        icon = QIcon(QIcon.fromTheme(u"document-new"))
        self.action_New.setIcon(icon)
        self.action_New.setFont(font)
        self.action_Open = QAction(mw_Main)
        self.action_Open.setObjectName(u"action_Open")
        icon1 = QIcon(QIcon.fromTheme(u"document-open"))
        self.action_Open.setIcon(icon1)
        self.action_Open.setFont(font)
        self.action_Save = QAction(mw_Main)
        self.action_Save.setObjectName(u"action_Save")
        icon2 = QIcon(QIcon.fromTheme(u"document-save"))
        self.action_Save.setIcon(icon2)
        self.action_Save.setFont(font)
        self.action_Quit = QAction(mw_Main)
        self.action_Quit.setObjectName(u"action_Quit")
        icon3 = QIcon(QIcon.fromTheme(u"window-close"))
        self.action_Quit.setIcon(icon3)
        self.action_Quit.setFont(font)
        self.a_GeneralInfor = QAction(mw_Main)
        self.a_GeneralInfor.setObjectName(u"a_GeneralInfor")
        icon4 = QIcon(QIcon.fromTheme(u"document-properties"))
        self.a_GeneralInfor.setIcon(icon4)
        self.a_Groups = QAction(mw_Main)
        self.a_Groups.setObjectName(u"a_Groups")
        icon5 = QIcon()
        icon5.addFile(u":/Btn/Group_edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.a_Groups.setIcon(icon5)
        self.a_Cases = QAction(mw_Main)
        self.a_Cases.setObjectName(u"a_Cases")
        self.a_Cases.setCheckable(False)
        self.a_Cases.setChecked(False)
        icon6 = QIcon()
        icon6.addFile(u":/Btn/Calculation_Case.png", QSize(), QIcon.Normal, QIcon.Off)
        self.a_Cases.setIcon(icon6)
        self.a_GetAllForce = QAction(mw_Main)
        self.a_GetAllForce.setObjectName(u"a_GetAllForce")
        icon7 = QIcon()
        icon7.addFile(u":/Btn/Force.png", QSize(), QIcon.Normal, QIcon.Off)
        self.a_GetAllForce.setIcon(icon7)
        self.a_MakeSPcolumn = QAction(mw_Main)
        self.a_MakeSPcolumn.setObjectName(u"a_MakeSPcolumn")
        icon8 = QIcon()
        icon8.addFile(u":/Btn/spcolumn-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.a_MakeSPcolumn.setIcon(icon8)
        self.a_BatchProcessor = QAction(mw_Main)
        self.a_BatchProcessor.setObjectName(u"a_BatchProcessor")
        icon9 = QIcon()
        icon9.addFile(u":/Btn/parallel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.a_BatchProcessor.setIcon(icon9)
        self.a_Doc = QAction(mw_Main)
        self.a_Doc.setObjectName(u"a_Doc")
        icon10 = QIcon(QIcon.fromTheme(u"help-browser"))
        self.a_Doc.setIcon(icon10)
        self.a_About = QAction(mw_Main)
        self.a_About.setObjectName(u"a_About")
        icon11 = QIcon(QIcon.fromTheme(u"help-about"))
        self.a_About.setIcon(icon11)
        self.a_ImportEtabs = QAction(mw_Main)
        self.a_ImportEtabs.setObjectName(u"a_ImportEtabs")
        icon12 = QIcon()
        icon12.addFile(u":/Btn/etabs logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.a_ImportEtabs.setIcon(icon12)
        self.a_ImportEtabs.setFont(font)
        self.a_Print = QAction(mw_Main)
        self.a_Print.setObjectName(u"a_Print")
        icon13 = QIcon(QIcon.fromTheme(u"document-print"))
        self.a_Print.setIcon(icon13)
        self.a_Print.setFont(font)
        self.a_MaterialProp = QAction(mw_Main)
        self.a_MaterialProp.setObjectName(u"a_MaterialProp")
        icon14 = QIcon()
        icon14.addFile(u":/Btn/material_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.a_MaterialProp.setIcon(icon14)
        self.a_MaterialProp.setFont(font)
        self.a_BarSet = QAction(mw_Main)
        self.a_BarSet.setObjectName(u"a_BarSet")
        icon15 = QIcon()
        icon15.addFile(u":/Btn/rebar_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.a_BarSet.setIcon(icon15)
        self.a_BarSet.setFont(font)
        self.actionDesign_Combos_Selection = QAction(mw_Main)
        self.actionDesign_Combos_Selection.setObjectName(u"actionDesign_Combos_Selection")
        icon16 = QIcon()
        icon16.addFile(u":/Btn/selection.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionDesign_Combos_Selection.setIcon(icon16)
        self.centralwidget = QWidget(mw_Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 5, 9, 0)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(9, 9, 9, 9)
        self.table_sumaryResults = QTableView(self.frame_2)
        self.table_sumaryResults.setObjectName(u"table_sumaryResults")
        self.table_sumaryResults.setAutoFillBackground(False)
        self.table_sumaryResults.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_sumaryResults.setSortingEnabled(False)

        self.gridLayout_3.addWidget(self.table_sumaryResults, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 9, 0, 9)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label.setIndent(9)

        self.horizontalLayout_2.addWidget(self.label)

        self.lb_pierLabel = QLabel(self.frame_4)
        self.lb_pierLabel.setObjectName(u"lb_pierLabel")
        self.lb_pierLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lb_pierLabel)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.table_CombosDCR = QTableView(self.frame_3)
        self.table_CombosDCR.setObjectName(u"table_CombosDCR")
        self.table_CombosDCR.setSortingEnabled(True)

        self.verticalLayout_2.addWidget(self.table_CombosDCR)


        self.gridLayout.addWidget(self.frame_3, 0, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 8)
        self.gridLayout.setColumnStretch(1, 3)
        mw_Main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mw_Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1366, 33))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        self.menu_File.setFont(font)
        self.m_Define = QMenu(self.menubar)
        self.m_Define.setObjectName(u"m_Define")
        self.m_Define.setFont(font)
        self.m_Analyze = QMenu(self.menubar)
        self.m_Analyze.setObjectName(u"m_Analyze")
        self.m_Analyze.setFont(font)
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuHelp.setFont(font)
        mw_Main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mw_Main)
        self.statusbar.setObjectName(u"statusbar")
        mw_Main.setStatusBar(self.statusbar)
        self.tb_File = QToolBar(mw_Main)
        self.tb_File.setObjectName(u"tb_File")
        mw_Main.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.tb_File)
        self.tb_Define = QToolBar(mw_Main)
        self.tb_Define.setObjectName(u"tb_Define")
        mw_Main.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.tb_Define)
        self.tb_Analyze = QToolBar(mw_Main)
        self.tb_Analyze.setObjectName(u"tb_Analyze")
        mw_Main.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.tb_Analyze)
        self.tb_Help = QToolBar(mw_Main)
        self.tb_Help.setObjectName(u"tb_Help")
        mw_Main.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.tb_Help)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.m_Define.menuAction())
        self.menubar.addAction(self.m_Analyze.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menu_File.addAction(self.action_New)
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.a_ImportEtabs)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.a_Print)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.m_Define.addAction(self.a_GeneralInfor)
        self.m_Define.addSeparator()
        self.m_Define.addAction(self.a_MaterialProp)
        self.m_Define.addAction(self.a_BarSet)
        self.m_Define.addSeparator()
        self.m_Define.addAction(self.a_Groups)
        self.m_Define.addAction(self.a_Cases)
        self.m_Analyze.addAction(self.actionDesign_Combos_Selection)
        self.m_Analyze.addAction(self.a_GetAllForce)
        self.m_Analyze.addAction(self.a_MakeSPcolumn)
        self.m_Analyze.addAction(self.a_BatchProcessor)
        self.menuHelp.addAction(self.a_Doc)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.a_About)
        self.tb_File.addAction(self.action_New)
        self.tb_File.addAction(self.action_Open)
        self.tb_File.addAction(self.action_Save)
        self.tb_File.addAction(self.a_Print)
        self.tb_File.addSeparator()
        self.tb_File.addAction(self.a_ImportEtabs)
        self.tb_Define.addAction(self.a_GeneralInfor)
        self.tb_Define.addSeparator()
        self.tb_Define.addAction(self.a_MaterialProp)
        self.tb_Define.addAction(self.a_BarSet)
        self.tb_Define.addSeparator()
        self.tb_Define.addAction(self.a_Groups)
        self.tb_Define.addAction(self.a_Cases)
        self.tb_Analyze.addAction(self.actionDesign_Combos_Selection)
        self.tb_Analyze.addAction(self.a_GetAllForce)
        self.tb_Analyze.addSeparator()
        self.tb_Analyze.addAction(self.a_MakeSPcolumn)
        self.tb_Analyze.addAction(self.a_BatchProcessor)
        self.tb_Help.addAction(self.a_Doc)
        self.tb_Help.addAction(self.a_About)

        self.retranslateUi(mw_Main)

        QMetaObject.connectSlotsByName(mw_Main)
    # setupUi

    def retranslateUi(self, mw_Main):
        mw_Main.setWindowTitle(QCoreApplication.translate("mw_Main", u"SP-editor", None))
        self.action_New.setText(QCoreApplication.translate("mw_Main", u"&New", None))
#if QT_CONFIG(shortcut)
        self.action_New.setShortcut(QCoreApplication.translate("mw_Main", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.action_Open.setText(QCoreApplication.translate("mw_Main", u"&Open", None))
#if QT_CONFIG(shortcut)
        self.action_Open.setShortcut(QCoreApplication.translate("mw_Main", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.action_Save.setText(QCoreApplication.translate("mw_Main", u"&Save", None))
#if QT_CONFIG(shortcut)
        self.action_Save.setShortcut(QCoreApplication.translate("mw_Main", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_Quit.setText(QCoreApplication.translate("mw_Main", u"&Quit", None))
#if QT_CONFIG(shortcut)
        self.action_Quit.setShortcut(QCoreApplication.translate("mw_Main", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.a_GeneralInfor.setText(QCoreApplication.translate("mw_Main", u"&General Information", None))
        self.a_Groups.setText(QCoreApplication.translate("mw_Main", u"&Groups", None))
#if QT_CONFIG(shortcut)
        self.a_Groups.setShortcut(QCoreApplication.translate("mw_Main", u"Ctrl+G", None))
#endif // QT_CONFIG(shortcut)
        self.a_Cases.setText(QCoreApplication.translate("mw_Main", u"Load Cases", None))
        self.a_GetAllForce.setText(QCoreApplication.translate("mw_Main", u"Get Forces", None))
        self.a_MakeSPcolumn.setText(QCoreApplication.translate("mw_Main", u"Generate SpCol Files", None))
        self.a_BatchProcessor.setText(QCoreApplication.translate("mw_Main", u"Batch Processor", None))
        self.a_Doc.setText(QCoreApplication.translate("mw_Main", u"Documentation", None))
#if QT_CONFIG(shortcut)
        self.a_Doc.setShortcut(QCoreApplication.translate("mw_Main", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.a_About.setText(QCoreApplication.translate("mw_Main", u"About SP-editor", None))
        self.a_ImportEtabs.setText(QCoreApplication.translate("mw_Main", u"Import", None))
#if QT_CONFIG(shortcut)
        self.a_ImportEtabs.setShortcut(QCoreApplication.translate("mw_Main", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.a_Print.setText(QCoreApplication.translate("mw_Main", u"Print", None))
#if QT_CONFIG(shortcut)
        self.a_Print.setShortcut(QCoreApplication.translate("mw_Main", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.a_MaterialProp.setText(QCoreApplication.translate("mw_Main", u"&Material Properties", None))
        self.a_BarSet.setText(QCoreApplication.translate("mw_Main", u"Bar Sets", None))
        self.actionDesign_Combos_Selection.setText(QCoreApplication.translate("mw_Main", u"Design Combos Selection", None))
        self.label.setText(QCoreApplication.translate("mw_Main", u"Group", None))
        self.lb_pierLabel.setText(QCoreApplication.translate("mw_Main", u"Name", None))
        self.menu_File.setTitle(QCoreApplication.translate("mw_Main", u"&File", None))
        self.m_Define.setTitle(QCoreApplication.translate("mw_Main", u"&Define", None))
        self.m_Analyze.setTitle(QCoreApplication.translate("mw_Main", u"Analyze", None))
        self.menuHelp.setTitle(QCoreApplication.translate("mw_Main", u"Help", None))
        self.tb_File.setWindowTitle(QCoreApplication.translate("mw_Main", u"File", None))
        self.tb_Define.setWindowTitle(QCoreApplication.translate("mw_Main", u"Define", None))
        self.tb_Analyze.setWindowTitle(QCoreApplication.translate("mw_Main", u"Analyze", None))
        self.tb_Help.setWindowTitle(QCoreApplication.translate("mw_Main", u"Help", None))
    # retranslateUi

