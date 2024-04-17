from flask import Flask,render_template

app = Flask(__name__)
@app.route("/")
# jobs =[{'id':1,'title':'Data Analyst',
#        'location':'Bengaluru,Indaia',
#        'Salary':'Rs. 10,00,000'},{'id':2,'title':'Data SCientist',
#          'location':'Delhi,Indaia',
#          'Salary':'Rs 15,00,000'},{'id':3,'title':'FrontenEnd Engineer','location':'Remote','Salary':'Rs. 12,00,000'},{'id':4,'title':'Backend Engineer',
#          'location':'san-francisco,Usa',
#          'Salary':'$15,00,00'}]

def hello_world():
  jobs =[{'id':1,'title':'Data Analyst',
     'location':'Bengaluru,Indaia',
     'Salary':'Rs. 10,00,000'},{'id':2,'title':'Data SCientist',
       'location':'Delhi,Indaia',
       'Salary':'Rs 15,00,000'},{'id':3,'title':'FrontenEnd Engineer','location':'Remote','Salary':'Rs. 12,00,000'},{'id':4,'title':'Backend Engineer',
       'location':'san-francisco,Usa',
       'Salary':'$15,00,00'}]
  return render_template('home.html',jobs=jobs,company_name="Thatboys")
if __name__ == "__main__":
  app.run(host="0.0.0.0",debug=True)