from imagemover import s3_query
from boto3 import client


def test_raw_query_s3():
    test_bucket_name = "eap-images-converted-jp2"
    test_prefix = "EAP566/EAP566_1_15_18_1/" # known folder with 57 images in
    file_list=[]

    conn = client('s3')  # again assumes boto.cfg setup, assume AWS S3
    for key in conn.list_objects(Bucket=test_bucket_name,Prefix=test_prefix)['Contents']:
        file_list.append(key['Key'])
    assert len(file_list) == 57


def test_query_s3():
    test_bucket_name = "eap-images-converted-jp2"
    test_prefix = "EAP566/EAP566_1_15_18_1/" # known folder with 57 images in

    file_list, _folders = s3_query.query_s3(test_bucket_name,test_prefix)
    assert len(file_list) == 57

