int moisture_level = 0;
#define moisture_pin A0;




void setup() {
  Serial.begin(9600);
  // put your setup code here, to run once:

}

void loop() {

  moisture_level = analogRead(A0);
  delay(2);
  Serial.println(moisture_level);
 

  
  
  // put your main code here, to run repeatedly:

}
