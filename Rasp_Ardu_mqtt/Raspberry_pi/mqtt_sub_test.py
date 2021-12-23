import paho.mqtt.client as mqtt

# 서버에서 conn 응답 시 호출되는 콜백
def attempt_connect(client, userdata, flags, rc):
    print("connected with result code " + str(rc))
    client.subscribe("test") # 구독 태그 명

def rcv_message(client, userdata, msg):
    print(msg.topic + " // " + str(msg.payload)) # 토픽 // 메시지

client = mqtt.Client("python_Sub")
client.on_connect = attempt_connect
client.on_message = rcv_message

client.connect("192.168.0.135", 1883, 60) # 라즈베리파이 브로커 연결
client.loop_forever()