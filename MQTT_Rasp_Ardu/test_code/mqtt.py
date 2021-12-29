from pub_mqtt import Pub_mqtt as p
from sub_mqtt import Sub_mqtt as s

if __name__ == "__main__":
    mq_pub = p('192.163.0.135', 1883, 'publisher', 'test/test1' )
    mq_sub = s('192.163.0.135', 1883, 'subscriber', 'test/test1')
    mq_pub.connect_mqtt()
    mq_sub.connect_mqtt()