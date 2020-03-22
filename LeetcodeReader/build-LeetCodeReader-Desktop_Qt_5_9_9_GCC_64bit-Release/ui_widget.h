/********************************************************************************
** Form generated from reading UI file 'widget.ui'
**
** Created by: Qt User Interface Compiler version 5.9.9
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_WIDGET_H
#define UI_WIDGET_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QTextBrowser>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Widget
{
public:
    QLabel *label;
    QLabel *label_2;
    QTextBrowser *textBrowser_1;
    QTextBrowser *textBrowser_2;
    QLineEdit *lineEdit;
    QPushButton *pushButton;
    QComboBox *comboBox;
    QTextBrowser *textBrowser_3;
    QPushButton *pushButton_2;
    QLineEdit *lineEdit_2;
    QLabel *label_3;

    void setupUi(QWidget *Widget)
    {
        if (Widget->objectName().isEmpty())
            Widget->setObjectName(QStringLiteral("Widget"));
        Widget->resize(1400, 600);
        label = new QLabel(Widget);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(340, 20, 54, 17));
        label_2 = new QLabel(Widget);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setGeometry(QRect(1100, 20, 54, 17));
        textBrowser_1 = new QTextBrowser(Widget);
        textBrowser_1->setObjectName(QStringLiteral("textBrowser_1"));
        textBrowser_1->setGeometry(QRect(340, 40, 500, 440));
        textBrowser_2 = new QTextBrowser(Widget);
        textBrowser_2->setObjectName(QStringLiteral("textBrowser_2"));
        textBrowser_2->setGeometry(QRect(870, 40, 500, 440));
        lineEdit = new QLineEdit(Widget);
        lineEdit->setObjectName(QStringLiteral("lineEdit"));
        lineEdit->setGeometry(QRect(20, 80, 211, 25));
        pushButton = new QPushButton(Widget);
        pushButton->setObjectName(QStringLiteral("pushButton"));
        pushButton->setGeometry(QRect(240, 80, 70, 25));
        comboBox = new QComboBox(Widget);
        comboBox->setObjectName(QStringLiteral("comboBox"));
        comboBox->setGeometry(QRect(20, 130, 151, 25));
        textBrowser_3 = new QTextBrowser(Widget);
        textBrowser_3->setObjectName(QStringLiteral("textBrowser_3"));
        textBrowser_3->setGeometry(QRect(20, 180, 291, 301));
        pushButton_2 = new QPushButton(Widget);
        pushButton_2->setObjectName(QStringLiteral("pushButton_2"));
        pushButton_2->setGeometry(QRect(240, 40, 70, 25));
        lineEdit_2 = new QLineEdit(Widget);
        lineEdit_2->setObjectName(QStringLiteral("lineEdit_2"));
        lineEdit_2->setGeometry(QRect(20, 40, 211, 25));
        label_3 = new QLabel(Widget);
        label_3->setObjectName(QStringLiteral("label_3"));
        label_3->setGeometry(QRect(410, 20, 620, 17));
        QWidget::setTabOrder(pushButton, lineEdit);
        QWidget::setTabOrder(lineEdit, textBrowser_1);
        QWidget::setTabOrder(textBrowser_1, comboBox);
        QWidget::setTabOrder(comboBox, textBrowser_3);
        QWidget::setTabOrder(textBrowser_3, pushButton_2);
        QWidget::setTabOrder(pushButton_2, lineEdit_2);
        QWidget::setTabOrder(lineEdit_2, textBrowser_2);

        retranslateUi(Widget);

        QMetaObject::connectSlotsByName(Widget);
    } // setupUi

    void retranslateUi(QWidget *Widget)
    {
        Widget->setWindowTitle(QApplication::translate("Widget", "Widget", Q_NULLPTR));
        label->setText(QApplication::translate("Widget", "question", Q_NULLPTR));
        label_2->setText(QApplication::translate("Widget", "answer", Q_NULLPTR));
        pushButton->setText(QApplication::translate("Widget", "quen num", Q_NULLPTR));
        comboBox->clear();
        comboBox->insertItems(0, QStringList()
         << QString()
         << QApplication::translate("Widget", "everyday one", Q_NULLPTR)
         << QApplication::translate("Widget", "stack", Q_NULLPTR)
         << QApplication::translate("Widget", "e", Q_NULLPTR)
         << QApplication::translate("Widget", "New Item", Q_NULLPTR)
        );
        pushButton_2->setText(QApplication::translate("Widget", "curr dir", Q_NULLPTR));
        label_3->setText(QApplication::translate("Widget", "TextLabel", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class Widget: public Ui_Widget {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_WIDGET_H
