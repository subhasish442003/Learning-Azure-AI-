# Enviroment (.env) for  Integrate Azure OpenAI into your app file
AZURE_OAI_ENDPOINT="https://openai-bicky.openai.azure.com/openai/deployments/gpt-35-turbo-xxx/chat/completions?api-version=2024-08-01-xxxxxxx"
AZURE_OAI_KEY="9rNUtArKZkRAkvXrvW9PvcTvxCGsaQWxMNjesLMDvaIDfOjYuGXyJQQJ99AKACYeBjFXJ3w3AAAxxxxxxxxx"
AZURE_OAI_DEPLOYMENT="gpt-35-turbo-xxx"

#code for Integrate Azure OpenAI into your app file
import os
from dotenv import load_dotenv
from openai import AzureOpenAI

def main():
    try:
        # Get configuration settings
        load_dotenv()
        azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
        azure_oai_key = os.getenv("AZURE_OAI_KEY")
        azure_oai_deployment = os.getenv("AZURE_OAI_DEPLOYMENT")

        # Initialize the Azure OpenAI client
        client = AzureOpenAI(
            azure_endpoint=azure_oai_endpoint,
            api_key=azure_oai_key,
            api_version="2024-02-15-preview"
        )

        # Create a system message
        system_message = """
        I am a hiking enthusiast named Forest who helps people discover hikes in their area.
        If no area is specified, I will default to near Rainier National Park.
        I will then provide three suggestions for nearby hikes that vary in length.
        I will also share an interesting fact about the local nature on the hikes when making a recommendation.
        """
        
        # Initialize messages array
        messages_array = [{"role": "system", "content": system_message}]

        while True:
            # Get input text
            input_text = input("Enter the prompt (or type 'quit' to exit): ")
            if input_text.lower() == "quit":
                break
            if len(input_text) == 0:
                print("Please enter a prompt.")
                continue

            print("\nSending request for summary to Azure OpenAI endpoint...\n")

            # Send request to Azure OpenAI model
            messages_array.append({"role": "user", "content": input_text})
            response = client.chat.completions.create(
                model=azure_oai_deployment,
                temperature=0.7,
                max_tokens=1200,
                messages=messages_array
            )
            
            # Extract generated text from the response
            generated_text = response.choices[0].message.content
            
            # Add generated text to messages array and print it
            messages_array.append({"role": "assistant", "content": generated_text})
            print("Summary: " + generated_text + "\n")

    except Exception as ex:
        print(f"An error occurred: {ex}")

if __name__ == '__main__':
    main()

