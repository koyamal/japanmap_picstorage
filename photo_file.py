import os

BASE_DIR = os.path.dirname(__file__)
DATA_FILE = BASE_DIR + '/data/photos.sqlite3'
FILES_DIR = BASE_DIR + '/files'

def get_path(picture_id, ptype = ''):
    return FILES_DIR + '/' + str(picture_id) + ptype + '.jpg'

