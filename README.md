# azureiot
A basic pub/sub application to test the Azure IoT services.

#### IoT Hub creation:

  1. In the Azure Portal, click "Create a resource" --> "Internet of Things" --> "IoT Hub";
  2. In the IoT Hub panel, fill in the fields:    
      2.1. Enter a hub name;    
      2.2. Enter a new resource group name;    
      2.3. Choose the closest location to you;    
      2.4. For pricing and scale tier, choose the "F1 - Free" tier    
  3. Click "Create";
  4. When the IoT Hub is ready, open the IoT Hub panel;
  5. Click on the "Overview" and get the "Hostname" information;
  6. Click on "Shared access policies";
  7. Click on the "iothubowner" policy and get the connection string (primary key).

#### IoT device creation:

  1. In the IoT hub panel, find the "EXPLORERS" menu and click "IoT devices";    
  2. Click on the "+Add" button and fill in the fields:    
      2.1. Type the "Device ID";    
      2.2. Select "X.509 Self-Signed" in the "Authentication Type";    
      2.3. Enter the "Primary Key" and "Secondary Key" thumbprints (in this case, I repeated the "Primary Key" thumbprint for the "Secondary Key");    
      2.4. In order to get the key thumbprint, you can perform:    
            2.4.1. Convert the .pem format file to a .der format file:

    openssl x509 -in rsa_cert.pem -out rsa_cert.der -outform der

            2.4.2. Get the SHA1 thumbprint for the cert file (the portal, for now, only supports SHA1 thumbprints - I already alerted the Azure team about this):

    openssl sha -sha1 rsa_cert.der

      2.5. Select "Enable" in the "Connect device to IoT Hub";
  3. Click "Save".

#### 


