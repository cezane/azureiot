import paho.mqtt.client as mqtt
import ssl, random
from time import sleep

iothub_name = "SMHub"
device_id = "SM1"
mqtt_url = "{}.azure-devices.net".format(iothub_name)
root_ca = "./certs/digicertbaltimoreroot.pem"
public_crt = "./certs/rsa_cert.pem"
private_key = "./certs/rsa_private.pem"
publish_point = "devices/{}/messages/events/".format(device_id)

connflag = False

def on_connect(client, userdata, flags, response_code):
    global connflag 
    connflag = True   
    print("Connected with status: {0}".format(response_code))

def on_publish(client, userdata, mid):
    print("User data: {} -- mID: {}".format(userdata, mid))
    #client.disconnect()

if __name__ == "__main__":
    print "Loaded MQTT configuration information."
    print "Endpoint URL: " + mqtt_url
    print "Root Cert: " + root_ca
    print "Device Cert: " + public_crt
    print "Private Key: " + private_key
    
    client = mqtt.Client("SM1", protocol=mqtt.MQTTv311)

    #client.password_pw_set(username="{}.azure-devices.net/{}/api-version=2016-11-14".format("SMHub", "SM1")

    client.tls_set(root_ca,
                   certfile = public_crt, 
                   keyfile = private_key, 
                   cert_reqs = ssl.CERT_REQUIRED, 
                   tls_version = ssl.PROTOCOL_TLSv1_2, 
                   ciphers = None)

    client.username_pw_set(username="{}.azure-devices.net/{}".format(iothub_name, device_id), password="")

    client.on_connect = on_connect
#    client.on_publish = on_publish

    print "Connecting to Azure IoT Hub..."
    client.connect(mqtt_url, port = 8883, keepalive=60)
    client.loop_start()
#    client.loop_forever()

    while 1==1:
        sleep(0.5)
        print connflag
        if connflag == True:
            print "Publishing..."
            ap_measurement = random.uniform(25.0, 150.0)
            client.publish(publish_point, ap_measurement, qos=1)
            print("ActivePower published: " + "%.2f" % ap_measurement )
        else:
            print("waiting for connection...")


