#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# In[4]:


# Step 1: Load the dataset
titanic_df = pd.read_csv("C:/Users/ALEN/Downloads/Titanic-Dataset.csv")
titanic_df


# In[10]:


# Step 2: Data Preprocessing
# Handle missing values
titanic_df.fillna(method='ffill', inplace=True)


# In[13]:


# Select features and target variable
X = titanic_df.drop(columns=['Survived', 'Name', 'Ticket', 'Cabin'])
y = titanic_df['Survived']
# Step 3: Split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Step 4: Model Selection and Training
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)


# In[14]:


# Step 5: Model Evaluation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("Classification Report:")
print(classification_report(y_test, y_pred))


# In[ ]:


# Step 6: Prediction
# You can now use the trained model to make predictions on new data

