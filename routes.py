from flask import Flask, render_template,url_for, flash, redirect
from forms import loginform, regform
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

app = Flask(__name__)
app.config['SECRET_KEY'] = '9811c5f2fe723bba58042708fd2e402b'
cred = credentials.Certificate('service.json')
fireb = firebase_admin.initialize_app(cred)
db = firestore.client()
docs = db.collection(u'Bikes').get()




@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/login', methods = ['POST','GET'])
def register():
    form = loginform()
    if form.validate_on_submit():
        if form.email.data == 'root' and form.password.data == 'root':
            flash(f'login successful {form.email.data}')
            return(redirect(url_for('home')))
        else: 
            flash(f'login unsuccessful')
    return render_template('register.html', form = form)

@app.route('/register', methods = ['GET','POST'])
def login():
    form = regform()
    return render_template('login.html')

@app.route('/database', methods = ['POST','GET'])
def data():
    urls= []
    for doc in docs:
        urls.append(doc.to_dict())
    print(urls)
    return render_template('database.html', urls = urls)

if __name__ == '__main__':
    app.run()
    