int moisture_level = 0;
#define moisture_pin A0;




void setup() {
  Serial.begin(9600);
  vector<int> data_vector;
  // put your setup code here, to run once:

}

void loop() {
  
  for (int x =0; x<500; ++x){
  moisture_level = analogRead(A0);
  
  datta_vector.push_back(moisture_level)
  
  Serial.println(moisture_level);
  }
  Serial.println("finished");
  
  
  // put your main code here, to run repeatedly:

}
