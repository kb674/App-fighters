from random import choice, randint


def fighter_name():
    names = ['Paulita', 'Manna', 'Tillie', 'Lamprecht', 'Jayme', 'Fannin', 'Caleb', 'Moris', 'Sideny', 'Monte']
    surnames = ['Coombs', 'Gallows', 'Franzoni', 'Hoeppner', 'Costello', 'Scotti', 'Mellor', 'Lowenstein', 'Merino', 'Portier']
    nick_names = ["The Beast", "The Dentist", "Beauty and the Beast", "Angel of Death", "Sugar Free", "Ice Cold", "Shogun", "The Thunder", "The Dreamcatcher", "War Machine", "Was a Bullfrog", "Sick Dog", "Cheesesteak", "Cabbage", "Stinkyfeet", "The Word", "Gouda Gouda"]    
    return f"{choice(names)} '{choice(nick_names)}'' {choice(surnames)}"

def martial_art():
    martial_art = ['Boxing', 'Submission Grappling', 'MMA']
    return choice(martial_art)



def four():
    name = fighter_name()
    art = martial_art()
    ko = randint(5, 10)
    sub = randint(7, 14)

    qoute_list = ['I want to outlive my children.',"This is a rat race...but I ain't no rat. I'm a turtle. A ninja turtle.", "I have gained some weight, and it is affecting my car's fuel consumption.", "My grandma's 100 years old, I am 44 years old and I am in great shape."]
    qoute = choice(qoute_list)
    
    if art == "Boxing":
        return f"{name} \n{art} \n{ko} wins by KO \n'{qoute}'"
    elif art == "Submission Grappling":
        return f"{name} \n{art} \n{sub} wins by Submission \n'{qoute}'"
    elif art == "MMA":
        return f"{name} \n{art} \n{ko} wins by TKO and {sub} wins by Submission \n'{qoute}'"
    
    
    

print(four())

    

        










