import time
import paho.mqtt.client as mqtt_client

broker_addr = '192.168.0.135'
port = 1883
topic = 'test/test1'
pub_id = 'py_pub'



def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("connected successs!")
        else:
            print("failed connect, return code %d\n", rc)

    pub = mqtt_client.Client(pub_id)
    pub.on_connect = on_connect
    pub.connect(broker_addr, port)
    return pub

def publish(client):
    msg_cnt = 0

    while True:
        time.sleep(1)
        msg = f"messages : {msg_cnt}"
        result = client.publish(topic, msg)
        status = result[0]

        if status == 0:
            print(f"send '{msg}' to topic '{topic}'")
        else:
            print(f"failed to send message")
        msg_cnt += 1

def run():
    pub = connect_mqtt()
    pub.loop_start()
    publish(pub)

if __name__ == '__main__':
    run()

#def on_publish(client, userdata, mid):
    #print("on_pub = ", mid)

#mqtt = mqtt.Client("python_pub")
#mqtt.connect("192.168.0.135", 1883) # mqtt 서버에 연결

#mqtt.publish("test", "Hello from Pub") # 토픽명, 메시지내용

#mqtt.loop(2) # timeout 2sec
#mqtt.loop_start()