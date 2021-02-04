from flask import Flask, render_template, request

app = Flask(__name__, template_folder="")

@app.route("/", methods=["GET","POST"]) 
def home():
   if (request.method == "GET"):
      return render_template("index.html")
   else:
      if (request.form["num1"] != "" and request.form["num2"] != ""):
         num1 = request.form ["num1"]
         num2 = request.form ["num2"]

         if (request.form == "mult"):
            mult = int(num1) * int(num2)
            return str(mult) 

         else:
            divi = int(num1) // int(num2)
            return str(divi)            
      else:
         return "Informe um valor válido!"   


app.run(port=8080, debug=True)     
