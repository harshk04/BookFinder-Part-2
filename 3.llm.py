from gradio_client import Client

def get_prompts(prompt):
    client = Client("harshk04/TextGeneration")
    result = client.predict(
            message=f"{prompt}",
            system_message="You are a friendly chatbot who has complete knowledge of books",
            max_tokens=512,
            temperature=0.7,
            top_p=0.95,
            api_name="/chat"
    )

    list_prompts = result.split("\n")
    list_prompts = [prompt[3:] for prompt in list_prompts if prompt and prompt[0].isdigit()]

    return list_prompts

if __name__ == '__main__':
    prompt1 = 'Top 100 fiction books'
    prompt2 = 'Top 10 fiction books'
    prompts1=get_prompts(prompt1)
    print(f"Query1: {prompt1}")
    print(f"LLM Response: {prompts1}")
    print("\n")
    prompts2=get_prompts(prompt2)
    print(f"Query2: {prompt2}")
    print(f"LLM Response: {prompts2}")

    with open('llm.txt', 'w') as file:
        for item in prompts1:
            file.write(f"{item}\n")
        for item in prompts2:
            file.write(f"{item}\n")

