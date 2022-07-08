# career options
import random

advices = ["Take time to think about what you like to do, and dream and imagine ideal careers.",
           "Talk with as many adults as possible about careers and colleges.",
           "It's never too early nor too late to get organized and begin making plans.",
           "Remember that everyone must follow his or her own path in life.",
           "Don't let anyone control your dreams and ambitions.",
           "Never stop learning: read, grow, and expand your mind.",
           "Get as much education as you can.",
           "Work, volunteer, or otherwise gain some experience.",
           "Challenge yourself in high school, but don't overwhelm yourself.",
           "Stay focused",
           "Pursue your passion",
           "Strive for excellence and stay motivated"]

list_of_careers = {
    "maths": [
        {
            "office": ["lecturer/ teacher", "Auditor", "mathematician", "budget analyst"],
            "field": ["Software Developer", "Data Scientist", "Computer Programmer", "data analyst"],
        }
    ],
    "languages": [
        {
            "office": ["lecture/ teacher", "writer", "reporter", "editor"],
            "field": ["publisher", "lawyer", "journalist", "reporter"],
        }
    ],
    "chemistry": [
        {
            "office": ["Lecturer/ teacher", "chemist", "Accountant/ Auditor", "chemical engineers"],
            "field": ["Organic chemist", "Forensic Scientist.", "Forensic Researcher.", "Chemical Development Engineer."],
        }
    ],
    "biology": [
        {
            "office": ["lecturer/ teacher", "science writer", "Academic researcher.", "dentist"],
            "field": ["park ranger", "Wildlife Biologist", "marine biologist", "Forensic scientist"],
        }
    ],
    "computer": [
        {
            "office": ["teacher/ lecturer", "Mathematician", "Statistician", "Systems engineer"],
            "field": ["Mobile application developer", "Data security analyst", "game designer", "graphic designer"],
        }
    ],
    "history": [
        {
            "office": ["teacher/ lecturer", "lawyer", "writer", "journalist"],
            "field": ["diplomat", "government historian", "political advisor", "Museum curator"],
        }
    ],
    "geography": [
        {
            "office": ["teacher/ lecturer", "Climate Change Analyst.", "Water conservation officer", "Hydrologist."],
            "field": ["Surveyor", "Town planner", "Meteorologist", "Pollution Analyst"],
        }
    ],
    "agriculture": [
        {
            "office": ["teacher/ lecturer", "Food scientist", " Agricultural engineer", "Agricultural salesperson."],
            "field": ["farmer", "Water/Wastewater engineer", "Environmental engineer", "Zoologist"],
        }
    ],
}

career_questions = [
    "Q 1) What is your favorite subject? \n1. languages, 2. computer, 3. history, 4. biology, 5. chemistry, 6. maths 7. geography 8. agriculture: ",
    "Q 2) Do you like working in an office? ('Y' for yes and 'N' for no): ",
    "Q 3) Do you feel confident working with modern technology? ('Y' for yes and 'N' for no): ",
    ]

# print(list_of_careers["agriculture"][0]["office"])
answers = []
list_of_subjects = ["languages", "computer", "history", "biology", "chemistry", "maths", "geography", "agriculture"]
my_list = ["y", "n"]

print(advices[random.randint(0, len(advices))])

count = 0
for i in career_questions:
    if count < 1:
        question = input(i)
        while question not in list_of_subjects:
            print("error")
            question = input(i)
        answers.append(question)
        count += 1
    else:
        question = input(i)
        while question not in my_list:
            print("error")
            question = input(i).lower()
        if question == "y":
            question = "office"
        else:
            question = "field"
        answers.append(question)


if answers[2] == "office":
    print(f"You should consider being a {list_of_careers[answers[0]][0][answers[1]][random.randint(2, 3)]}")
else:
    print(f"You should consider being a {list_of_careers[answers[0]][0][answers[1]][random.randint(0, 1)]}")