from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Define routes using templates

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['GET', 'POST'])
def manage_users():
    if request.method == 'POST':
        user_name = request.form['name']
        users.append(user_name)
        return redirect(url_for('manage_users'))
    return render_template('users.html', users=users)

@app.route('/notes', methods=['GET', 'POST'])
def manage_notes():
    if request.method == 'POST':
        note_content = request.form['content']
        note_user = request.form['user']
        if note_user:  # Check if a user is selected
            notes.append({'user': note_user, 'content': note_content})
            return redirect(url_for('manage_notes'))
    return render_template('notes.html', notes=notes, users=users)

# List to store user names and notes
users = []
notes = []


if __name__ == '__main__':
    app.run(debug=True, port=5000)


