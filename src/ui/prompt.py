# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/prompt.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PromptDialog(object):
    def setupUi(self, PromptDialog):
        PromptDialog.setObjectName("PromptDialog")
        PromptDialog.resize(481, 505)
        self.prompt_ok_btn = QtWidgets.QDialogButtonBox(PromptDialog)
        self.prompt_ok_btn.setGeometry(QtCore.QRect(110, 450, 341, 32))
        self.prompt_ok_btn.setOrientation(QtCore.Qt.Horizontal)
        self.prompt_ok_btn.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.prompt_ok_btn.setObjectName("prompt_ok_btn")
        self.prompt_text = QtWidgets.QLabel(PromptDialog)
        self.prompt_text.setGeometry(QtCore.QRect(30, 20, 431, 16))
        self.prompt_text.setObjectName("prompt_text")
        self.prompt_msg = QtWidgets.QTextBrowser(PromptDialog)
        self.prompt_msg.setGeometry(QtCore.QRect(20, 50, 441, 391))
        self.prompt_msg.setObjectName("prompt_msg")

        self.retranslateUi(PromptDialog)
        self.prompt_ok_btn.accepted.connect(PromptDialog.accept) # type: ignore
        self.prompt_ok_btn.rejected.connect(PromptDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(PromptDialog)

    def retranslateUi(self, PromptDialog):
        _translate = QtCore.QCoreApplication.translate
        PromptDialog.setWindowTitle(_translate("PromptDialog", "Error al hacer el filtro"))
        self.prompt_text.setText(_translate("PromptDialog", "Lo siento... no te pude hacer el filtro. Por favor revisá lo que pusiste. Python me dijo que:"))
        self.prompt_msg.setHtml(_translate("PromptDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
