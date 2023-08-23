import os
from pprint import pprint
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'/home/cloud_user/gcp/Python-for-Cloud-and-Machine-Learnng/gcp-py-api.json'
#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'gcp-py-api.json'

storage_client = storage.Client()


"""
Get Bucket
"""
#my_bucket = storage_client.get_bucket(bucket_name)
#pprint(vars(my_bucket))

"""
Upload File
"""
def upload_to_bucket(blob_name, file_path, bucket_name):
    '''
    Upload file to a bucket
    : blob_name  (str) - object name
    : file_path (str)
    : bucket_name (str)
    '''
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(file_path)
    return blob

# response = upload_to_bucket('Voice List', 'Voice List.csv', bucket_name)
# response = upload_to_bucket('/docs/requirementABC', 'requirements.txt', bucket_name)




if __name__ == "__main__":
    #create_bucket(bucket_name=sys.argv[1])
    #for bucket in storage_client.list_buckets(max_results=100):
    #   print(bucket)
    bucket_name= 'my-new-bucket-1010101010-dilip'
    blob_name = '/docs/test.txt'
    file_path ='demo.txt'
    print(upload_to_bucket(blob_name, file_path, bucket_name))

    my_bucket = storage_client.get_bucket(bucket_name)
    pprint(vars(my_bucket))