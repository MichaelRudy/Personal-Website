from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	info = {
		'Name': 'Michael Rudy',
		'headline': ['About', 'Education', 'Projects', 'Contact'],
		'location': 'Washington, D.C.',
		'email': 'michaelrudy4@icloud.com', 
		'education': {'school': 'The George Washington University', 
					  'degree': 'Bachelors in Information Systems; minor in Economics',
					  'date': 'May 2021',
					  'desc': """Notable coursework included Business Systems Development, 
					  Database Application and Design, Python Programming, Financial Economics, Human Capital Economics, Intermediate Macroeconomic Theory, and Intermediate Microeconomic Theory."""},
		
	}
	return render_template('home.html', info=info)
	
if __name__ == '__main__':
	app.run(debug=True)


