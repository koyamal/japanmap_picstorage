from photo_sqlite import exec

exec('''
CREATE TABLE pictures (
    picture_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    picture_name     TEXT,
    pref             TEXT,
    created_at       TIMESTAMP DEFAULT (DATETIME('now', 'localtime'))
)
''')

print('OK')
