# codewars challenge, check out the URL:
# https://www.codewars.com/kata/568dc014440f03b13900001d/train/python
def get_drink_by_profession(param):
    # Convert all string input to lowercase to prevent issues 
    # with incorrect writing styles.
    param = param.lower()
    dictionary = {
        "jabroni" : "Patron Tequila",
        "school counselor" : "Anything with Alcohol",
        "programmer" : "Hipster Craft Beer",
        "bike gang member" : "Moonshine",
        "politician" : "Your tax dollars",
        "rapper" : "Cristal",
    }
    # Use conditional values to pull values out of the dict that are
    # available. Else you just return "Beer" and your're done.
    if param in dictionary:
        return dictionary.get(param)
    else:
        return 'Beer'
        
get_drink_by_profession()