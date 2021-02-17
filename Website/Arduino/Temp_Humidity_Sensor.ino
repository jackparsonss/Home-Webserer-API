#include<LiquidCrystal.h>
#include<DHT.h>
#define Type DHT11

int echoPin = 6;
int trigPin = 4;
int travelTime;

int sensorPin = 2;
int btnPin = 5;
int btnVal;
bool celsius = true;

int rs = 7;
int en = 8;
int d4 = 9;
int d5 = 10;
int d6 = 11;
int d7 = 12;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

DHT HT(sensorPin, Type);
float humidity;
float temp;

void setup() {
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(btnPin, INPUT);
  digitalWrite(btnPin, HIGH);
  HT.begin();
  lcd.begin(16, 2);
  lcd.print("Temp: ");
  lcd.setCursor(0,1);
  lcd.print("Humidity: ");
}

void loop() {
  delay(250);
  temp = HT.readTemperature();
  Serial.println(temp);
  humidity=HT.readHumidity();
  Serial.println(humidity);

  
  getTravelTime();
  
  if(travelTime > 3500){
    lcd.clear();
  }else{
    printHumidity();
    btnVal = digitalRead(btnPin);
    if(btnVal == 0){
      celsius = !celsius;
      //delay(500);
    }
    if(celsius){
      printTempC();
    }else{
      printTempF();
    }
  }
 }
  
void printHumidity(){
  lcd.setCursor(0,1);
  lcd.print("Humidity: ");
  lcd.setCursor(9,1);
  humidity=HT.readHumidity();
  lcd.print(humidity);
  lcd.setCursor(14,1);
  lcd.print("%");
}

void printTempC(){
  lcd.setCursor(0, 0);
  lcd.print("Temp: ");
  temp = HT.readTemperature();
  lcd.setCursor(5,0);
  lcd.print(temp);
  lcd.setCursor(10,0);
  lcd.print("C");  
}

void printTempF(){
  lcd.setCursor(0, 0);
  lcd.print("Temp: ");
  temp = HT.readTemperature(true);
  lcd.setCursor(5,0);
  lcd.print(temp);
  lcd.setCursor(10,0);
  lcd.print("F");  
}

void getTravelTime(){
  digitalWrite(trigPin, LOW);
  delayMicroseconds(10);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  travelTime = pulseIn(echoPin, HIGH);  
}
