const int sensorPin = A0;
int sensorValue;

void setup() {
  Serial.begin(9600);
  Serial.println("time_ms,sensor_value");   // CSV header
}

void loop() {

  sensorValue = analogRead(sensorPin);

  Serial.print(millis());   // time
  Serial.print(",");
  Serial.println(sensorValue); // sensor reading

  delay(200);
}
