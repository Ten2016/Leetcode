#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include <QDir>
#include <QTextStream>

QT_BEGIN_NAMESPACE
namespace Ui { class Widget; }
QT_END_NAMESPACE

class Widget : public QWidget
{
    Q_OBJECT

public:
    Widget(QWidget *parent = nullptr);
    ~Widget();

private slots:
    void on_pushButton_clicked();

    void on_comboBox_currentIndexChanged(int index);

    void on_pushButton_2_clicked();

    void on_pushButton_3_clicked();

    void on_pushButton_4_clicked();

    void on_pushButton_5_clicked();

private:
    bool Findque(void);
    void Showquelist(void);
    void Showque(void);
    
private:
    Ui::Widget *ui;

    QString curPath;
    QString queName;
    QList<QString> queList;
    qint32 queListIndex;




};
#endif // WIDGET_H
