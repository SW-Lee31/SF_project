import paho.mqtt.client as mqtt_client

broker_addr = '192.168.0.135'
port = 1883
topic = 'test/test1'
sub_id = f'py_sub'

# MQTT 연결 콜백함수
def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print('connected Successful')
        else:
            print('failed connect, return code %d\n', rc)

    sub = mqtt_client.Client(sub_id)
    sub.on_connect = on_connect
    sub.connect(broker_addr, port)
    return sub

# 구독 연결 콜백함수
def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received '{msg.payload.decode()}' from '{msg.topic}' topic")

    client.subscribe(topic)
    client.on_message = on_message

def run():
    sub = connect_mqtt()
    subscribe(sub)
    # Loop (내장 스레드)
    sub.loop_forever()

if __name__ == '__main__':
    run()


# 서버에서 conn 응답 시 호출되는 콜백
#def attempt_connect(client, userdata, flags, rc):
    #print("connected with result code " + str(rc))
    #client.subscribe("test") # 구독 태그 명

#def rcv_message(client, userdata, msg):
    #print(msg.topic + " // " + str(msg.payload)) # 토픽 // 메시지

#client = mqtt.Client("python_Sub")
#client.on_connect = attempt_connect
#client.on_message = rcv_message

#client.connect_async("192.168.0.135", 1883, 60) # 라즈베리파이 브로커 연결
#client.loop_forever()