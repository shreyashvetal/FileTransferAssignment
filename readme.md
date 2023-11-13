# FileTransfer Python Package

The `FileTransfer` package provides a simple interface for transferring files to AWS S3 and Google Cloud Storage.

## Installation

You can install the package using pip:

    
    pip install dist/Filetransfer-1.0.0.tar.gz

## Usage
Import the FileTransfer class in your Python script or application:

    from filetransfer.transfer import FileTransfer

    # Create an instance of FileTransfer
    file_transfer = FileTransfer(source_dir='path/to/source/directory')
    
    # Perform file transfers
    file_transfer.upload_to_s3(bucket_name='your_s3_bucket',profile_name='profile name in case of session connection',extentions='list_of_extentions')
    file_transfer.upload_to_gcs(bucket_name='your_gcs_bucket',extentions='list_of_extentions')
    
## Parameters
**source_dir**: The path to the source directory containing the files you want to transfer.

**forced_check**: (Optional) If True, forces a re-check of the source directory.

**profile_name**: (Optional) The AWS profile name to use for S3 authentication.

**extensions**: (Optional) List of file extensions to consider during file transfers.

## Example
Here's an example of transferring files using the FileTransfer package:

    from filetransfer.transfer import FileTransfer
    
    file_transfer = FileTransfer(source_dir='path/to/source/files')
    file_transfer.upload_to_s3(bucket_name='my_s3_bucket', profile_name='my_aws_profile',extensions=['.png'])
    file_transfer.upload_to_gcs(bucket_name='my_gcs_bucket',extensions=['.pdf'])
