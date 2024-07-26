from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import Config
import mistune

app = Flask(__name__)
app.config.from_object(Config)
CORS(app) 

db = SQLAlchemy(app)

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

@app.route('/test', methods=['GET'])
def test():
    with open('./example/example.md', 'r', encoding='utf-8') as file:
        mdText = file.read()
        markdown = mistune.create_markdown(renderer=HighlightRenderer(), plugins=['math', 'table'])
        
        html = markdown(mdText)
        return jsonify({'msg': 'Test Good', 'html': html}), 200

if __name__ == '__main__':
    app.run(debug=True)
