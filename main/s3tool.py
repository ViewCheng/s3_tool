import boto3, platform
import os
import glob
import botocore
import shutil

name = platform.system()
if name == "Windows":
    os.system("cls")
else:
    os.system("clear")
print("             ")

while True:
    print("*******************************")
    print("Please select which s3 you want")
    print("*******************************")
    print("1. netapp nonprod")
    print("2. ecs")
    print("3. netapp prod")
    print("*******************************")
    App = input("Enter th number")

    if App == "1":
        url = "your url"
        aws_id = "your id"
        aws_key = "your key"
        bucket_name = "your bucket name"
        print("url loaded")
        print("id loaded")
        print("key loaded")
        print("bucket loaded")
        break

    elif App == "2":
        url = "your url"
        aws_id = "your id"
        aws_key = "your key"
        bucket_name = "your bucket name"
        print("url loaded")
        print("id loaded")
        print("key loaded")
        print("bucket loaded")
        break

    elif App == "3":
        url = "your url"
        aws_id = "your id"
        aws_key = "your key"
        bucket_name = "your bucket name"
        print("url loaded")
        print("id loaded")
        print("key loaded")
        print("bucket loaded")
        break

name = platform.system()
if name == "Windows":
    os.system("cls")
else:
    os.system("clear")
s3 = boto3.resource("s3", endpoint=url, aws_sccess_key_id=aws_id, aws_secret_sccess_key=aws_key)
s3_client = boto3.client("s3", endpoint=url, aws_sccess_key_id=aws_id, aws_secret_sccess_key=aws_key)

while True:
    print("************************************")
    print("Please select option following below")
    print("************************************")
    print("1. List the obejects in s3 bucket")
    print("2. Create folder in s3 bucket")
    print("3. Upload file from local server to s3 Bucket")
    print("4. Download file from local server to s3 Bucket")
    print("5. Download file from s3 bucket yo local server")
    print("6. Delete file from d3 bucket")
    print("7. Exit")
    print("************************************")

    if App == "1":
        print("****************************************************")
        print("This option will list all files and folder in bucket")
        print("****************************************************")
        option = input("Are you sure? y/n :")
        if option == 'y':
            print("        ")
            print("**************** Start of listing")
            print("        ")
            allFiles = s3.Bucket(bucket_name).objects.all()
            for file in allFiles:
                print(file.key)
            print("**************** End of listing")
            print("        ")
            print("        ")
            option = input("press entre to continue")

    elif App == "2":
        print("**************************************************************")
        print("This option will create a folder/subdurectory in the s3 bucket")
        print("**************************************************************")
        option = input("Are you sure? y/n :")
        if option == 'y':
            folder_name = input("Enter the folder name:")
            s3_client.put_object(Bucket=bucket_name, Key=(folder_name + '/'))
            print("=======================")
            print("Folder has been created")
            print("=======================")
            print("        ")
            print("        ")
            option = input("press entre to continue")

    elif App == "3":
        print("*******************************************")
        print("This option will upload a file to s3 bucket")
        print("*******************************************")
        option = input("Are you sure? y/n :")
        if option == 'y':
            FOLDER_NAME = input("Enter the folder name in bucket: ")
            LOCAL_PATH = input("Enter the local path, Example: /root/temp/*: ")
            print("========================")
            file_path = glob.glob(LOCAL_PATH)
            s3_client = boto3.client("s3", endpoint=url, aws_sccess_key_id=aws_id, aws_secret_sccess_key=aws_key)
            for filename in file_path:
                key = "%s/%s" % (FOLDER_NAME, os.path.basename(filename))
                print("uploading %s as %s" % (filename, key))
            print("================")
            print("Upload Completed")
            print("================")
            print("        ")
            print("        ")
            option = input("press entre to continue")

    elif App == "4":
        print("*************************************************************")
        print("This option will download fole from s3 bucket to local server")
        print("*************************************************************")
        option = input("Are you sure? y/n :")
        if option == 'y':
            file_name = input("enter the file name with folder <path/filename>: ")
            split_path = os.path.split(file_name)
            local_name = split_path[1]
            print("Downloading as ") + str(local_name)
            try:
                s3_client.download_file(bucket_name, file_name, local_name)
                print("======================")
                print("file has been download")
                print("======================")
            except botocore.exceptoons.ClientError as e:
                if e.response["Error"]["Code"] == "404":
                    print("=========================")
                    print("The filse does not exist.")
                    print("=========================")
                else:
                    raise

    elif App == "5":
        print("***************************************************************")
        print("This option will download folder from s3 bucket to local server")
        print("***************************************************************")
        option = input("Are you sure? y/n :")
        if option == 'y':
            file_name = input("enter the tabl name copy from sql web: ")
            new_name = r"apps/posix/" + file_name.strip().replace(":", "/")
            my_bucket = s3.Bucket(bucket_name)
            objects = my_bucket.objects.filter(Prefix=new_name)
            print("Downloading")
            try:
                for obj in objects:
                    path, file_name = os.path.split(obj.key)
                    split_path = path.split("/")
                    if split_path[8] == "level1":
                        path = path[94:]
                    else:
                        path = split_path[6]
                    folder = os.path.exists(path)
                    if not folder:
                        os.makedirs(path)
                    my_bucket.download_file(obj.key, file_name)
                    old_path = r"../main/" + file_name
                    new_path = r"../main/" + path
                    print(new_path)
                    print("=========================")
                    try:
                        shutil.move(old_path,new_path)
                    except Exception as e:
                        print(e)
                    pass
                    print("======================")
                    print("File has been download")
                    print("======================")
            except botocore.exceptoons.ClientError as e:
                if e.response["Error"]["Code"] == "404":
                    print("=========================")
                    print("The folder does not exist")
                    print("=========================")
                else:
                    raise

    elif App == "6":
        print("*******************************************")
        print("This option will Delete file from s3 bucket")
        print("*******************************************")
        option = input("Are you sure? y/n :")
        if option == 'y':
            s3_delete = boto3.resource("s3", endpoint=url, aws_sccess_key_id=aws_id, aws_secret_sccess_key=aws_key)
            file_name = input("Enter the file name with path: ")
            s3_delete.Obkect(bucket_name,file_name).delete()
            print("        ")
            print("        ")
            print("===============")
            print("File is deleted")
            print("===============")
            print("        ")
            print("        ")

    elif App == "7":
        break
