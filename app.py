#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import traceback


# In[23]:


# load model 



# In[24]:


# define model prediction function

import numpy as np
import pandas as pd
import sys
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler



# In[28]:
model2 = True # should read from model file 

app = Flask(__name__)

@app.route('/predict', methods=['POST']) # Create http://host:port/predict POST end point

def predict():
    if model2:
        try:
            json_ = request.json #capture the json from POST
            query = pd.read_json(json_, orient='records')  
            prediction = query 

            #return jsonify({'prediction': [int(x) for x in prediction]})
            return prediction.to_json(orient="records")
        

        except Exception as e:

            return jsonify({'error': str(e), 'trace': traceback.format_exc()})
    else:
        print('train first')
        return 'no model here'
    
if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=81, debug=False)



# In[ ]:




