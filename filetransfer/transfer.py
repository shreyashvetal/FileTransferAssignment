import os
import boto3
from google.cloud import storage

class FileTransfer:
    _source_dir_content = None  # Class attribute to store source dir path data
    _source_dir = None  # Class attribute to store the source dir path

    def __init__(self, source_dir, forced_check=False):
        if forced_check or FileTransfer._source_dir != source_dir or not FileTransfer._source_dir_content:
            if not os.path.exists(source_dir):
                raise FileNotFoundError(f'The directory "{source_dir}" does not exist.')
            file_dict = {}
            for root, dirs, filenames in os.walk(source_dir):  # Fix variable name 'directory' to 'source_dir'
                for filename in filenames:
                    file_path = os.path.join(root, filename)  # Fix variable name 'file' to 'filename'
                    _, file_extension = os.path.splitext(file_path)
                    if file_extension:
                        file_extension = file_extension.lower()
                        if file_extension in file_dict:
                            file_dict[file_extension].append(file_path)
                        else:
                            file_dict[file_extension] = [file_path]
            FileTransfer._source_dir_content = file_dict
            FileTransfer._source_dir = source_dir

    def upload_to_s3(self, bucket_name, profile_name="", extensions = ('.jpg', '.png', '.svg', '.webp', '.mp3', '.mp4', '.mpeg4', '.wmv', '.3gp', '.webm')):
        try:
            s3 = boto3.client('s3')
        except Exception as e:
            session = boto3.Session(profile_name=profile_name)
            s3 = session.client('s3')

        for ext in extensions:
            ext = ext.lower()

            if ext in FileTransfer._source_dir_content:
                for file_path in FileTransfer._source_dir_content[ext]:
                    file_name = os.path.basename(file_path)
                    try:
                        s3.upload_file(file_path, bucket_name, file_name)
                    except Exception as e:
                        raise RuntimeError(f"Failed to upload {file_path} to S3. Error: {e}")
        
    def upload_to_gcs(self, bucket_name, extensions = ('.doc', '.docx', '.csv', '.pdf')):
        try:
            client = storage.Client()
            bucket = client.bucket(bucket_name)

            for ext in extensions:
                ext = ext.lower()

                if ext in self.file_dict:
                    for file_path in self.file_dict[ext]:
                        file_name = os.path.basename(file_path)
                        blob = bucket.blob(file_name)
                        blob.upload_from_filename(file_path)

        except Exception as e:
            raise RuntimeError(f"Failed to upload files to GCS. Error: {e}")