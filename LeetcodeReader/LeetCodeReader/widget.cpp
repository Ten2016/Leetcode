#include "widget.h"
#include "ui_widget.h"

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
    , curPath("/home/jialu/Documents/GitPro/Leetcode")
{
    ui->setupUi(this);
    this->setWindowTitle("LeetcodeReader");
    this->setMaximumSize(1400,600);
    this->setMinimumSize(1400,600);
    this->move(50,50);
    this->setStyleSheet("background:white");
    ui->lineEdit_2->setText(curPath);
    ui->label_3->clear();
    ui->label_3->show();
}

Widget::~Widget()
{
    delete ui;
}


void Widget::on_pushButton_clicked()
{
    ui->textBrowser_3->clear();
    QString quenum = ui->lineEdit->text();
    if(quenum==""){
        ui->textBrowser_3->setText("please input question num...");
        ui->textBrowser_3->show();
        return;
    }
    QDir dir;
    dir.setPath(curPath);
    if (!dir.exists()){
        ui->textBrowser_3->setText("dir error...");
        ui->textBrowser_3->show();
        return;
    }
    bool findflag=false;
    QString quename;
    QList<QString> queue;
    queue.push_back(dir.path());
    while(!queue.empty()){
        QDir tmpdir;
        dir.setPath(queue.front());
        queue.pop_front();
        dir.setFilter(QDir::Dirs|QDir::Files|QDir::NoSymLinks|QDir::NoDotAndDotDot);
        QFileInfoList list = dir.entryInfoList();
        for(int i=0; i<list.size(); ++i){
            QFileInfo fileinfo = list[i];
            QString ts=fileinfo.fileName();
            if(fileinfo.isDir()){ //if it is dir
                queue.push_back(fileinfo.filePath());

            }
            else if(ts.startsWith(quenum)){
                ui->textBrowser_3->append(ts);
                if(findflag==false){
                    findflag=true;
                    quename=fileinfo.filePath();
                }
            }
        }
        ui->textBrowser_3->show();
    }
    if(findflag==true){
        ui->label_3->setText(quename);
        ui->label_3->show();
    }
    else{
        ui->textBrowser_3->setText("question "+quenum+" not found...");
        ui->textBrowser_3->show();
    }
}

void Widget::on_pushButton_2_clicked()
{
    curPath = ui->lineEdit_2->text();
}

void Widget::on_comboBox_currentIndexChanged(int index)
{
    ui->textBrowser_3->clear();
    ui->textBrowser_3->show();
    QString sortname;
    switch(index){
        case 1:  sortname="每日一题";   break;
        case 2:  sortname="栈";        break;
        default: break;
    }
    if(sortname=="")
        return;
    QDir dir;
    dir.setPath(curPath);
    if (!dir.exists()){
        ui->textBrowser_3->setText("dir error...");
        ui->textBrowser_3->show();
        return;
    }
    QList<QString> queue;
    queue.push_back(dir.path());
    while(!queue.empty()){
        QDir tmpdir;
        dir.setPath(queue.front());
        queue.pop_front();
        dir.setFilter(QDir::Dirs|QDir::NoSymLinks|QDir::NoDotAndDotDot);
        QFileInfoList list = dir.entryInfoList();
        for(int i=0; i<list.size(); ++i){
            QFileInfo fileinfo = list[i];
            if(fileinfo.fileName()==sortname){
                dir.setPath(fileinfo.filePath());
                dir.setFilter(QDir::Files|QDir::NoSymLinks|QDir::NoDotAndDotDot);
                list = dir.entryInfoList();
                for(int j=0; j<list.size(); ++j)
                    ui->textBrowser_3->append(list[j].fileName());
                ui->textBrowser_3->show();
                return;
            }
            else
                queue.push_back(fileinfo.filePath());
        }
    }
}

