import re

def categorize_description(description):
    description = description.lower()

    if re.search(r'\brecharge\b|\bairtel\b|\bjio\b|\bvodafone\b', description):
        return "Bill"
    elif re.search(r'\bnetflix\b|\bhotstar\b|\bprime\b|\bott\b', description):
        return "OTT Subscription"
    elif re.search(r'\buber\b|\bola\b|\bcab\b', description):
        return "Transport"
    elif re.search(r'\bgroceries\b|\bbigbasket\b|\bdmart\b', description):
        return "Groceries"
    elif re.search(r'\bswiggy\b|\bzomato\b|\bfood\b|\brestaurant\b', description):
        return "Food"
    elif re.search(r'\brent\b|\blandlord\b', description):
        return "Rent"
    elif re.search(r'\bamazon\b|\bflipkart\b', description):
        return "Shopping"
    elif re.search(r'\bmedicines\b|\bhospital\b|\bpharmacy\b', description):
        return "Health"
    else:
        return "Others"
