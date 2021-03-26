/*  
  Robot Car with Speed Sensor Demonstration
  RobotCarSpeedSensorDemo.ino
  Demonstrates use of Hardware Interrupts
  to control motors on Robot Car
  
  DroneBot Workshop 2017
  http://dronebotworkshop.com
*/

#ifndef ROBOT_MOVE_FUNCTIONS_H
#define ROBOT_MOVE_FUNCTIONS_H

// Constants for Interrupt Pins
// Change values if not using Arduino Uno
const byte MOTOR_A = 3;  // Motor 2 Interrupt Pin - INT 1 - Right Motor
const byte MOTOR_B = 2;  // Motor 1 Interrupt Pin - INT 0 - Left Motor

// Constant for steps in disk
const float stepcount = 20.00;  // 20 Slots in disk, change if different

// Constant for wheel diameter
const float wheeldiameter = 60; // Wheel diameter in millimeters, change if different

// Integers for pulse counters
volatile int counter_A = 0;
volatile int counter_B = 0;


// Motor A

int enA = 4;
int in1 = 42;
int in2 = 44;

// Motor B

int enB = 5;
int in3 = 46;
int in4 = 48;


//This the interrupt function for the first encoder
void ISR_countA() ;

//this is the interrupt function for the second encoder
void ISR_countB();

//This function takes in the distance the rover needs to move and converts it into steps
int CMtoSteps(float cm);

//This function takes in the total distance needed to travel and how many stops you want 
//and returns the distance it must travel each time
double grid_square_distance(float distance, int resolution);

//This function moves the robot forward
void MoveForward(int steps, int mspeed) ;

//this function moves the robot backwards
void MoveReverse(int steps, int mspeed);

//This fucntion spins the right wheel
void SpinRight(int steps, int mspeed);

//This function spins the left wheel
void SpinLeft(int steps, int mspeed);

#endif
