import os
import boto3
from google.cloud import storage

AWS_CONFIG = {
    'access_key': '',
    'secret_key': '',
    'bucket_name': '',
}

GCP_CONFIG = {
    'keyfile': '/path/gcp_keyfile.json',  # Path to your GCP service account key file
    'bucket_name': '',
}

class FileTransfer:
    def __init__(self, source_dir):
        self.source_dir = source_dir

    def get_files(self, directory, extensions):
        files = []
        for root, dir, filenames in os.walk(directory):
            for filename in filenames:
                if filename.endswith(extensions):
                    files.append(os.path.join(root, filename))
        return files

    def transfer_to_aws_s3(self, files):
        s3 = boto3.client(
            's3',
            aws_access_key_id=AWS_CONFIG['access_key'],
            aws_secret_access_key=AWS_CONFIG['secret_key']
        )

        for file in files:
            s3.upload_file(file, AWS_CONFIG['bucket_name'], os.path.basename(file))

    def transfer_to_gcp_storage(self, files):
        client = storage.Client.from_service_account_json(GCP_CONFIG['keyfile'])
        bucket = client.bucket(GCP_CONFIG['bucket_name'])

        for file in files:
            blob = bucket.blob(os.path.basename(file))
            blob.upload_from_filename(file)

def main():
    source_dir = "\SacumenAssignment" #DIR path
    transfer = FileTransfer(source_dir)

    image_files = transfer.get_files(source_dir, ('.jpg', '.png', '.svg', '.webp'))
    media_files = transfer.get_files(source_dir, ('.mp3', '.mp4', '.mpeg4', '.wmv', '.3gp', '.webm'))
    document_files = transfer.get_files(source_dir, ('.doc', '.docx', '.csv', '.pdf'))

    transfer.transfer_to_aws_s3(image_files)
    transfer.transfer_to_aws_s3(media_files)
    transfer.transfer_to_gcp_storage(document_files)

if __name__ == "__main__":
    main()
