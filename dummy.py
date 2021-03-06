import paho.mqtt.client as mqtt
import threading
import time

def on_connect(client, userdata, flags, rc):
    print ("Connect with result code: "+str(rc))
    client.subscribe("Kaylee/sys/#")
    client.publish("Kaylee/sys/startup","Dummy Started")
    t = threading.Thread(target=send_update)
    t.start()
    


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))   

def send_update():
    temps = ['98', '72', '65', '45']
    while True:
        for val in temps:
            client.publish("Kaylee/Temp",val)
            time.sleep(60)


client=mqtt.Client("dummy")
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

client.loop_forever()
