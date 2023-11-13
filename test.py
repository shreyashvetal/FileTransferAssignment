import os
import sys
import pytest
from unittest.mock import patch

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))
sys.path.insert(0, project_root)
from filetransfer.transfer import FileTransfer

@pytest.fixture
def setup_test_files(tmpdir_factory):
    source_dir = tmpdir_factory.mktemp("test_source_dir")
    file_content = b'Test content'
    test_files = ['file1.jpg', 'file2.png', 'file3.docx']

    for filename in test_files:
        file_path = source_dir.join(filename)
        file_path.write(file_content)

    yield str(source_dir)

@pytest.fixture(autouse=True)
def cleanup_temp_directory(request, setup_test_files):
    yield
    source_dir = setup_test_files
    source_dir.remove()

def test_upload_to_s3(setup_test_files):
    with patch('boto3.client') as mock_boto_client:
        transfer = FileTransfer(setup_test_files, forced_check=True)
        transfer.upload_to_s3('test_bucket', extensions=['.jpg', '.png'])

    mock_boto_client.assert_called_once_with('s3')

    s3_mock = mock_boto_client.return_value
    for filename in ['file1.jpg', 'file2.png']:
        s3_mock.upload_file.assert_any_call(
            f'{setup_test_files}/{filename}', 'test_bucket', filename
        )

def test_upload_to_gcs(setup_test_files):
    with patch('google.cloud.storage.Client') as mock_gcs_client:
        transfer = FileTransfer(setup_test_files, forced_check=True)
        transfer.upload_to_gcs('test_bucket', extensions=['.docx'])

    mock_gcs_client.assert_called_once()

    gcs_client_mock = mock_gcs_client.return_value
    bucket_mock = gcs_client_mock.bucket.return_value
    for filename in ['file3.docx']:
        bucket_mock.blob.assert_any_call(filename)
        bucket_mock.blob.return_value.upload_from_filename.assert_any_call(
            f'{setup_test_files}/{filename}'
        )
