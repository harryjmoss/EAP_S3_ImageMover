from imagemover import move_images
from imagemover import s3_query

def main():
    bucket="eap-images-converted-jp2"
    folder = 'EAP566'

    file_list, folder_list = s3_query.query_s3(bucket,folder)
    move_images.move_images(bucket,file_list,folder_list)


if __name__ == "__main__":
    main()