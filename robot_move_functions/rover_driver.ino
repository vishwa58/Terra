#include "robot_move_functions.h"



void setup() 
{
 pinMode(enA,OUTPUT);
 pinMode(enB,OUTPUT);
 pinMode(in1,OUTPUT);
 pinMode(in2,OUTPUT);
 pinMode(in3,OUTPUT);
 pinMode(in4,OUTPUT);
  // Attach the Interrupts to their ISR's
  attachInterrupt(digitalPinToInterrupt (MOTOR_A), ISR_countA, RISING);  // Increase counter A when speed sensor pin goes High
  attachInterrupt(digitalPinToInterrupt (MOTOR_B), ISR_countB, RISING);  // Increase counter B when speed sensor pin goes High
  
  // Test Motor Movement  - Experiment with your own sequences here  
  
  MoveForward(CMtoSteps(50), 255);  // Forward half a metre at 255 speed
  delay(1000);  // Wait one second
//  MoveReverse(10, 255);  // Reverse 10 steps at 255 speed
//  delay(1000);  // Wait one second
//  MoveForward(10, 150);  // Forward 10 steps at 150 speed
//  delay(1000);  // Wait one second
//  MoveReverse(CMtoSteps(25.4), 200);  // Reverse 25.4 cm at 200 speed
//  delay(1000);  // Wait one second
//  SpinRight(20, 255);  // Spin right 20 steps at 255 speed
//  delay(1000);  // Wait one second
//  SpinLeft(60, 175);  // Spin left 60 steps at 175 speed
//  delay(1000);  // Wait one second
//  MoveForward(1, 255);  // Forward 1 step at 255 speed
  
  
} 

void loop()
{
  // Put whatever you want here!

  
}
