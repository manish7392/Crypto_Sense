from flask import Flask, render_template
from app import create_app, db


app = create_app()
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/help')
def help():
    return render_template('help.html')

if __name__ == '__main__':
    app.run(debug=True)
