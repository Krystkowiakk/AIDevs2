import openai
import requests

class OpenAIClient:
    """
    A client to interact with OpenAI's API.
    Provides a method to obtain completions.
    """
    
    @staticmethod
    def get_completion(prompt, model="gpt-4", max_tokens=300, temperature=0.3):
        """
        Get a completion response from OpenAI for a given prompt.
        
        :param prompt: Text prompt for the completion.
        :param model: OpenAI model to use.
        :param max_tokens: Maximum tokens in the response.
        :param temperature: Sampling temperature.
        :return: Completion response or None if request fails.
        """
        messages = [{"role": "user", "content": prompt}]
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return response.choices[0].message["content"]
        except openai.error.OpenAIError as e:
            print(f"OpenAI error: {e}")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        
#OpenAIClient.get_completion("What is the capital of France?")

class AIDevsClient:
    """
    A client to interact with a given API.
    Provides methods to obtain tokens, fetch tasks, and submit answers.
    """
    
    def __init__(self, base_url, api_key):
        """
        Initialize the APIClient.
        
        :param base_url: Base URL for the API.
        :param api_key: Authentication key for the API.
        """
        self.base_url = base_url
        self.api_key = api_key

    def _make_request(self, method, endpoint, payload=None):
        """
        A generic method to make API requests.
        
        :param method: HTTP method (GET, POST, etc.)
        :param endpoint: API endpoint.
        :param payload: JSON payload for POST requests.
        :return: JSON response or None if request fails.
        """
        url = f"{self.base_url}/{endpoint}"
        response = getattr(requests, method)(url, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error in {method} request to {endpoint}: {response.text}")
            return None

    def get_token(self, task_name):
        """
        Fetch a token for a given task name.
        
        :param task_name: Name of the task.
        :return: Token or None if request fails.
        """
        payload = {"apikey": self.api_key}
        return self._make_request("post", f"token/{task_name}", payload)

    def get_task(self, token):
        """
        Fetch a task using a token.
        
        :param token: Token for the task.
        :return: Task details or None if request fails.
        """
        return self._make_request("get", f"task/{token}")

    def submit_answer(self, token, answer):
        """
        Submit an answer for a task using a token.
        
        :param token: Token for the task.
        :param answer: Answer to be submitted.
        :return: API response or None if request fails.
        """
        payload = {"answer": answer}
        return self._make_request("post", f"answer/{token}", payload)

### Initialize the APIClient with your base URL and API key.
#api_client = AIDevsClient(base_url=BASE_URL, api_key=API_KEY)