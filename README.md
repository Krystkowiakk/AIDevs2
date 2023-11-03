# AIDevs.pl Second Edition Course Repository

This repository contains the code for the second edition of the AIDevs, a 5-week practical program blending Generative AI tools, particularly OpenAI models, with RAG, application logic and automation tools.

The course is instructed by:

- Adam Gospodarczyk (@overment)
- Jakub Mrugalski (@unknown)
- Mateusz Chrobok (@MateuszChrobok)
  
## Getting Started

1. Complete the .env file:
AI_DEVS_API_KEY = "enter your AIDevs API code"
OPEN_AI_API_KEY="enter your AIDevs API code"

2. My solutions for AIDevs tasks are in AIDevs2.ipynb, starting from the newest at the top.

## Utilities

- [`config.py`](./utilities/config.py): loading environment variables using the `dotenv` package. It ensures that the keys required for interacting with the AIDevs platform and OpenAI API are correctly loaded from the `.env` file and made available throughout the codebase.

- [`common.py`](./utilities/common.py): Contains two classes, `OpenAIClient` and `AIDevsClient`, which act as wrappers for their respective APIs. `OpenAIClient` facilitates communication with OpenAI's API, allowing for easy generation of AI completions. `AIDevsClient` provides methods for obtaining tokens, fetching tasks, and submitting answers within the AIDevs platform.
