from time import sleep

import paho.mqtt.client as mqtt

team_id = 'arithe'

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    #client.subscribe(team_id + "/motor")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("hi-code.kr", 4883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_start()
sleep(0.1)
for i in range(100):
    k = input(str(i)+':')
    if k == 'w':
        client.publish(team_id+'/motor', '50,50')
    elif k == 's':
        client.publish(team_id+'/motor', '-50,-50')
    elif k == 'a':
        client.publish(team_id+'/motor', '0,50')
    elif k == 'd':
        client.publish(team_id+'/motor', '50,0')
    else:
        client.publish(team_id+'/motor', '0,0')    