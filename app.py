from flask import Flask,render_template,jsonify

app = Flask(__name__)
JOBS =[
  {     'id':1,
        'title':'Data Analyst',
        'location':'Bengaluru,Indaia',
       ' Salary':'Rs. 10,00,000'
  },
  {'id':2,
       'title':'Data SCientist',
      'location':'Delhi,Indaia',
      'Salary':'Rs 15,00,000'
  },
  {'id':3,
       'title':'FrontenEnd Engineer',
       'location':'Remote',
       'Salary':'Rs. 12,00,000'
  },
  {'id':4,
       'title':'Backend Engineer',
      'location':'san-francisco,Usa',
      'Salary':'$150,000'
  }]
@app.route("/")  
def hello_world():
  return render_template('home.html',jobs=JOBS,company_name="Thatboys")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
if __name__ == "__main__":
  app.run(host="0.0.0.0",debug=True)