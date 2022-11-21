const int echoPin = 5;
int pin = 3;

float duration, distance;

void setup() {
  pinMode(echoPin, INPUT);
  Serial.begin(9600);

  pinMode(pin, OUTPUT);
  
}

void loop() {
  tone(3, 16000);

  duration = pulseIn(echoPin, HIGH);
  distance = (duration*.0343)/2;
  Serial.print("Distance: ");
  Serial.println(distance);
  delay(100);
}
