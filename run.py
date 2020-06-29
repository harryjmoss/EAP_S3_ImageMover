from imagemover import move_images
from imagemover import s3_query
from datetime import datetime

def main():
    bucket="eap-images-converted-jp2"
    folder = 'EAP566'

    file_list, folder_list = s3_query.query_s3(bucket,folder)
    all_files_moved = move_images.move_images(bucket,file_list,folder_list)

    today = datetime.today().strftime('%Y-%m-%d')
    output_file_name = folder+"_FilesMoved_"+today+".csv"

    with open(output_file_name, 'w') as outfile:
        outfile.write("Old Location, New Location")
        for item in all_files_moved:
            outfile.write(item[0],item[1])



if __name__ == "__main__":
    main()