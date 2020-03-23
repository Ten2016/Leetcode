#include "widget.h"
#include "ui_widget.h"

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
    , curPath("/home/jialu/Documents/GitPro/Leetcode/新的起点")
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

bool Widget::Findque()
{
    QDir dir;
    dir.setPath(curPath);
    if (!dir.exists()){
        ui->textBrowser_3->clear();
        ui->textBrowser_3->setText("dir error...");
        ui->textBrowser_3->show();
        return false;
    }
    QList<QString> queue;
    queList.clear();
    queue.push_back(dir.path());
    while(!queue.empty()){
        dir.setPath(queue.front());
        queue.pop_front();
        dir.setFilter(QDir::Dirs|QDir::Files|QDir::NoSymLinks|QDir::NoDotAndDotDot);
        QFileInfoList list = dir.entryInfoList();
        for(int i=0; i<list.size(); ++i){
            QFileInfo fileinfo = list[i];
            QString filename=fileinfo.fileName();
            if(fileinfo.isDir()) //if it is dir
                queue.push_back(fileinfo.filePath());
            else if(filename.contains(queName))
                queList.push_back(fileinfo.filePath());
        }
    }
    if(queList.size()==0)
        return false;
    else
        return true;
}

void Widget::Showquelist()
{
    ui->textBrowser_3->clear();
    QString filename, tmpstr;
    queListIndex=0;
    for(int i=0; i<queList.size(); ++i){
        filename = queList[i];
        int tmpint=filename.lastIndexOf('/');
        tmpstr = filename.left(tmpint);
        tmpint = filename.size()-tmpint;
        tmpint += tmpstr.size()-tmpstr.lastIndexOf('/');
        ui->textBrowser_3->append(filename.right(tmpint));
    }
    ui->textBrowser_3->show();
}


void Widget::Showque()
{
    QString quename=queList[queListIndex];
    ui->label_3->setText(quename);
    ui->label_3->show();
    QFile fp(quename);
    if(!fp.open(QIODevice::ReadOnly)){
        ui->textBrowser_1->show();
        ui->textBrowser_1->setText("question "+quename+" open error...");
        ui->textBrowser_1->show();
        return;
    }
    QTextStream filestream(&fp);
    QString str;
    ui->textBrowser_1->clear();
    while (!filestream.atEnd()){
        str=filestream.readLine();
        if(str.startsWith("解法"))
            break;
        ui->textBrowser_1->append(str);
    }
    ui->textBrowser_1->show();
    ui->textBrowser_2->clear();
    while (!filestream.atEnd()){
        str=filestream.readLine();
        ui->textBrowser_2->append(str);
    }
    ui->textBrowser_2->show();
    fp.close();
}


void Widget::on_pushButton_clicked()    //que name
{
    queName = ui->lineEdit->text();
    if(queName==""){
        ui->textBrowser_3->clear();
        ui->textBrowser_3->setText("please input question name...");
        ui->textBrowser_3->show();
        return;
    }
    if(Findque()==false){
        ui->textBrowser_3->clear();
        ui->textBrowser_3->setText("question "+queName+" not found...");
        ui->textBrowser_3->show();
        return;
    }
    Showquelist();
    Showque();
}

void Widget::on_pushButton_2_clicked()  //curr dir
{
    curPath = ui->lineEdit_2->text();
}



void Widget::on_comboBox_currentIndexChanged(int index)
{
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
        ui->textBrowser_3->clear();
        ui->textBrowser_3->setText("dir error...");
        ui->textBrowser_3->show();
        return;
    }
    QList<QString> queue;
    queList.clear();
    queue.push_back(dir.path());
    while(!queue.empty()){
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
                for(int j=0; j<list.size(); ++j){
                    fileinfo = list[j];
                    queList.push_back(fileinfo.filePath());
                }
                goto FINDOK;
            }
            else
                queue.push_back(fileinfo.filePath());
        }
    }
    return;
    FINDOK:
    Showquelist();
    Showque();
}


void Widget::on_pushButton_3_clicked()      //random
{

}

void Widget::on_pushButton_4_clicked()      //before
{
    if(queList.size()==0)
        return;
    if(queListIndex>0)
        --queListIndex;
    Showque();

}

void Widget::on_pushButton_5_clicked()      //next
{
    if(queList.size()==0)
        return;
    if(queListIndex<queList.size()-1)
        ++queListIndex;
    Showque();
}
