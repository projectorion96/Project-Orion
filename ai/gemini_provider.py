import time
from google import genai

client = genai.Client()

# Models to try in order
MODELS = [
    "gemini-3.1-flash-lite",
    "gemini-flash-lite-latest",
    "gemini-2.0-flash",
]


def ask_gemini(prompt):
    last_error = None

    for model in MODELS:
        print(f"Trying model: {model}")

        for attempt in range(3):
            try:
                response = client.models.generate_content(
                    model=model,
                    contents=prompt,
                )

                return response.text

            except Exception as e:
                last_error = e
                print(f"Attempt {attempt + 1} failed: {e}")

                if attempt < 2:
                    wait = (attempt + 1) * 5
                    print(f"Retrying in {wait} seconds...")
                    time.sleep(wait)

        print(f"Switching from {model} to next model...\n")

    raise last_error