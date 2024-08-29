import requests
import json
from llm_keys import *

class LLM:
    @staticmethod
    def complete(input_prompt, llm):
        if llm.startswith("ollama_"):
            return LLM._ollama(input_prompt, llm[7:])  # Remove "ollama_" prefix
        elif llm == "Claude":
            return LLM._claude(input_prompt)
        elif llm == "Gemini":
            return LLM._gemini(input_prompt)
        elif llm == "Cohere":
            return LLM._cohere(input_prompt)
        else:
            raise ValueError(f"Unsupported LLM: {llm}")

    @staticmethod
    def _ollama(prompt, model):
        url = "http://localhost:11434/api/generate"
        data = {
            "model": model,
            "prompt": prompt
        }
        response = requests.post(url, json=data)
        response_text = response.text
        try:
            # Parse the response as a series of JSON objects
            response_objects = [json.loads(line) for line in response_text.strip().split('\n')]
            # Combine all 'response' fields
            full_response = ''.join(obj.get('response', '') for obj in response_objects if 'response' in obj)
            return full_response
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON response from Ollama: {response_text}")

    @staticmethod
    def _claude(prompt):
        url = "https://api.anthropic.com/v1/messages"
        headers = {
            "Content-Type": "application/json",
            "X-API-Key": CLAUDE_API_KEY,
            "anthropic-version": "2023-06-01"
        }
        data = {
            "model": "claude-3-sonnet-20240229",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 1000
        }
        response = requests.post(url, headers=headers, json=data)
        response_json = response.json()
        if 'content' in response_json:
            return response_json['content'][0]['text']
        else:
            raise ValueError(f"Unexpected response structure from Claude: {response_json}")

    @staticmethod
    def _gemini(prompt):
        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "contents": [{"parts":[{"text": prompt}]}],
            "generationConfig": {
                "temperature": 0.9,
                "topK": 1,
                "topP": 1,
                "maxOutputTokens": 2048,
            }
        }
        params = {
            "key": GEMINI_API_KEY
        }
        response = requests.post(url, headers=headers, json=data, params=params)
        return response.json()['candidates'][0]['content']['parts'][0]['text']

    @staticmethod
    def _cohere(prompt):
        url = "https://api.cohere.ai/v1/generate"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {COHERE_API_KEY}"
        }
        data = {
            "model": "command",
            "prompt": prompt,
            "max_tokens": 1000,
            "temperature": 0.7
        }
        response = requests.post(url, headers=headers, json=data)
        return response.json()['generations'][0]['text']

if __name__ == "__main__":
    def test_llm(llm_name):
        try:
            response = LLM.complete("Hello, how are you?", llm_name)
            print(f"{llm_name} Test Passed. Response: {response[:50]}...")
        except Exception as e:
            print(f"{llm_name} Test Failed. Error: {str(e)}")

    # Test all LLMs
    test_llm("ollama_llama2")
    test_llm("Claude")
    test_llm("Gemini")
    test_llm("Cohere")

    # Test unsupported LLM
    try:
        LLM.complete("Test", "UnsupportedLLM")
        print("Unsupported LLM Test Failed: No exception raised")
    except ValueError as e:
        print(f"Unsupported LLM Test Passed. Error: {str(e)}")