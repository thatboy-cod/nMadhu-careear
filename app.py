from flask import Flask


app = Flask(__name__)

@app.route("/")

def hello_world():
  return "hellow nabu"
if __name__ == "__main__":
  print("iam inside the if now ")
  app.run(host="0.0.0.0",debug=True)