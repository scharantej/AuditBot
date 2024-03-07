
# Import necessary modules
from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

# Define the database model
class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(120))

# Create the database tables
db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the data from the input field
        data = request.form['data']

        # Create a new Data object and add it to the database
        new_data = Data(data=data)
        db.session.add(new_data)
        db.session.commit()

        # Redirect to the confirmation page
        return redirect(url_for('confirmation'))

    return render_template('index.html')

@app.route('/confirmation')
def confirmation():
    return '<h1>Data submitted successfully!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
