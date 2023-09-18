import json
from rudycorp.utils import request
from rudycorp import app, render_template

@app.route('/')
def index():
	headlines = ['About', 'Resume', 'Interests', 'Projects', 'Contact']
	return render_template('home.html', info=info)

# @app.route('/<string:page_name>')
# def html_page(page_name):
#     return render_template(page_name, info=info, works=works)
	
if __name__ == '__main__':
	app.run(debug=True)


