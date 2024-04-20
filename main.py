# main.py

from assess_risk import assess_transaction_risk
from config import get_openai_client
def process_transactions(file_path,client):
    try:
        with open(file_path, 'r') as file:
            heading = next(file).strip()
            print(heading)
            for line in file:
                transaction_description = line.strip()
                if transaction_description:
                    risk_score = assess_transaction_risk(transaction_description,client)
                    print(f"Transaction: {transaction_description} - Risk Score: {risk_score}")
            print()  # Print a blank line after finishing processing each file
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred while processing {file_path}: {e}")
if __name__ == '__main__':
    client = get_openai_client()
    files_to_process = ['transactions.txt', 'high_assessment.txt', 'low_assessment.txt']
    for file_name in files_to_process:
        process_transactions(file_name, client)
