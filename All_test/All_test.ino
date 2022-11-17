#include <Servo.h>
Servo servox;
Servo servoy;

const int trigPin = 2;
const int echoPin = 3;

float duration, distance;
int posx=1100;
int posy=1100;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);

  servox.attach(10);
  servoy.attach(7);
}

void ultrasound() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = (duration*.0343)/2;
  Serial.print("Distance: ");
  Serial.println(distance);
  delay(100);
}

void printPos(){
  Serial.print("(posx, posy) = (");
  Serial.print(posx);
  Serial.print(", ");
  Serial.print(posy);
  Serial.println(")");
}

void loop() {
  servox.writeMicroseconds(1100);
  servoy.writeMicroseconds(1100);
  delay(5000);
  
  for (posy=1100; posy<1900; posy+=200) {
    servoy.writeMicroseconds(posy);
    
    if (posx==1100) {
      for (posx=1100; posx<1900; posx+=200) {
        servox.writeMicroseconds(posx);
        delay(3000);
        printPos();
        ultrasound();
      }

    } else if (posx == 1900){
      for (posx=1900; posx>1100; posx-=200) {
        servox.writeMicroseconds(posx);
        delay(3000);       
        printPos();
        ultrasound();
      }
    }
  }

  servoy.detach();
  servox.detach();
}
