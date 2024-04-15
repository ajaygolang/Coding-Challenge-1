import re

def validate_credit_card(card):
    # Define the regular expression pattern
    pattern = r'^[456]\d{3}(-?\d{4}){3}$'
    
    # Check if the card matches the pattern
    if re.match(pattern, card):
        # Remove hyphens if present
        card = card.replace('-', '')
        
        # Check if there are no more than 4 repeated digits
        if re.search(r'(\d)\1{3,}', card):
            return 'Invalid'
        else:
            return 'Valid'
    else:
        return 'Invalid'

# Input the number of credit card numbers
n = int(input().strip())

# Input and validate each credit card number
for _ in range(n):
    card_number = input().strip()
    print(validate_credit_card(card_number))
