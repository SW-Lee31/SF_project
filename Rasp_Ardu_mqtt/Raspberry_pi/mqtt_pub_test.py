import paho.mqtt.client as mqtt

mqtt = mqtt.Client("python_pub")
mqtt.connect("192.168.0.135", 1883) # mqtt 서버에 연결

mqtt.publish("test", "Hello from Pub") # 토픽명, 메시지내용

mqtt.loop(2) # timeout 2sec
mqtt.loop_start()