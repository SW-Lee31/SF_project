import time
import paho.mqtt.client as mqtt_client

class Pub_mqtt:
    def __init__(self, borker_addr, port, pub_id, topic):
        self.broker_addr = borker_addr
        self.port = port
        self.pub_id = pub_id
        self.topic = topic

    def connect_mqtt(self):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("connected successs!")
            else:
                print("failed connect, return code %d\n", rc)

        pub = mqtt_client.Client(self.pub_id)
        pub.on_connect = on_connect
        pub.connect(self.broker_addr, self.port)
        return pub

    def publish(self, client):
        msg_cnt = 0

        while True:
            time.sleep(1)
            msg = f"messages : {msg_cnt}"
            result = client.publish(self.topic, msg)
            status = result[0]

            if status == 0:
                print(f"send '{msg}' to topic '{self.topic}'")
            else:
                print(f"failed to send message")
            msg_cnt += 1

    # def run(self):
        # pub = connect_mqtt()
        # pub.loop_start()
        # publish(pub)

