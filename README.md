## This project repository contains the following files essential for the development and execution of the Crop Prediction System:

# Crop_Suggestions
The Crop Prediction System is a web-based application that assists farmers in predicting the best crop to plant based on soil nutrients and pH levels. The system uses a machine learning model to analyze input parameters (Nitrogen, Phosphorus, Potassium, and pH) and provides a crop suggestion.

# Crop_Suggestions.pptx:
A PowerPoint presentation summarizing the project. It includes details about the problem statement, data analysis, model development, results, and conclusions. This presentation is useful for stakeholders to understand the project’s objectives and outcomes.

# soil_measures.csv:
The dataset used in the project for training and testing the machine learning model. It contains various soil measurements and the corresponding crops that thrive in those conditions. This dataset is critical for model development and evaluation.

# Crop_Suggestions.ipynb:
A Jupyter Notebook that includes the complete process of data analysis, model training, and evaluation. It showcases the steps taken to build and fine-tune the machine learning model used for predicting the best crop based on soil nutrients and pH levels.

# index.html:
The frontend interface for the Crop Prediction System. It allows users to input soil parameters (Nitrogen, Phosphorus, Potassium, pH) and submit them to the backend for crop prediction. The HTML file is designed to be user-friendly and responsive.

# main.py:
The core backend script written in Python using FastAPI. It handles HTTP requests, processes the input from the frontend, and returns the crop prediction based on the trained model. This file is essential for running the server-side logic of the application.

# random_forest_model.pkl:
A serialized Random Forest model file used by the backend to make predictions. This file contains the trained machine learning model, which is loaded by the main.py script to provide real-time crop suggestions.

