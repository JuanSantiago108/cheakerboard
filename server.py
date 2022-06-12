
from re import X
from flask import Flask, render_template
app = Flask(__name__)



@app.route('/')
def level_zero():
    return render_template("index.html")



@app.route('/checkerboard/<int:x>/<int:y>')
def level_one(x,y):
    return render_template("index.html",x=x, y=y )


# @app.route('/checkerboard/<int:num>')
# def level_one(num):
#     return render_template("index.html")	# notice the 2 new named arguments!


# @app.route('/checkerboard/<int:num>/<string:color>')
# def level_two(num,color):
#     return render_template("index.html", color=color,num=num)	# notice the 2 new named arguments!



if __name__=="__main__":
    app.run(debug=True)

