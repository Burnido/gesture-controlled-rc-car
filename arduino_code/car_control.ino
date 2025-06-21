#include <SoftwareSerial.h>
SoftwareSerial BTSerial(3, 2); // RX, TX

int in1 = 8;
int in2 = 9;
int in3 = 10;
int in4 = 11;
int enA = 5;
int enB = 6;

void setup() {
  Serial.begin(9600);
  BTSerial.begin(9600);

  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);

  analogWrite(enA, 200);  // Adjust speed as needed
  analogWrite(enB, 200);

  Serial.println("Arduino Ready to Receive Bluetooth Commands");
}

void loop() {
  if (BTSerial.available()) {
    char cmd = BTSerial.read();
    Serial.print("Received: ");
    Serial.println(cmd);

    switch (cmd) {
      case 'F': moveForward(); Serial.println("→ Forward"); break;
      case 'B': moveBackward(); Serial.println("→ Backward"); break;
      case 'L': turnLeft(); Serial.println("→ Left"); break;
      case 'R': turnRight(); Serial.println("→ Right"); break;
      case 'S': stopCar(); Serial.println("→ Stop"); break;
    }
  }
}

void moveForward() {
  digitalWrite(in1, HIGH); digitalWrite(in2, LOW);
  digitalWrite(in3, HIGH); digitalWrite(in4, LOW);
}

void moveBackward() {
  digitalWrite(in1, LOW); digitalWrite(in2, HIGH);
  digitalWrite(in3, LOW); digitalWrite(in4, HIGH);
}

void turnLeft() {
  digitalWrite(in1, LOW); digitalWrite(in2, HIGH);
  digitalWrite(in3, HIGH); digitalWrite(in4, LOW);
}

void turnRight() {
  digitalWrite(in1, HIGH); digitalWrite(in2, LOW);
  digitalWrite(in3, LOW); digitalWrite(in4, HIGH);
}

void stopCar() {
  digitalWrite(in1, LOW); digitalWrite(in2, LOW);
  digitalWrite(in3, LOW); digitalWrite(in4, LOW);
}
