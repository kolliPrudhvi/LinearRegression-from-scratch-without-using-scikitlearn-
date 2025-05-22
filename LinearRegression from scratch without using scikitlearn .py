#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt


# In[3]:


#hours studied
X= np.array([[1.5],[3.2],[5.1],[7.0],[8.3]])

#Labels(exam scores)
y=np.array([[30],[50],[75],[85],[95]])


# In[31]:


plt.scatter(X,y,color='blue')
plt.xlabel("Hours studied")
plt.ylabel("Exam Score")
plt.title("Hours studied VS Exam Score")
plt.grid(True)
plt.show()


# In[24]:


class LinearRegressionScratch:
    def __init__(self,learning_rate=0.01,epochs=1000):
        self.lr=learning_rate
        self.epochs=epochs
        self.w=0
        self.b=0
    def fit(self,x,y) :
        n=len(X)
        for _ in range(self.epochs):
            y_pred = self.w * X + self.b
            dw = (2/n) * np.sum(X * (y_pred - y))
            db = (2/n) * np.sum(y_pred - y)
            self.w -= self.lr * dw
            self.b -= self.lr * db
    def predict(self,X):
        return self.w*X + self.b


# In[25]:


def predict(self,X):
    return self.w * + self.b
     


# In[27]:


#Training 
model=LinearRegressionScratch(learning_rate=0.01,epochs=1000)
model.fit(X,y)


# In[29]:


# predictions
predictions = model.predict(X)


# In[30]:


print(f"Learned weight (w): {model.w}")
print(f"Learned bias (b): {model.b}")


# In[32]:


plt.scatter(X, y, color="blue", label="Actual Data")
plt.plot(X, predictions, color="red", label="Predicted Line")
plt.title("Linear Regression From Scratch")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:




