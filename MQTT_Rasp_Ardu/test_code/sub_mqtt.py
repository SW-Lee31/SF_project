import paho.mqtt.client as mqtt_client

class Sub_mqtt:
    def __init__(self, broker_addr, port, sub_id, topic):
        self.broker_addr = broker_addr
        self.port = port
        self.sub_id = sub_id
        self.topic = topic


        # MQTT 연결 콜백함수
    def connect_mqtt(self) -> mqtt_client:
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print('connected Successful')
            else:
                print('failed connect, return code %d\n', rc)

        sub = mqtt_client.Client(self.sub_id)
        sub.on_connect = on_connect
        sub.connect(self.broker_addr, self.port)
        return sub

# 구독 연결 콜백함수
    def subscribe(self, client: mqtt_client):
        def on_message(client, userdata, msg):
            print(f"Received '{msg.payload.decode()}' from '{msg.topic}' topic")

        client.subscribe(self.topic)
        client.on_message = on_message

    # def run(self):
        # sub = self.connect_mqtt()
        # self.subscribe(sub)
        # Loop (내장 스레드)
        # sub.loop_forever()