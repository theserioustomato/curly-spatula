#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, render_template
import joblib


# In[2]:


app = Flask(__name__)


# In[3]:



@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        rate = request.form.get("rate")
        print(rate)
        
        model1 = joblib.load("DBS_Reg")
        pred1 = model1.predict([[float(rate)]])
        print(pred1)
        out1 = "Predicted DBS share price base on Linear Regression Model is: " + str(pred1)
        
        model2 = joblib.load("DBS_DT")
        pred2 = model2.predict([[float(rate)]])
        print(pred2)
        out2 = "Predicted DBS share price base on Decision Tree Model is: " + str(pred2)
        
        model3 = joblib.load("DBS_NN")
        pred3 = model3.predict([[float(rate)]])
        print(pred3)
        out3 = "Predicted DBS share price base on Neutral Network Model is: " + str(pred3)
        
        return(render_template("index.html", result1=out1, result2=out2, result3=out3))
        
    else:
        return(render_template("index.html", result1="1", result2="2", result3="3"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




