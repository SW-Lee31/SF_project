#failed

import threading
import time
import paho.mqtt.client as mqtt_client

broker_addr = '192.168.0.135'
port = 1883
sub_topic = 'outTopic'
pub_topic = 'test/test1'
pub_id = 'py_pub'
sub_id = 'py_sub'
rcv_msg = ''
sub_conn_flag = False

# Pub측 연결
def pub_connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("connected successs!")
        else:
            print("failed connect, return code %d\n", rc)

    pub = mqtt_client.Client(pub_id)
    pub.on_connect = on_connect
    pub.connect(broker_addr, port)
    return pub

# Pub측 Publish(send) 데이터 송신 함수(Call back)
def publish(client):
    msg_cnt = 0

    while True:
        time.sleep(1)
        msg = ''
        #msg = f"messages : 안녕하세여 from Pub{msg_cnt}"
        if (rcv_msg != ''):
            msg = rcv_msg

        result = client.publish(pub_topic, msg)
        status = result[0]

        if status == 0:
            print(f"send '{msg}' to topic '{pub_topic}'")
        else:
            print(f"failed to send message")
        msg_cnt += 1

# Sub측 연결
def sub_connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            if sub_conn_flag == False:
                print('connected Successful')
            sub_conn_flag = True
        else:
            print('failed connect, return code %d\n', rc)

    sub = mqtt_client.Client(sub_id)
    sub.on_connect = on_connect
    sub.connect(broker_addr, port)
    return sub

# Sub측 Subscribe(receive) 데이터 수신
def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received '{msg.payload.decode()}' from '{msg.topic}' topic")
        rcv_msg = msg.payload.decode() + '토픽명 : ' + msg.topic

    client.subscribe(sub_topic)
    client.on_message = on_message

def sub_run():
    sub = sub_connect_mqtt()
    subscribe(sub)
    sub.loop_forever()

def run():
    pub = pub_connect_mqtt()
    #pub.loop_start()
    publish(pub)

if __name__ == '__main__':
    sub_thread = threading.Thread(target=sub_run)
    sub_thread.start()

    run()