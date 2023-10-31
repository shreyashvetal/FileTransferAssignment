import os
from services.transfer import FileTransfer
import pytest

TEMP_DIR = 'temp_test_dir'

@pytest.fixture(scope='module')
def setup_teardown():
    os.makedirs(TEMP_DIR)
    with open(os.path.join(TEMP_DIR, 'test_file.txt'), 'w') as f:
        f.write('Test content')
    yield

    os.rmdir(TEMP_DIR)

def test_get_files(setup_teardown):
    transfer = FileTransfer(TEMP_DIR)
    files = transfer.get_files(TEMP_DIR, ('.txt',))
    assert len(files) == 1
    assert os.path.basename(files[0]) == 'test_file.txt'
