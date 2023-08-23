import os
from pprint import pprint
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'/home/cloud_user/gcp/Python-for-Cloud-and-Machine-Learnng/gcp-py-api.json'
#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'gcp-py-api.json'

storage_client = storage.Client()

if __name__ == "__main__":
    #create_bucket(bucket_name=sys.argv[1])
    for bucket in storage_client.list_buckets(max_results=100):
       print(bucket)

       #pprint(vars(bucket))

       #bucket.name
       #bucket._properties['selfLink']
       #bucket._properties['id']
       #bucket._properties['location']
       #bucket._properties['timeCreated']
       #bucket._properties['storageClass']
       #bucket._properties['timeCreated']
       #bucket._properties['updated']