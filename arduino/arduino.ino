const int r1 = 2; 
const int r2 = 3; 
const int r3 = 4; 
const int r4 = 5; 

void setup() {
  Serial.begin(9600);
  pinMode(r1, OUTPUT);
  pinMode(r2, OUTPUT);
  pinMode(r3, OUTPUT);
  pinMode(r4, OUTPUT);
  digitalWrite(r1, HIGH);
  digitalWrite(r2, HIGH);
  digitalWrite(r3, HIGH);
  digitalWrite(r4, HIGH);
}
bool r1status = true;
bool r2status = true;
bool r3status = true;
bool r4status = true;
void loop() {
  
  if (Serial.available()) {
    String gesture = Serial.readStringUntil('\n');
    processGesture(gesture);
  }
  
//  digitalWrite(r1, LOW);
//  delay(1000);
//  digitalWrite(r2, LOW);
//  delay(1000);
//  digitalWrite(r3, LOW);
//  delay(1000);
//  digitalWrite(r4, LOW);
//  delay(1000);
  
}

void processGesture(String gesture) {
  if (gesture == "thumbs up") {
    if( r1status == false){ 
      digitalWrite(r1, HIGH); 
      r1status = true;
    }
    else if( r1status == true){
      r1status = false;
      digitalWrite(r1, LOW);  
    }
  } else if (gesture == "thumbs down") {
    if( r2status == false){ 
      digitalWrite(r2, HIGH); 
      r2status = true;
    }
    else if( r2status == true){
      r2status = false;
      digitalWrite(r2, LOW);  
    }
  } else if (gesture == "rock") {
    if( r3status == false){ 
      digitalWrite(r3, HIGH); 
      r3status = true;
    }
    else if( r3status == true){
      r3status = false;
      digitalWrite(r3, LOW);  
    }
  } else if (gesture == "live long") {
    if( r4status == false){ 
      digitalWrite(r4, HIGH); 
      r4status = true;
    }
    else if( r4status == true){
      r4status = false;
      digitalWrite(r4, LOW);  
    }
  }
//  delay(5000);
}
