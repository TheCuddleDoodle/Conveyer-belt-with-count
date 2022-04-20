int a = 7;
int count= 0;
void setup() { 
    pinMode(2,INPUT);
    pinMode(4,INPUT);
     pinMode(7,OUTPUT); 
     Serial.begin(9600); 
     }


 void loop() {
    if (digitalRead(2) == 1) {
         digitalWrite(a,1);
            Serial.println("Loading");
        if(digitalRead(4) == 1){
            digitalWrite(a,0);
            count++;
        Serial.println(count); 
            
        }
        
        


    }
        }