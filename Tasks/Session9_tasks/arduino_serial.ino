#define LED1 2
#define LED2 3
#define LED3 4
#define LED4 5

String inputString = "";
boolean receiving = false;

void setup() {
  Serial.begin(9600);

  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
  pinMode(LED4, OUTPUT);
}

void loop() {
  while (Serial.available()) {
    char c = Serial.read();

    if (c == '*') {       // start of frame
      inputString = "";
      receiving = true;
    }
    else if (c == '#') {  // end of frame
      receiving = false;
      parseFrame(inputString);
    }
    else if (receiving) {
      inputString += c;
    }
  }
}

void parseFrame(String frame) {
  // Split into 4 parts
  int leds[4];
  int idx = 0;

  while (frame.length() > 0 && idx < 4) {
    int commaIndex = frame.indexOf(',');
    String value;

    if (commaIndex == -1) {
      value = frame;
      frame = "";
    } else {
      value = frame.substring(0, commaIndex);
      frame = frame.substring(commaIndex + 1);
    }

    leds[idx++] = value.toInt();
  }

  // Apply LED states
  if (idx == 4) {
    digitalWrite(LED1, leds[0]);
    digitalWrite(LED2, leds[1]);
    digitalWrite(LED3, leds[2]);
    digitalWrite(LED4, leds[3]);

    Serial.print("Parsed: ");
    for (int i = 0; i < 4; i++) {
      Serial.print(leds[i]);
      Serial.print(" ");
    }
    Serial.println();
  }
}