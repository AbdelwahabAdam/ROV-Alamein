// C++ code
//
void setup()
{
  pinMode(3, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
}

void loop()
{
  analogWrite(3, 255);
  analogWrite(5, 0);
  analogWrite(9, 0);
  delay(500); // Wait for 500 millisecond(s)
  analogWrite(10, 255);
  delay(250); // Wait for 250 millisecond(s)
  analogWrite(10, 0);
  delay(250); // Wait for 250 millisecond(s)
  analogWrite(3, 0);
  analogWrite(9, 0);
  analogWrite(5, 255);
  delay(500); // Wait for 500 millisecond(s)
  analogWrite(10, 255);
  delay(250); // Wait for 250 millisecond(s)
  analogWrite(10, 0);
  delay(250); // Wait for 250 millisecond(s)
  analogWrite(5, 0);
  analogWrite(3, 0);
  analogWrite(9, 255);
  delay(500); // Wait for 500 millisecond(s)
  analogWrite(10, 255);
  delay(250); // Wait for 250 millisecond(s)
  analogWrite(10, 0);
  delay(250); // Wait for 250 millisecond(s)
  analogWrite(3, 50);
  analogWrite(5, 100);
  analogWrite(9, 50);
  delay(500); // Wait for 500 millisecond(s)
  analogWrite(10, 255);
  delay(250); // Wait for 250 millisecond(s)
  analogWrite(10, 0);
  delay(250); // Wait for 250 millisecond(s)
  analogWrite(3, 150);
  analogWrite(5, 200);
  analogWrite(9, 0);
  delay(500); // Wait for 500 millisecond(s)
  analogWrite(10, 255);
  delay(250); // Wait for 250 millisecond(s)
  analogWrite(10, 0);
  delay(250); // Wait for 250 millisecond(s)
  analogWrite(3, 0);
  analogWrite(5, 150);
  analogWrite(9, 200);
  delay(500); // Wait for 500 millisecond(s)
  analogWrite(10, 255);
  delay(250); // Wait for 250 millisecond(s)
  analogWrite(10, 0);
  delay(250); // Wait for 250 millisecond(s)
  analogWrite(3, 0);
  analogWrite(5, 0);
  analogWrite(9, 0);
  delay(5000); // Wait for 5000 millisecond(s)
}