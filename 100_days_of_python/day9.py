#Dictonairy
#First_dictonairy ={
# key: value,
#"Function": "a loop"
#}

#To call a dictoanry you do this
#print(First_dictonairy["Function"])
#output would be: "a loop"

#empty_dictonairy = {}

#wiping dictonairy if its full to just use this
#empty_dictonairy = {}


#This is how you get the values of the dictoanairy. If i wanted just the key then it would be print(thing)
#for thing in First_dictonairy:
   # print(First_dictornairy[thing])

# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# student_grades = {}

# for key in student_scores:
#     score  = student_scores[key]
#     if score <= 70:
#         student_grades[key] = "Fail"
#     if  score >= 71 and score <= 80:
#         student_grades[key] = "Acceptable"
#     if  score >= 81 and score <= 90:
#         student_grades[key] = "Exceeds Expectations"
#     if  score >= 91 and score <= 100:
#         student_grades[key] = "Outstanding"
      


#-------------------------------------------------------------------------
#Nested lists and dictonairies

# travel_log = {
#   "france" : ["paris", "Lille", "Djon"]  

# }
# print(travel_log["france"][1])


# nested_list = ["a", "b", ["c", "d"]]
# #2 is to go into the second brackets and 1 is the element inside those brackets
# print(nested_list[2][1])

# travel_log = {
    
# "France": {
#     "num_cities_visted": 8,
#     "num_times visited": 3,
#     "cities": ["paris", "lille", "Dijon"]
# }
# }

# print(travel_log["France"]["cities"][2])

#----------------------------------------------------------------------------------------------------
bidders = {}

def addbidder():
    name = input("What is your name?: \n")
    bid = int(input("What is your bid?: \n"))
    bidders[name] = bid
    answer = input("Is there another bidder? Enter: 'y' or 'n' \n")
    if answer == 'y':
        print("\n" * 100) 
        addbidder()
    else:
        top_bidder = 0
        winner = ""
        for key in bidders:
            money = bidders[key]
            if money > top_bidder:
                top_bidder = money
                winner = key
        print(f"The winner is {winner} with a bid of ${top_bidder}")

addbidder()
                 
             
