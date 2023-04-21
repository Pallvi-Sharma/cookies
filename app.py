
from flask import Flask, render_template
app=Flask(__name__)
@app.route("/")
def pal():
    return render_template('index.html')
@app.route("/about")
def vip():
    return render_template('about.html')
@app.route("/contact")
def vp():
    return render_template('contact.html')
@app.route("/fruit")
def vpo():
    return render_template('fruit.html')
@app.route("/testimonial")
def vpi():
    return render_template('testimonial.html')

if __name__=="__main__":
    app.run(debug=True)  