#include <SoftwareSerial.h>       //Software Serial library
SoftwareSerial espSerial(2, 3);   //Pin 2 and 3 act as RX and TX. Connect them to TX and RX of ESP8266      
#define DEBUG true
#define moisture_pin A0
String mySSID = "Oozma Kappa";       // WiFi SSID
String myPWD = "1004packard"; // WiFi Password
String myAPI = "yeee";   // API Key
String myHOST = "api.thingspeak.com";
String myPORT = "80";
String myFIELD = "field1"; 




void setup()
{
  Serial.begin(9600);
  espSerial.begin(115200);
  
  espData("AT+RST", 1000, DEBUG);                      //Reset the ESP8266 module
  espData("AT+CWMODE=1", 1000, DEBUG);                 //Set the ESP mode as station mode
  espData("AT+CWJAP=\""+ mySSID +"\",\""+ myPWD +"\"", 1000, DEBUG);   //Connect to WiFi network
  /*while(!esp.find("OK")) 
  {          
      //Wait for connection
  }*/
  delay(1000);
  
}

  void loop()
  {
    /* Here, I'm using the function random(range) to send a random value to the 
     ThingSpeak API. You can change this value to any sensor data
     so that the API will show the sensor data  
    */
    
    int moisture_val = get_moisture(moisture_pin);
    send_data(moisture_val);
    delay(5000);
    
  }

  String espData(String command, const int timeout, boolean debug)
{
  Serial.print("AT Command ==> ");
  Serial.print(command);
  Serial.println("     ");
  
  String response = "";
  espSerial.println(command);
  long int time = millis();
  while ( (time + timeout) > millis())
  {
    while (espSerial.available())
    {
      char c = espSerial.read();
      response += c;
    }
  }
  if (debug)
  {
    //Serial.print(response);
  }
  return response;
}

void send_data(int data){
    //int sendVal = random(1000); // Send a random number between 1 and 1000
    String sendData = "GET /update?api_key="+ myAPI +"&"+ myFIELD +"="+String(data);
    espData("AT+CIPMUX=1", 1000, DEBUG);       //Allow multiple connections
    espData("AT+CIPSTART=0,\"TCP\",\""+ myHOST +"\","+ myPORT, 1000, DEBUG);
    espData("AT+CIPSEND=0," +String(sendData.length()+4),1000,DEBUG);  
    espSerial.find(">"); 
    espSerial.println(sendData);
    Serial.print("Value to be sent: ");
    Serial.println(data);
     
    espData("AT+CIPCLOSE=0",1000,DEBUG);
    delay(10000);
}

int get_moisture(int pin){
  int data_size =500;
  double sum=0;
  int data[data_size];
  for (int x =0; x<data_size; ++x){
      data[x]=analogRead(moisture_pin);  
  }//for x
  for (int z =0; z<data_size; ++z){
    sum+=data[z];
  }
  return sum/data_size;
}
