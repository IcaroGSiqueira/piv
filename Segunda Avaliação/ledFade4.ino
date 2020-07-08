/*
 Fade
 
 This example shows how to fade an LED on all pwm pins
 using the analogWrite() function.
 
 This example code is in the public domain.
 */
int led[]        = { 6, 9, 10, 11 };    // the pin that the LED is attached to

// the setup routine runs once when you press reset:
void setup()  { 
  //INICIALIZA A SERIAL
  Serial.begin(9600);
} 

// the loop routine runs over and over again forever:
void loop()  { 

  if (Serial.available() > 0){

    if (Serial.read() == 97){

	  for( int i=0; i<4; i++ ){
	  	for (int fadeValue = 0 ; fadeValue <= 255; fadeValue += 5) {
		    // sets the value (range from 0 to 255):
		    analogWrite(led[i], fadeValue);
		    // wait for 30 milliseconds to see the dimming effect
		    delay(10);
		}
	  }
	  for (int fadeValue = 255 ; fadeValue >= 0; fadeValue -= 5) {
	    // sets the value (range from 0 to 255):
	    analogWrite(led[0], fadeValue);
		analogWrite(led[1], fadeValue);
		analogWrite(led[2], fadeValue);
		analogWrite(led[3], fadeValue);
	  }
	}
  }

  if (Serial.available() > 0){	
    if (Serial.read() == 98){

	  for( int i=3; i>=0; i-- ){
	  	for (int fadeValue = 0 ; fadeValue <= 255; fadeValue += 5) {
		    // sets the value (range from 0 to 255):
		    analogWrite(led[i], fadeValue);
		    // wait for 30 milliseconds to see the dimming effect
		    delay(10);
		}
	  }
	  for (int fadeValue = 255 ; fadeValue >= 0; fadeValue -= 5) {
	    // sets the value (range from 0 to 255):
	    analogWrite(led[0], fadeValue);
		analogWrite(led[1], fadeValue);
		analogWrite(led[2], fadeValue);
		analogWrite(led[3], fadeValue);
	  }
	}
  }
}
