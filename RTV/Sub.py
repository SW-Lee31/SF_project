import paho.mqtt.client as mqtt_client

broker_addr = '192.168.0.32'
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
        global rcvmsg
        rcvmsg = msg.payload.decode()

    client.subscribe(topic)
    client.on_message = on_message

def rcved_data(client: mqtt_client):
    return

def run():
    sub = connect_mqtt()
    subscribe(sub)
    # Loop (내장 스레드)
    sub.loop_forever()