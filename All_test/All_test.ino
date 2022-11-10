#include <Servo.h>
Servo myservo;

const int trigPin = 2;
const int echoPin = 3;

float duration, distance;
int posx=0;
int posy=0;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);

  myservo.attach(5);
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

void loop() {
  for(posy=0; posy<=179; posy++){
    for (posx = 0; posx <= 180; posx += 1) { // goes from 0 degrees to 180 degrees
      // in steps of 1 degree
      myservo.write(posx);              // tell servo to go to position in variable 'pos'
      ultrasound();
//      delay(30);                       // waits 15ms for the servo to reach the position
    }
    posy++;
    for (posx = 180; posx >=0; posx--) {
      myservo.write(posx);              // tell servo to go to position in variable 'pos'
      ultrasound();
//      delay(30);
    }
  }
}
