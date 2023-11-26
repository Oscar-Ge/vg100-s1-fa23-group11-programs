const int dirPin = 3;  // 方向引脚
const int stepPin = 5; // 步进引脚
 
// 电机每圈步数
const int STEPS_PER_REV = 200;
 
void setup() {
  
  // Arduino控制A4988步进和方向的引脚为输出模式
  pinMode(stepPin,OUTPUT); 
  pinMode(dirPin,OUTPUT);
}

void runStepper (int rotationSpeed, int stepNum){
  for(int x = 0; x < stepNum; x++) {
    digitalWrite(stepPin,HIGH); 
    delayMicroseconds(rotationSpeed); 
    digitalWrite(stepPin,LOW); 
    delayMicroseconds(rotationSpeed); 
  }  
}

void loop() {
  
  // 设置电机顺时针旋转
  digitalWrite(dirPin,LOW); 
  
  // 电机慢速旋转
  for(int x = 0; x < STEPS_PER_REV; x++) {
    digitalWrite(stepPin,HIGH); 
    delayMicroseconds(2000); 
    digitalWrite(stepPin,LOW); 
    delayMicroseconds(2000); 
  }
  
  // 等待一秒
  delay(1000); 
  
  // 设置电机逆时针旋转
  digitalWrite(dirPin,HIGH);
  
  // 电机快速旋转
  for(int x = 0; x < (STEPS_PER_REV * 2); x++) {
    digitalWrite(stepPin,HIGH);
    delayMicroseconds(1000);
    digitalWrite(stepPin,LOW);
    delayMicroseconds(1000);
  }
  
  // 等待一秒
  delay(1000);
}