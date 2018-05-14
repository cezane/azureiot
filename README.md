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
  2. 

