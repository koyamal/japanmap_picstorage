import re, photo_file
from photo_sqlite import exec, select

def save_file(upfile, prefName):
    if not re.search(r'\.(jpg|jpeg)$', upfile.filename):
        print('JPEGではない：', upfile.filename)
        return 0
    picture_id = exec('''INSERT INTO pictures (picture_name, pref) 
    VALUES (?, ?)''', upfile.filename, prefName)
    upfile.save(photo_file.get_path(picture_id))
    return picture_id

def get_file(picture_id):
    a = select('SELECT * FROM pictures WHERE picture_id=?', picture_id)
    if len(a) == 0:
        return None
    p = a[0]
    p['path'] = photo_file.get_path(picture_id)
    return p


def get_pref_pictures(prefName):
    return select('SELECT * FROM pictures WHERE pref=? ORDER BY picture_id DESC', prefName)