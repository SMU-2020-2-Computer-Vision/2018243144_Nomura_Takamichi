#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask

sample_api = Flask(__name__)

@sample_api.route("/gse/api/sample", methods=["GET"])
def hello_world():
    return "Hello World!"

if __name__ == "__main__":
    sample_api.run()

