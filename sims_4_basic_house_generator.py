import random  #

print("welcome to TS4 House Generator!")  

input("press Enter to generate...")  # prompts user to press enter

# def defines input
def generate_lot():
    # random.choice randomly select a *word* from the list
    
    style = random.choice([
        "modern", "craftsman", "gothic", "contemporary", "rustic", "colonial",
        "farmhouse", "cottagecore", "industrial", "victorian", "art deco",
        "minimalist", "hippie", "nature-inspired", "bohemian", "mid-century modern",
        "scandinavian", "beach house", "art nouveau", "grunge"
    ])
    #random.randint selects a random *number* from list
    number_of_bedrooms = random.randint(0, 10)
    number_of_bathrooms = random.randint(1, 5)
    sizes = random.choice(["small home", "medium home", "large home"])
    building_type = random.choice([
        "house", "apartment", "condo", "townhouse", "duplex", "triplex", "quadplex",
        "villa", "cottage", "bungalow", "chalet", "cabin", "farmhouse", "ranch",
        "lodge", "palace", "castle", "fortress", "tower", "trailer", "mobile home",
        "treehouse", "houseboat", "igloo", "loft", "barn", "penthouse"
    ])
    unique_feature = random.choice([
        "pool", "garden", "balcony", "terrace", "fireplace", "sauna", "gym",
        "home theater", "wine cellar", "library", "office", "art studio", "game room",
        "rooftop deck", "outdoor kitchen", "hot tub", "pond", "fountain", "waterfall",
        "greenhouse", "farm", "music room", "craft room", "playroom", "gazebo", "porch",
        "patio", "garage", "guesthouse", "salon", "basement"
    ])
    # return = returns variable
    # "f" = f string formatting, example f"variable: {variable}
    # "\n" = new line

    return (
        f"style:           {style}\n" 
        f"bedrooms:        {number_of_bedrooms}\n"
        f"bathrooms:       {number_of_bathrooms}\n"
        f"size:            {sizes}\n"
        f"type:            {building_type}\n"
        f"unique feature:  {unique_feature}\n"
    )

print("here is your generated lot:") 

#if = checks true or false and runs code accordingly

while True:  # true = loop will run until broken
        lot = generate_lot()  # generates a new lot
        print(lot)  # prints the generated lot
        again = str(input("would you like to try again? please type 'Y' or 'N': ")) # again = user input to continue or exit
        if again.strip().upper() == "Y":  # if yes 
            continue
        elif again.strip().upper() == "N":  # if no
            print("bye!")
            break
        else:
            print("bye!")
            break

          