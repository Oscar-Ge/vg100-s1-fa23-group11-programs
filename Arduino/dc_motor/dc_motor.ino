#define input1 9//左
#define input2 10//左
#define input3 5//右
#define input4 6//右

void forward()//
{

 analogWrite(input3,127);
 analogWrite(input4,0);
 delay(10);
}
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  pinMode(input3,OUTPUT);
  pinMode(input4,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  forward();
  Serial.println("counterclockwise");
  delay(1000);
}
