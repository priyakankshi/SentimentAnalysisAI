#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask
from flask import request, render_template
from textblob import TextBlob


# In[2]:


app = Flask(__name__)


# In[3]:


@app.route("/", methods=["GET","POST"])
def index():
    if request.method=="POST":
        text = request.form.get("text")
        print(text)
        output = TextBlob(text).sentiment
        s = "Sentiment is: "+ str(output)
        return(render_template("index.html", result = s))
    else:
        return(render_template("index.html", result ="waiting"))


# In[4]:


if __name__ == "__main__":
    app.run()


# In[ ]:




