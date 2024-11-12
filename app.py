from flask import Flask, render_template, request, url_for, redirect, flash

app = Flask(__name__)
app.config.from_mapping(SECRET_KEY='jashdklhsdjh68772391')

db =[
    {
        'id': 1,
        'title': 'Reed book',
        'complited': False
    },
    {
        'id': 2,
        'title': 'To do sport',
        'complited': True
    },
    {
        'id': 3,
        'title': 'Go to work',
        'complited': False
    }
]


@app.route('/')
def home():
    all_complited = all(el['complited'] for el in db)
    return render_template('home.html', todo_list = db, all_complited=all_complited)

@app.route('/add', methods=['POST'])
def create_task():
    title = request.form.get('title', '').strip()
    if title:
        db.append(
        {
            'id': get_last_id(),
            'title': title,
            'complited': False
        }
    )
    else:
        flash("Incorect task name", "error")
    
    return redirect(url_for('home'))

@app.route('/update/<int:id>')
def update_task(id):
    for el in db:
        if el['id'] == id:
            el['complited'] = not el['complited']
            break
    else:
            flash('Invalid task id', 'error')
    return redirect(url_for('home'))

@app.route('/delete/<int:id>')
def delete_task(id):
    for el in db:
        if el['id'] == id:
            db.remove(el)
            break
    else:
            flash('Invalid task id', 'error')
    return redirect(url_for('home'))


def get_last_id():
    if len(db) < 1:
        return 1
    else:
        x = len(db)+1
        return x


if __name__ == '__main__':
    app.run(debug=True)