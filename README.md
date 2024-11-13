Learning-Azure-AI-
Azure AI provides a suite of tools and services for building intelligent applications, including Azure Cognitive Services, Azure Machine Learning, and the Azure Bot Service. It helps developers integrate AI capabilities like vision, language understanding, and machine learning into their solutions.

#ReadMe file for rest-client file
This Python script detects the language of user-input text using Azure's Text Analytics Language API. It reads the API endpoint and key from a `.env` file, then sends text to the API for language detection. To use, set up an Azure endpoint and key, enter text when prompted, and type "quit" to exit.

#ReadMe file for sdk-client file
This Python script detects the language of user-input text using Azure's Text Analytics SDK. It retrieves the API endpoint and key from a `.env` file, and utilizes `TextAnalyticsClient` for language detection. To run, configure the `.env` file with your Azure credentials, input text when prompted, and type "quit" to stop.

#ReadMe file for Image-Analysis file
This Python script uses Azure AI Vision's Image Analysis Client to analyze images for captions, tags, objects, and people. It also includes functionality for background removal or foreground matting using the Azure API. Requires environment variables for the Azure endpoint and key, and an image file as input.

#ReadMe file for Read-Text file
This Python script uses Azure AI Vision's Image Analysis Client to read and extract text from images. It can handle both printed text and handwritten text recognition. The recognized text and bounding boxes are displayed on the image, which is then saved with annotations. Requires environment variables for Azure endpoint and key.
#ReadMe file for  Fruit Image Classification
This repository contains a dataset of fruit images, labeled and organized for image classification tasks. Each image is stored with metadata including resolution, file name, and capture date. The goal is to use these images for training machine learning models to classify different types of fruits. All images are sourced and stored securely in Azure Blob Storage, accessible via provided URLs.


#  Readme file for Hiking Guide Chatbot using Azure OpenAI
This Python script creates a chatbot named "Forest" that suggests hiking trails. By default, it offers recommendations near Rainier National Park, sharing trail options and interesting nature facts. Environment variables (`AZURE_OAI_ENDPOINT`, `AZURE_OAI_KEY`, `AZURE_OAI_DEPLOYMENT`) should be set in a `.env` file for the Azure OpenAI configuration.
## Usage
Run `python script.py` and enter prompts to interact with the bot.

#ReadMe file Text Analytics with Azure AI
This Python script performs text analytics on files in a `reviews` folder using Azure AI's Text Analytics service. It detects the language, analyzes sentiment, extracts key phrases, identifies entities, and recognizes linked entities within each text file. To run, configure your Azure AI endpoint and key in a `.env` file as `AI_SERVICE_ENDPOINT` and `AI_SERVICE_KEY`. 
# Requirements
- Install dependencies: `pip install -r requirements.txt`

