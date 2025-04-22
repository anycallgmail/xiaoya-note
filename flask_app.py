```python
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# 存储笔记的目录
NOTES_DIR = 'notes'
if not os.path.exists(NOTES_DIR):
    os.makedirs(NOTES_DIR)

# 首页，显示所有笔记
@app.route('/')
def index():
    notes = []
    for filename in os.listdir(NOTES_DIR):
        if filename.endswith('.txt'):
            note_id = os.path.splitext(filename)[0]
            with open(os.path.join(NOTES_DIR, filename), 'r', encoding='utf-8') as file:
                content = file.read()
            notes.append({'id': note_id, 'content': content})
    return render_template('index.html', notes=notes)

# 创建新笔记
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        content = request.form.get('content')
        if content:
            # 生成唯一的笔记ID
            note_id = str(len(os.listdir(NOTES_DIR)) + 1)
            filename = os.path.join(NOTES_DIR, f'{note_id}.txt')
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(content)
            return redirect(url_for('index'))
    return render_template('create.html')

# 查看笔记详情
@app.route('/note/<note_id>')
def note(note_id):
    filename = os.path.join(NOTES_DIR, f'{note_id}.txt')
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        return render_template('note.html', note_id=note_id, content=content)
    return '笔记未找到', 404

# 编辑笔记
@app.route('/edit/<note_id>', methods=['GET', 'POST'])
def edit(note_id):
    filename = os.path.join(NOTES_DIR, f'{note_id}.txt')
    if os.path.exists(filename):
        if request.method == 'POST':
            content = request.form.get('content')
            if content:
                with open(filename, 'w', encoding='utf-8') as file:
                    file.write(content)
                return redirect(url_for('index'))
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        return render_template('edit.html', note_id=note_id, content=content)
    return '笔记未找到', 404

# 删除笔记
@app.route('/delete/<note_id>')
def delete(note_id):
    filename = os.path.join(NOTES_DIR, f'{note_id}.txt')
    if os.path.exists(filename):
        os.remove(filename)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```