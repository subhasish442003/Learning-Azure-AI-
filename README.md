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

