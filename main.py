from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/thread/<int:thread_id>')
def thread(thread_id):
    topics = {
        1: {"name": "Обсуждаем всё!", "description": "Здесь можно обсудить абсолютно всё!"},
        2: {"name": "Технологии будущего", "description": "Давайте поговорим о новых технологиях и будущем!"},
        3: {"name": "Графический дизайн", "description": "Обсуждаем дизайн, арт, графику и многое другое."}
    }
    
    topic = topics.get(thread_id)
    
    if topic:
        return render_template('thread.html', topic_name=topic["name"], topic_description=topic["description"])
    else:
        return "Тема не найдена", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
