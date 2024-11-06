#Enviroment for READ-TEXT file
AI_SERVICE_ENDPOINT="https://azureai-xxxxxx.cognitiveservices.azure.com/"
AI_SERVICE_KEY="8mtVHOv0dtzGXQkLvWu8KzcsBmvttRJiqgoaakMoBKVuwQ65N0dXJQQJ99AKACYeBjFXJ3w3AAAAACOG4wO0"

#code for READ-TEXT file
from dotenv import load_dotenv
import os
import time
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt

# Import namespaces
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

def main():
    global cv_client
    try:
        # Load environment variables
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')

        # Authenticate Azure AI Vision client
        cv_client = ImageAnalysisClient(
            endpoint=ai_endpoint,
            credential=AzureKeyCredential(ai_key)
        )

        # Display menu options for reading text
        print('\n1: Use Read API for image (Lincoln.jpg)')
        print('2: Read handwriting (Note.jpg)')
        print('Any other key to quit\n')

        command = input('Enter a number: ')
        if command == '1':
            image_file = os.path.join('images', 'Lincoln.jpg')
            GetTextRead(image_file)
        elif command == '2':
            image_file = os.path.join('images', 'Note.jpg')
            GetTextRead(image_file)

    except Exception as ex:
        print("Error:", ex)

def GetTextRead(image_file):
    print('\nProcessing Image:', image_file)
    
    # Open image file
    with open(image_file, "rb") as f:
        image_data = f.read()
    
    # Use the Analyze function to read text in the image
    result = cv_client.analyze(
        image_data=image_data,
        visual_features=[VisualFeatures.READ]
    )

    # Display the image and overlay extracted text
    if result.read is not None:
        print("\nExtracted Text:")
        
        # Prepare image for drawing annotations
        image = Image.open(image_file)
        fig = plt.figure(figsize=(image.width / 100, image.height / 100))
        plt.axis('off')
        draw = ImageDraw.Draw(image)
        color = 'cyan'

        for line in result.read.blocks[0].lines:
            # Print detected text line
            print(f"  {line.text}")

            # Draw bounding polygon for each line
            line_polygon = [(point.x, point.y) for point in line.bounding_polygon]
            draw.polygon(line_polygon, outline=color, width=3)

            # Draw bounding polygons and print confidence for each word
            for word in line.words:
                word_polygon = [(point.x, point.y) for point in word.bounding_polygon]
                print(f"    Word: '{word.text}', Bounding Polygon: {word_polygon}, Confidence: {word.confidence:.4f}")
                draw.polygon(word_polygon, outline=color, width=2)
        
        # Display the annotated image
        plt.imshow(image)
        plt.tight_layout(pad=0)

        # Save annotated image
        outputfile = 'text.jpg'
        fig.savefig(outputfile)
        print('\nResults saved in', outputfile)

if __name__ == "__main__":
    main()
