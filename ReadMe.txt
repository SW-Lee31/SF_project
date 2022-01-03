Don't use pip-install (Realiablity ↓) -> can't install smbus properly
Install smbus manually 
Change "import smbus" -> "import smbus2" in Arm_Lib

pip로 인스톨 하지 말 것 (smbus -> smbus2 사용)
setup파일로 수동으로 라이브러리 설치 권장

ic2-tools (i2c 통신 디버깅)
install i2c-tools 

i2cdetect (외부 i2c 장치 연결여부 확인)
i2cdetect -y 1

track_bar_ex -> 로봇 팔 제어 GUI 구현(센서 값 읽어들이기 용이 c#과의 연계는 추후)

