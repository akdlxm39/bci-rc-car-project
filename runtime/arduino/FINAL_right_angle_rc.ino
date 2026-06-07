#include <SoftwareSerial.h>
#include <AFMotor.h>

// ── 모터 채널 설정: 왼쪽 M1, 오른쪽 M2 (필요하면 3-4로 교체)
AF_DCMotor leftMotor(1, MOTOR12_64KHZ);
AF_DCMotor rightMotor(2, MOTOR12_64KHZ);

// ── 파라미터
const uint8_t SPEED_LEFT = 252;  // 왼쪽 바퀴 속도
const uint8_t SPEED_RIGHT = 206; // 오른쪽 바퀴 속도(약간 보정이 필요할 수도 있음)
const int TURN_LEFT_MS = 280;   // 90도 포인트턴 시간 - 기체마다 보정 필요
const int TURN_RIGHT_MS = 300;
char prevAction = 'S';
char buf[3];

SoftwareSerial BT(A0, A1); // HM-10 TX->A0, RX->A1

void turnLeft90()
{
  leftMotor.run(BACKWARD);
  delay(TURN_LEFT_MS);
  leftMotor.run(FORWARD);
}

void turnRight90()
{
  rightMotor.run(FORWARD);
  delay(TURN_RIGHT_MS);
  rightMotor.run(BACKWARD);
}

void setup()
{
  buf[0] = 'S';
  buf[1] = 'S';
  buf[2] = 'S';
  Serial.begin(9600);
  BT.begin(9600);
  Serial.println("HM-10 Bluetooth ready");
  leftMotor.run(FORWARD);
  rightMotor.run(BACKWARD);
}

void loop()
{
  if (BT.available())
  {
    char c = BT.read();
    if (c == 'a'){
      leftMotor.setSpeed(SPEED_LEFT);
      rightMotor.setSpeed(SPEED_RIGHT);
      return;
    }
    if (c == 'z'){
      leftMotor.setSpeed(0);
      rightMotor.setSpeed(0);
      return;
    }
    if (c!='L' && c!='R' && c!='S') return;
    buf[2] = c;
    bool allSame = true;
    for (int i = 0; i < 3; i++)
    {
      if (buf[i] != buf[0])
        allSame = false;
    }
    buf[0] = buf[1];
    buf[1] = buf[2]; // buf[0] = 바로 이전, buf[1] = 현재
    if (!allSame){
      prevAction = 'S';
      return;
    }

    if (c == 'L' && prevAction != 'L')
    {
      prevAction = 'L';
      turnLeft90();
    }
    else if (c == 'R' && prevAction != 'R')
    {
      prevAction = 'R';
      turnRight90();
    }
  }

}
