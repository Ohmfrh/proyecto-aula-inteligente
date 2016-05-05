/*
  * Pin layout should be as follows (on Arduino Uno):  
  * MOSI: Pin 11
  * MISO: Pin 12 
  * SCK: Pin 13 
  * SS: Pin 8  
  * RST: Pin 3  
  * GREEN LED 6
  * RED LED 5
  * BLUE LED 2
  */ 

#include <SPI.h>
#include <WiFi.h>
#include <RFID.h> 

#define RST_PIN 3 //for RFID module
#define SelectRFID 8 //for stackability with the WiFi Shield
#define SelectWiFi 10
#define SelectSSD 4

#define GREEN_LED 6 //valid card
#define RED_LED 5 //invalid card
#define BLUE_LED 2 //show network activity

int serNum[5]; //for saving RFID values

// Network connection  
char ssid[] = "AulaInteligente"; //network name
char pass[] = "aulainteligente"; //network's password
int flag = 1; //for identifying a card read
int network_error = 0;
int count = 0;

int status = WL_IDLE_STATUS;

// Initialize the Wifi client library
WiFiClient client;

// Initialize RFID 
RFID rfid(SelectRFID,RST_PIN);

// Server address & port configuration
IPAddress server(192,168,1,200); //Modulo Central de Administracion
int port = 9090;

void setup() {
  // Initialize serial and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  // Port initializations
  // SS SPI ports must be LOW to be selected (one slave at a time)
  // If SS value is set to HIGH, slave sets MOSI and MISO pins to third state
  // We dissable all SPI slaves initially
  Serial.println("Initializing ports and SS lines");
  pinMode(SelectRFID,OUTPUT);
  digitalWrite(SelectRFID,HIGH); 
  pinMode(SelectWiFi,OUTPUT);
  digitalWrite(SelectWiFi,HIGH); 
  pinMode(SelectSSD,OUTPUT);
  digitalWrite(SelectSSD,HIGH);
  
  // LEDs (all turned off)
  Serial.println("Initializing LEDs");
  pinMode(GREEN_LED, OUTPUT);
  digitalWrite(GREEN_LED, LOW);
  pinMode(RED_LED, OUTPUT); 
  digitalWrite(RED_LED, LOW);
  pinMode(BLUE_LED, OUTPUT); 
  digitalWrite(BLUE_LED, LOW);

  // Enabling WiFi
  Serial.println("Enabling WiFi");
  digitalWrite(SelectWiFi,LOW); 
  
  // check for the presence of the shield:
  Serial.println("Verifying WiFi shield presence...");
  digitalWrite(RED_LED, HIGH);
  do {
    status = WiFi.status();
  } while (status == WL_NO_SHIELD);
  digitalWrite(RED_LED, LOW);
  status = WL_IDLE_STATUS;
  
  // Attempt to connect to Wifi network
  // Program does not continue until network connection has been established
  digitalWrite(BLUE_LED,HIGH);
  while (status != WL_CONNECTED) {
    Serial.print("Attempting to connect to SSID: ");
    Serial.println(ssid);
    status = WiFi.begin(ssid, pass);
  }
  
  // Connecting to server
  connect_to_server();
  
  //Initializing RFID
  Serial.println("Initializing RFID");
  rfid.init(); 
  
  Serial.println("Done initializing");
  digitalWrite(BLUE_LED,LOW);
  Serial.println("Waiting for card...");
//End of setup()
}

void loop() {
  String string = "";
  String temp = "";
  int i = 0;

  //Incoming data from server
  while (client.available()) {
    digitalWrite(BLUE_LED, LOW);
    char c = client.read();
    if (c == '1'){
      digitalWrite(GREEN_LED,HIGH);
      Serial.println("Access Granted");
    } 
    else {
      digitalWrite(RED_LED,HIGH);
      Serial.println("Access Denied");
    }
    delay(1500);
    digitalWrite(RED_LED,LOW);
    digitalWrite(GREEN_LED,LOW);
    flag = 1;
    count = 0;
    // Closing connection
    //client.stop();
    Serial.println("Waiting for card...");
    break;
  }

  //Enabling RFID
  digitalWrite(SelectWiFi, HIGH);
  digitalWrite(SelectRFID,LOW); 
  
  if (flag == 1) {
    flash();
  }

  if(flag == 1 && rfid.isCard()) { 
    //Card was detected 
    if(rfid.readCardSerial()) {  
      Serial.println("Card read");
      // RFID is dissabled after card is read by library functions; no need to turn off
      digitalWrite(BLUE_LED, HIGH);
      //Create ID string
      for (i = 0; i < 4; i++){
        temp = String(rfid.serNum[i],HEX);
        if (temp.length() == 1) temp = "0" + temp;
        string += temp;
      }
     Serial.println("Sending string: " + string);
     // Send request
     // WiFi enabling is done automatically by WiFi library on send commands
     sendIdToServer(string);
     flag = network_error;
    }
  }
  rfid.halt();  
//End of loop()
}

// Flash both LEDs to indicate system is waiting for card to read
// Flash three LEDs to indicate server connection is not established
int flash() {
  if (count == 75) {
    if (network_error) digitalWrite(BLUE_LED,HIGH);
    digitalWrite(RED_LED,HIGH);
    digitalWrite(GREEN_LED,HIGH);
    delay(100);
    digitalWrite(BLUE_LED,LOW);
    digitalWrite(RED_LED,LOW);
    digitalWrite(GREEN_LED,LOW);
    count = -1;
  }
  count ++;
}

// This method makes a connection to the server:
void sendIdToServer(String cardID) {
  client.flush();
  // checking for connexion
  if (connect_to_server() == 1) client.println(cardID);
}

// Connecting to server
int connect_to_server() {
  if (client.connected()) {
    Serial.println("Connection Verifed");
    network_error = 0;
    return 1;
  }
  Serial.println("Attempting to connect to server");
  if (client.connect(server, port)) {
    // Identifying with the server
    client.println("module=RFID");
    Serial.println("Connection successfully established");
  }
  else {
    Serial.println("Connection with server failed");
    digitalWrite(RED_LED,HIGH);
    digitalWrite(GREEN_LED,HIGH);
    digitalWrite(BLUE_LED,HIGH);
    delay(1000);
    digitalWrite(RED_LED,LOW);
    digitalWrite(GREEN_LED,LOW);
    digitalWrite(BLUE_LED,LOW);
    network_error = 1;
    return 0;
  }
  network_error = 0;
  return 1;
}


