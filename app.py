from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_bootstrap import Bootstrap
import os
from email_validator import validate_email, EmailNotValidError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://userapp:user1234@localhost/loguserapp' #ubah sesuai database pada mysql
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_secret_key')
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
Bootstrap(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Validate email format
        try:
            validate_email(email)
        except EmailNotValidError as e:
            return str(e), 400

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('reg.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            access_token = create_access_token(identity={'username': user.username})
            session['token'] = access_token
            return redirect(url_for('login_success'))
        return 'Invalid credentials', 401
    return render_template('log.html')

@app.route('/login_success', methods=['GET', 'POST'])
def login_success():
    token = session.get('token')
    if request.method == 'POST':
        auth_code = request.form['auth_code']
        if auth_code == token:
            return redirect(url_for('protected'))
        return 'Invalid authentication code', 401
    return render_template('login_success.html', token=token)

@app.route('/protected', methods=['GET'])
def protected():
    token = session.get('token')
    if not token:
        return redirect(url_for('login'))
    return render_template('proc.html')

@app.route('/verify_token', methods=['POST'])
@jwt_required()
def verify_token():
    return jsonify({"msg": "Token is valid"}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables
    app.run(debug=True)

