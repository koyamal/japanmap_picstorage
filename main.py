from flask import Flask, render_template, request, redirect, send_file
import photo_db

app = Flask(__name__)
app.secret_key = 'adfba2efkajd2fjlir37aerwe'

@app.route('/')
def top():
    return render_template('main.html')

@app.route('/photo/<picture_id>')
def photo(picture_id):
    print('Hello!')
    photo = photo_db.get_file(picture_id)
    if photo is None:
        return msg('ファイルがありません')
    return send_file(photo['path'])

@app.route('/prefecture/<prefName>')
def hello_pref(prefName):
    return render_template('hello_pref.html', prefName=prefName, pictures=photo_db.get_pref_pictures(prefName))

@app.route('/upload/try', methods=['POST'])
def upload_try():
    prefName = request.form.get('pref_name', None)
    upfile = request.files.get('upfile', None)
    if upfile is None:
        return msg('アップロード失敗')
    if upfile.filename == '':
        return msg('アップロード失敗')
    picture_id = photo_db.save_file(upfile, prefName)
    if picture_id == 0:
        return msg('データベースのエラー')

    return redirect('/')

def msg(s):
    return render_template('msg.html', msg=s)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
