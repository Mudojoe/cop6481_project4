
#from config import get_openai_client
from openai import OpenAI, APIError
import requests
import re
def extract_number_from_text(text):
    """Extracts the first number found in the provided text."""
    match = re.search(r'\d+', text)
    if match:
        return int(match.group(0))
    return None

def assess_transaction_risk(transaction_description,client):
    #client = get_openai_client()
    prompt_text = f"Given the transaction description: '{transaction_description}', " \
                  f"assess the level of risk on a scale from 1 (very low risk) to 10 (very high risk)."

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt_text
            }
        ],
        model="gpt-3.5-turbo",
    )

    try:
        response_text = chat_completion.choices[0].message.content.strip()
        risk_score = extract_number_from_text(response_text)
        if risk_score is None:
            print("No numerical risk score found in the response.")

    except ValueError:
        print("No valid risk score extracted from the model's response.")
        risk_score = 5

    except APIError:
        print("A problem occurred with the OpenAI API.")
        risk_score = -1


    except requests.exceptions.RequestException as e:
        print(f"A network-related error occurred: {e}")
        risk_score = -1


    except AttributeError as e:
        print(f"Error accessing the response data: {e}")
        raise

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        risk_score = -1

    return risk_score
