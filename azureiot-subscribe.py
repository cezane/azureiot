import paho.mqtt.client as mqtt
import ssl, random
from time import sleep

root_ca = "./certs/digicertbaltimoreroot.pem"
public_crt = './certs/rsa_cert.pem'
private_key = './certs/rsa_private.pem'

iothub_name = "SMHub"
device_id = "SM1"
mqtt_url = "{}.azure-devices.net".format(iothub_name)
mqtt_port = 8883
topic = "devices/{}/messages/devicebound/#".format(device_id)
print topic
def error_str(rc):
    """Convert a Paho error to a human readable string."""
    return "Some error occurred. {}: {}".format(rc, mqtt.error_string(rc))

def on_disconnect(unused_client, unused_userdata, rc):
    """Paho callback for when a device disconnects."""
    print("on_disconnect", error_str(rc))

def on_connect(client, userdata, flags, response_code):
    print("Connected with status: {0}".format(response_code))
    client.subscribe(topic, 1)

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(client, userdata, msg):
    print("------ON MESSAGE!!!! -- {}".format(msg))
    print("Topic: {0} -- Payload: {1}".format(msg.topic, str(msg.payload)))

if __name__ == "__main__":
    print "Loaded MQTT configuration information."
    print("Endpoint URL: {0}".format(mqtt_url))
    print("Root Cert: {0}".format(root_ca))
    print("Device Cert: {0}".format(public_crt))
    print("Private Key: {0}".format(private_key))
    
    client = mqtt.Client("SM1", protocol=mqtt.MQTTv311)

    client.tls_set(root_ca, 
                   certfile = public_crt, 
                   keyfile = private_key, 
                   cert_reqs = ssl.CERT_REQUIRED, 
                   tls_version = ssl.PROTOCOL_TLSv1_2, 
                   ciphers = None)

    client.username_pw_set(username="{}.azure-devices.net/{}".format(iothub_name, device_id), password="")

    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect

    print("Connecting to Azure IoT Hub...")
    client.connect(mqtt_url, mqtt_port, keepalive=60)
    client.loop_forever()

