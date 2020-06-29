from tqdm import tqdm
import boto3

def move_eap_cover_image_to_end(bucket,old_file_key,new_file_key):
    old_file_location = bucket+'/'+old_file_key
    s3 = boto3.resource('s3')
    s3.Object(bucket,new_file_key).copy_from(CopySource=old_file_location)
    s3.Object(bucket,old_file_key).delete()
    return

def get_folder_contents(file_list,folder):
    folderContents = [s for s in file_list if folder in s]
    return folderContents

def get_first_last_file_numbers(folderContents):
    fileNumbers=[]
    for file in folderContents:
        fileNumbers.append(int(file.rsplit(r'/',1)[1].split('.',1)[0]))
    fileNumbers.sort()
    coverFile=str(fileNumbers[0])
    endFile=str(fileNumbers[-1]+1)
    return coverFile,endFile


def move_images(bucket,file_list,folder_list):
    for folder in tqdm(folder_list):
        folderContents = get_folder_contents(file_list,folder)
        cover_file, end_file = get_first_last_file_numbers(folderContents)
        #move_eap_cover_image_to_end(bucket, cover_file,end_file)

        # you just want the base name of the folder + the file numbers + .jp2
        cover_file_key=folderContents[0].rsplit('/',1)[0]+'/'+cover_file+'.jp2'
        new_file_key=folderContents[0].rsplit('/',1)[0]+'/'+end_file+'.jp2'

        print(cover_file_key,end_file_key)

