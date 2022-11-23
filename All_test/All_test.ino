#include <Servo.h>
Servo servo_y;
Servo servo_x;

const int trigPin = 2;
const int echoPin = 3;

float duration, distance;
int pos_y=1100;
int pos_x=1100;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);

  servo_y.attach(10);
  servo_x.attach(7);
}

void printPos(){
//  Serial.print("(x,y,z) -> ");
  Serial.print(pos_x);
  Serial.print(", ");
  Serial.print(pos_y);
  Serial.print(", ");
  Serial.println(distance);
}

void ultrasound() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = (duration*.0343)/2;
  printPos();
  delay(100);
}

void loop() {
  servo_y.writeMicroseconds(1100);
  servo_x.writeMicroseconds(1100);
  delay(5000);
  
  for (pos_x=1100; pos_x<=1900; pos_x+=100) {
    servo_x.writeMicroseconds(pos_x);
    
    if (pos_y==1100) {
      for (pos_y=1100; pos_y<=1900; pos_y+=100) {
        servo_y.writeMicroseconds(pos_y);
        
        delay(500);
        ultrasound();
        ultrasound();
        ultrasound();
        ultrasound();
        ultrasound();
      }
      pos_y-=100;

    } else if (pos_y == 1900){
      for (pos_y=1900; pos_y>=1100; pos_y-=100) {
        servo_y.writeMicroseconds(pos_y);
        delay(500);
        ultrasound();
        ultrasound();
        ultrasound();
        ultrasound();
        ultrasound();
      }
      pos_y+=100;
    }
  }

  servo_x.detach();
  servo_y.detach();
  pos_y=0;
}
