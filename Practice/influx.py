import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
import random
import random
import decimal
import time



bucket = "ros"
org = "org"
token = "3gx3OABxgX9iEg0z76R44GxbLPZoyOL3NGMCMOCPAKKPObWXoDbKKSKomDrpfEX0ESyNSJPZ_CpBJdnzpRTRIA=="
# Store the URL of your InfluxDB instance
url = "http://192.168.1.246:8086"

client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
)

# Write script
write_api = client.write_api(write_options=SYNCHRONOUS)

def createRandomData () :
    return random.randint(-100000000, 900000000)/100000000

try:
    x = 1
    while (1):
        record = influxdb_client.Point("ros_data") \
            .field("shoulder_lift_joint",createRandomData() ) \
            .field("wrist_1_joint", createRandomData() ) \
            .field("wrist_2_joint", createRandomData() ) \
            .field("wrist_3_joint", createRandomData() ) \
            .field("shoulder_pan_joint", createRandomData() )
        write_api.write(bucket=bucket, org=org, record=record)
        print("Data Inserted: ", x)
        x = x + 1
        time.sleep(1)
except Exception as e:
    print(e)



