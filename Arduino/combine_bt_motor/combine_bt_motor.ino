#define input1 9//左
#define input2 8//左
#define input3 5//右
#define input4 6//右
#define input5 7//左
#define input6 4//左
#define input7 2//右
#define input8 3//右
#include <SoftwareSerial.h>          //库文件
SoftwareSerial BT(10,11);           //设置蓝牙与板子的连接端口。  pin 10  接蓝牙的 TXD    pin 11 接蓝牙的 RXD
char X;                              //定义一个变量存数据。
char Y;

void backward()//
{
  analogWrite(input1,255);
  analogWrite(input2,0);
  analogWrite(input3,255);
  analogWrite(input4,0);
  analogWrite(input5,255);
  analogWrite(input6,0);
  analogWrite(input7,255);
  analogWrite(input8,0);
  delay(10);
}

void forward()//
{
  analogWrite(input1,0);
  analogWrite(input2,255);
  analogWrite(input3,0);
  analogWrite(input4,255);
  analogWrite(input5,0);
  analogWrite(input6,255);
  analogWrite(input7,0);
  analogWrite(input8,255);
  delay(10);
}

void turnright()//left拉满
{
 analogWrite(input1,0);
 analogWrite(input2,255);
 analogWrite(input3,255);
 analogWrite(input4,0); 
 analogWrite(input5,255);
 analogWrite(input6,0);
 analogWrite(input7,0);
 analogWrite(input8,255);
 delay(10);
}
void turnleft()//right拉满
{
 analogWrite(input1,255);
 analogWrite(input2,0);
 analogWrite(input3,0);
 analogWrite(input4,255); 
 analogWrite(input5,0);
 analogWrite(input6,255);
 analogWrite(input7,255);
 analogWrite(input8,0);
 delay(10);
}

void stop()
{
 analogWrite(input1,0);
 analogWrite(input2,0);
 analogWrite(input3,0);
 analogWrite(input4,0); 
 analogWrite(input5,0);
 analogWrite(input6,0);
 analogWrite(input7,0);
 analogWrite(input8,0);
 delay(10);
}

void setup() {
  // put your setup code here, to run once:

  pinMode(input1,OUTPUT);
  pinMode(input2,OUTPUT);
  pinMode(input3,OUTPUT);
  pinMode(input4,OUTPUT);  
  pinMode(input5,OUTPUT);
  pinMode(input6,OUTPUT);
  pinMode(input7,OUTPUT);
  pinMode(input8,OUTPUT);
  Serial.begin(38400);              //串口监视器通信速率，38400
  Serial.println("蓝牙连接正常");     //串口监视器显示蓝牙正常状态

  BT.begin(38400);                  //蓝牙通信速率，默认一般为 38400
  
 
}



void loop()                         //大循环，执行。
{
 if (Serial.available())           //检测：【串口】如果数据写入，则执行。
  {
    Y = Serial.read();              //把写入的数据给到自定义变量  Y
    BT.print(Y);                    //把数据给蓝牙
  }

  if (BT.available())               //检测：【蓝牙】如果数据写入，则执行。
  {
    X = BT.read();                  //把检测到的数据给到自定义变量 X
    Serial.print(X);                //把从蓝牙得到的数据显示到串口监视器
    
    if (X== 'G')
    {
    forward();
   
    BT.print("forward");
    }

    if (X== 'H')
    {
    turnleft();

    BT.print("turnleft");
    }

    if (X== 'I')
    {
    stop();
 
    BT.print("stop");
    }

    if (X== 'J')
    {
    turnright();
   
    BT.print("turnright");
    }
  }


    if (X== 'K')
    {
    backward();
  
    BT.print("backward");
    }
}


