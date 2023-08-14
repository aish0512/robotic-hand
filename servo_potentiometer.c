
#include <Servo.h> //accesses the Arduino Servo Library

Servo myservo1;
Servo myservo2;  // creates servo object to control a servo
Servo myservo3;
Servo myservo4;
Servo myservo5;

int val1;
int val2;
int val3;
int val4;  
int val5;   // variable to read the value from the analog pin

void setup()
{
  Serial.begin(9600);
  myservo1.attach(13);
  myservo2.attach(12);
  myservo3.attach(11);
  myservo4.attach(10);
  myservo5.attach(9);

    // ensures output to servo on pin 9
}

void loop() 
{ 
  val1 = analogRead(1);            // reads the value of the potentiometer from A1 (value between 0 and 1023) 
  val1 = map(val1, 0, 1023, 0, 180);     // converts reading from potentiometer to an output value in degrees of rotation that the servo can understand 
  myservo1.write(val1);
  //Serial.print("val1");      
  //Serial.println(val1);            // sets the servo position according to the input from the potentiometer 
  delay(15);
  
  val2 = analogRead(2);            // reads the value of the potentiometer from A1 (value between 0 and 1023) 
  val2 = map(val2, 0, 1023, 0, 180);     // converts reading from potentiometer to an output value in degrees of rotation that the servo can understand 
  myservo2.write(val2);
  //Serial.print("val2");      
  //Serial.println(val2);            // sets the servo position according to the input from the potentiometer 
  delay(15);

  val3 = analogRead(3);            // reads the value of the potentiometer from A1 (value between 0 and 1023) 
  val3 = map(val3, 0, 1023, 0, 180);     // converts reading from potentiometer to an output value in degrees of rotation that the servo can understand 
  myservo3.write(val3);
  //Serial.print("val3");      
  //Serial.println(val3);            // sets the servo position according to the input from the potentiometer 
  delay(15);
  
  
  val4 = analogRead(4);            // reads the value of the potentiometer from A1 (value between 0 and 1023) 
  val4 = map(val4, 0, 1023, 0, 180);     // converts reading from potentiometer to an output value in degrees of rotation that the servo can understand 
  myservo4.write(val4);
  //Serial.print("val4");      
  //Serial.println(val4);            // sets the servo position according to the input from the potentiometer 
  delay(15);
  

  val5 = analogRead(5);            // reads the value of the potentiometer from A1 (value between 0 and 1023) 
  val5 = map(val5, 0, 1023, 0, 180);     // converts reading from potentiometer to an output value in degrees of rotation that the servo can understand 
  myservo5.write(val5);
  //Serial.print("val5");      
  //Serial.println(val5);            // sets the servo position according to the input from the potentiometer 
  delay(15);
                           // waits 15ms for the servo to get to set position  
} 

