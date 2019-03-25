from flask import Flask,render_template,request,redirect
#import ulysses

app = Flask(__name__)

app.vars={}
urls=""

@app.route('/',methods=['GET'])
def index():
    	#return render_template('tool.html')
        return "you GETTED me"

@app.route('/slack',methods=['POST'])
def index2():
	# app.vars['url'] = request.form['url']
	# urls = str(app.vars['url'])
	# ulysses.ithaca(urls)
	# title = ulysses.title
	# wcount = ulysses.wcount
	# return render_template('result.html',ptitle=title)
    return "you POSTED me"

if __name__ == "__main__":
    app.run()
