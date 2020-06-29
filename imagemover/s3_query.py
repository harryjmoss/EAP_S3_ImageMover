from boto3 import client

def get_all_s3_objects(s3, **base_kwargs):
    # use this function to get the entire contents of an s3 bucket 1000 items at a time
    # 1000 is the max, so this gets around the 1k limit with continuation tokens
    continuation_token = None
    while True:
        list_kwargs = dict(MaxKeys=1000, **base_kwargs)
        if continuation_token:
            list_kwargs['ContinuationToken'] = continuation_token
        response = s3.list_objects_v2(**list_kwargs)
        yield from response.get('Contents', [])
        if not response.get('IsTruncated'):  # At the end of the list?
            break
        continuation_token = response.get('NextContinuationToken')


def query_s3(bucket_name,folder):

    file_list=[]
    folder_list=[]
    for file in get_all_s3_objects(client('s3'), Bucket=bucket_name, Prefix=folder):
        file_list.append(file['Key'])
        folder_list.append(file['Key'].rsplit(r'/',1)[0])
    return file_list, set(folder_list)
