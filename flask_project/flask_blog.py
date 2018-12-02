from flask import Flask,render_template
app = Flask(__name__)

posts=[
{
"author" : "Manoj Agarwal",
"title" : "Blogpost1",
"Content" :"First Post",
"date_posted" :" December 4 2018"
},
{
"author" : "Manoj Kumar",
"title" : "Blogpost2",
"Content" : "Second Post",
"date_posted" : " December 4 2018"
}
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title="About")

if __name__=='__main__':
    app.run(debug=True)
