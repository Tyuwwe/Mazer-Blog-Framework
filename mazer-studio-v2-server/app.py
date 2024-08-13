from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from config import Config
from datetime import datetime, timedelta
from exts import jwt
import mistune, os, glob, uuid

app = Flask(__name__)
app.config.from_object(Config)
jwt.init_app(app)
CORS(app) 
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

filePath = os.path.dirname(os.path.abspath(__file__))

ALLOWED_IMG_EXT = set(['png', 'jpg', 'JPG', 'PNG', 'gif', 'GIF', 'webp', 'WEBP', 'avif', 'AVIF', 'jpeg', 'JPEG'])
 
def allowed_img(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_IMG_EXT

# Markdown Highlight Renderer
class HighlightRenderer(mistune.HTMLRenderer):
    def block_code(self, code, info=None):
        if not info or info == "no-highlight":
            return f'<pre><code class="language-text line-numbers">{code}</code></pre>'
        return f'<pre><code class="language-{info} line-numbers">{code}</code></pre>'

    def codespan(self, text):
        return f'<code class="language-shell">{text}</code>'

    def inline_math(self, text):
        return f'<span class="math inline-math">{text}</span>'

    def block_math(self, text):
        return f'<div class="block-math-container"><div class="math block-math">{text}</div><button class="cp-formula btn btn-secondary btn-sm" data="{text}">Copy Formula</button></div>'

# Server Table DB Class

class Users(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    usr = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    psw = db.Column(db.Text, nullable=False)
    usr_role = db.Column(db.Integer, nullable=False)
    usr_desc = db.Column(db.Text, nullable=False)
    avt = db.Column(db.String(200))
    

class Syslog(db.Model):
    __tablename__ = 'syslog'
    
    log_id = db.Column(db.Integer, primary_key=True)
    evt_id = db.Column(db.Integer, nullable=False)
    evt_text = db.Column(db.Text, nullable=False)
    evt_at = db.Column(db.DateTime, default=datetime.utcnow)

class Pages(db.Model):
    __tablename__ = 'pages'
    
    pgs_id = db.Column(db.Integer, primary_key=True)
    md_url = db.Column(db.String(100), unique=True, nullable=False)
    ht_url = db.Column(db.String(100), unique=True)

class Articles(db.Model):
    __tablename__ = 'articles'
    
    auid = db.Column(db.String(40), primary_key=True)
    md_url = db.Column(db.String(100), unique=True, nullable=False)
    ht_url = db.Column(db.String(100), unique=True)
    author_email = db.Column(db.String(50), unique=True, nullable=False)

def convertHTML(mdText):
    markdown = mistune.create_markdown(renderer=HighlightRenderer(), plugins=['math', 'table'])
    html = markdown(mdText)
    return html

def generateHTML(folderPath):
    mdFiles = glob.glob(os.path.join(folderPath, '*.md'))
    for file in mdFiles:
        with open(file, 'r', encoding='utf-8') as f:
            content = convertHTML(f.read())
            fileName = str(uuid.uuid4()) + '.mbf'
            with open(filePath + '/static/article/' + fileName, 'w', encoding='utf-8') as w:
                w.write(content)
                # base64 encrypt
                # w.write(base64.b64encode(content.encode("utf-8")).decode("utf-8"))

def generateHTMLbyFile(file):
    with open(filePath + file, 'r', encoding='utf-8') as f:
        content = convertHTML(f.read())
        fileName = str(uuid.uuid4()) + '.mbf'
        with open(filePath + '/static/article/' + fileName, 'w', encoding='utf-8') as w:
            w.write(content)
        return '/static/article/' + fileName

@app.route('/test/<int:test_id>', methods=['GET'])
def test(test_id):
    fileAddr = filePath + '\example\\1.md'
    if test_id == 2 :
        fileAddr = filePath + '\example\example.md'
    with open(fileAddr, 'r', encoding='utf-8') as file:
        mdText = file.read()
        markdown = mistune.create_markdown(renderer=HighlightRenderer(), plugins=['math', 'table'])
        
        html = markdown(mdText)
        return jsonify({'msg': 'Test Good', 'html': html}), 200

# New Article
@app.route('/api/new_article', methods=['GET'])
def new_article():
    try:
        genID = uuid.uuid4()
        newArticle = Articles(md_url = genID + '.md')
        db.session.add(newArticle)
        db.session.commit()
        return jsonify({'message': 'New Article Created!', 'art_uuid': genID}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
    
# User Register
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['usr']
    email = data['email']
    password = data['psw']
    avt = "/static/image/default.jpg"
    print(data)
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    newUser = Users(usr=username, email=email, psw=hashed_password, usr_role=1, avt=avt)
    
    try:
        db.session.add(newUser)
        db.session.commit()
        return jsonify({'message': 'Registered Successful!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Registered Failed.'}), 400

# User Login
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['psw']
    
    user = Users.query.filter_by(email=email).first()
    
    if user and bcrypt.check_password_hash(user.psw, password):
        access_token = create_access_token(identity=email)
        refresh_token = create_refresh_token(identity=email)
        return jsonify({'message': 'Login Successful!', 'jwt': access_token, 'jwt_ref': refresh_token}), 201
    else:
        return jsonify({'error': 'Invalid username or password'}), 401

# Get User Info
@app.route('/api/users', methods=['GET'])
@jwt_required()
def getSingleUser(): 
    email = get_jwt_identity()
    user = Users.query.filter_by(email=email).first()
    if user:
        return jsonify({'usr': user.usr, 'email': user.email, 'usr_desc': user.usr_desc, 'avt': user.avt}), 201
    else:
        return jsonify({'error': 'Invalid request'}), 401

# Token Test
@app.route('/api/tokentest', methods=['GET'])
@jwt_required()
def getTokenStat():
    email = get_jwt_identity()
    return jsonify({'email': email}), 201

# Upload Image
@app.route('/api/uploadImage', methods=['POST'])
@jwt_required()
def uploadImage():
    email = get_jwt_identity()
    img = request.files['file']
    if allowed_img(img.filename):
        newFilename = str(uuid.uuid4()) + '.' + img.filename.rsplit('.', 1)[1]
        savePath = filePath + "/static/image/" + newFilename
        img.save(savePath)
        return jsonify({'message': 'Upload successful!', 'url': "/static/image/" + newFilename})
    else:
        return jsonify({'error': 'Invalid request'}), 401

# Get Random UUID
@app.route('/api/getUUID', methods=['GET'])
def getUUID():
    return jsonify({'message': 'Get successful!', 'uuid': uuid.uuid4()})

# Save Article
@app.route('/api/saveMD', methods=['POST'])
@jwt_required()
def saveMD():
    email = get_jwt_identity()
    data = request.get_json()
    md = data['md']
    auid = data['auid']
    
    art = Articles.query.filter_by(auid=auid).first()
    # Exist MD
    if art:
        with open(filePath + art.md_url, 'w', encoding='utf-8') as file:
            file.write(md)
    else:
        savePath = '/static/markdown/' + auid + '.md'
        with open(filePath + savePath, 'w', encoding='utf-8') as file:
            file.write(md)
        newArticle = Articles(auid=auid, author_email=email, md_url=savePath)
        try:
            db.session.add(newArticle)
            db.session.commit()
            return jsonify({'message': 'Save Successful!'}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'Save Failed.'}), 400

# Publish Article
@app.route('/api/publish', methods=['POST'])
@jwt_required()
def publishArt():
    email = get_jwt_identity()
    data = request.get_json()
    md = data['raw_md']
    auid = data['auid']
    
    art = Articles.query.filter_by(auid=auid).first()
    # Exist MD
    if art:
        with open(filePath + art.md_url, 'w', encoding='utf-8') as file:
            file.write(md)
        genHTML = generateHTMLbyFile(art.md_url)
        if os.path.exists(filePath.replace('\\', '/') + art.ht_url):
            os.remove(filePath.replace('\\', '/') + art.ht_url)
        art.ht_url = genHTML
        try:
            db.session.commit()
            return jsonify({'message': 'Published Successful!'}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'Publish Failed.'}), 400
    else:
        savePath = '/static/markdown/' + auid + '.md'
        with open(filePath + savePath, 'w', encoding='utf-8') as file:
            
            file.write(md)
        genHTML = generateHTMLbyFile(savePath)
        newArticle = Articles(auid=auid, author_email=email, md_url=savePath, ht_url=genHTML)
        try:
            db.session.add(newArticle)
            db.session.commit()
            return jsonify({'message': 'Published Successful!'}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'Publish Failed.'}), 400

if __name__ == '__main__':
    # generateHTML(filePath + '/static/markdown')
    app.run(debug=True)
