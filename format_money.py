# codewars challenge, check out the URL:
# https://www.codewars.com/kata/55902c5eaa8069a5b4000083/train/python
def format_money(amount):
    # The format method does fit the purpuse
    # Keyword to google is just 'number formatting'
    amount = '${0:.2f}'.format(amount)
    return amount

format_money()

# Examples:

# 3 needs to become $3.00

# 3.1 needs to become $3.10
