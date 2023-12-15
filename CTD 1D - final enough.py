# Libraries to Import
from math import *
import webbrowser, os, random, copy
import time #from ano

#github test
#Global Variables
exitvar = 0
menuPage = 0
dayCount = 0
hours = 0
hoursSpent = 0
hwFailCount = 0 # for annie
sleep = False
days = [['Monday', 6], ['Tuesday', 6], ['Wednesday', 6], ['Thursday', 6], ['Friday', 6], ['Saturday', 12], ['Sunday', 12]]
twocounter = 0
# stats = [20, 20, 20, 20, 20]
stats_orig = [['Money', 20.0],['Social', 20.0],['Knowledge',20.0],['Health (Physical)',20.0],['Health (Mental)', 20.0]]
stats = copy.deepcopy(stats_orig)
money = stats[0]
social = stats[1]
knowledge =stats[2]
physical = stats[3]
mental = stats[4]

#SUTD Tasks
tasksW1 = {
    'Physics Homework 1': 
        {
            'deadlineDay': 5,
            'req': 15,
            'status': False
            },
    'Math Homework 1': 
        {
            'deadlineDay': 7,
            'req': 25,
            'status': False
            }
}

tasksW2 = {
    'Physics Homework 2': 
        {
            'deadlineDay': 12,
            'req': 40,
            'status': False
            },
    'CTD Quiz 1': 
        {
            'deadlineDay': 14,
            'req': 53,
            'status': False 
            }
}

tasksW3 = {
    'Math Homework 2': 
        {
            'deadlineDay': 19,
            'req': 65,
            'status': False
            },
    'CTD Quiz 2': 
        {
            'deadlineDay': 21,
            'req': 75,
            'status': False
            }
}

tasksW4 = {
    'Physics Exam': 
        {
            'deadlineDay': 24,
            'req': 95,
            'status': False
            },
    'Math Exam': 
        {
            'deadlineDay': 26,
            'req': 100,
            'status': False
            }
}

#Functions
def clearOutput():
    os.system('cls')

def getDayNo():
    if dayCount <= 6 and dayCount >= 0:
        return dayCount
    elif dayCount > 6:
        return dayCount % 7 

def getHours(): #Function gets number of free hours according to the day list. This function must be called at the start of every day
    hours = days[getDayNo()][1]
    return hours


# game reset function - annie
def gameExit(exitvar, menuPage, dayCount, hours, hoursSpent, hwFailCount, twocounter, sleep, stats, stats_orig, money, social, knowledge, physical, mental):
    print('Would you like to try again?')
    print("[1] Try Again")
    print("[2] Exit")
    option = input("Select your option: ")
    clearOutput()
    if int(option) == 1:
        exitvar = 0
        dayCount = 0
        hours = 0
        hoursSpent = 0
        hwFailCount = 0 # for annie
        sleep = False
        twocounter = 0
        stats = copy.deepcopy(stats_orig)
        money = stats[0]
        social = stats[1]
        knowledge =stats[2]
        physical = stats[3]
        mental = stats[4]
        menuPage = 1
    elif int(option) == 2:
        exit() 
    else:
        print('Please select of the available options.')
        gameExit(exitvar, menuPage, dayCount, hours, hoursSpent, hwFailCount, twocounter, sleep, stats, stats_orig, money, social, knowledge, physical, mental)

# insta death check - annie
def deathCheck():
    deathcheck = money[1] < 0 or social[1] < 0 or physical[1] < 0 or mental[1] < 0 or hwFailCount >= 3
    return deathcheck

# what happens if u sudden death - annie
def suddenDeath(exitvar, menuPage, dayCount, hours, hoursSpent, hwFailCount, twocounter, sleep, stats, stats_orig, money, social, knowledge, physical, mental):
    print("===============================================================================\n")
    print("GAME OVER")
    if money[1] < 0:
        print("You don't have enough money to buy your next meal...")
    if social[1] < 0:
        print ('You became a shut-in...')
    if physical[1] < 0:
        print ('Oh no! You are no longer physically fit to continue studying...')
    if mental[1] < 0:
        print ('Uh oh... Due to mental health reasons, you might have met your untimely end...')
    if hwFailCount >= 3:
        print ('You were unable to academically sustain yourself in SUTD...Goodbye, my friend...')
    gameExit(exitvar, menuPage, dayCount, hours, hoursSpent, hwFailCount, twocounter, sleep, stats, stats_orig, money, social, knowledge, physical, mental)

def week():
    weekNo = ''
    if dayCount >=1 and dayCount<=7:
        weekNo = 'W1'
    elif dayCount >=8 and dayCount<=14:
        weekNo = 'W2'
    elif dayCount >=15 and dayCount<=21:
        weekNo = 'W3'
    elif dayCount >= 22 and dayCount<=28:
        weekNo = 'W4'
    return weekNo

def taskFailTest(hwFailCount): # annie 
    if week() == 'W1':
        for i in tasksW1:
            if tasksW1[i]['deadlineDay'] == dayCount:
                if knowledge[1] >= tasksW1[i]['req']:
                    tasksW1[i]['status'] = True
                    print("===============================================================================")
                    print('{} was due yesterday. Congratulations on successfully submitting your assignment!'.format(i))
                else:
                    hwFailCount += 1
                    print("===============================================================================")
                    print('{} was due yesterday. Unfortunately, you were unable to complete the assignment.'.format(i))
                    print('You currently have {} failed assignments.'.format(hwFailCount))
    elif week() == 'W2':
        for i in tasksW2:
            if tasksW2[i]['deadlineDay'] == dayCount:
                if knowledge[1] >= tasksW2[i]['req']:
                    tasksW2[i]['status'] = True
                    print("===============================================================================")
                    print('{} was due yesterday. Congratulations on successfully submitting your assignment!'.format(i))
                else:
                    hwFailCount += 1
                    print("===============================================================================")
                    print('{} was due yesterday. Unfortunately, you were unable to complete the assignment.'.format(i))
                    print('You currently have {} failed assignments.'.format(hwFailCount))
    elif week() == 'W3':
        for i in tasksW3:
            if tasksW3[i]['deadlineDay'] == dayCount:
                if knowledge[1] >= tasksW3[i]['req']:
                    tasksW3[i]['status'] = True
                    print("===============================================================================")
                    print('{} was due yesterday. Congratulations on successfully submitting your assignment!'.format(i))
                else:
                    hwFailCount += 1
                    print("===============================================================================")
                    print('{} was due yesterday. Unfortunately, you were unable to complete the assignment.'.format(i))
                    print('You currently have {} failed assignments.'.format(hwFailCount))
    # exam pass / fail test - for use in ending !!
    elif week == 'W4':
        for i in tasksW4:
            if tasksW4[i]['deadlineDay'] == dayCount:
                if knowledge[1] >= tasksW4[i]['req']:
                    tasksW4[i]['status'] = True

def done_status(week, task):
    if week[task]['status'] == False:
        return ("Not completed")
    elif week[task]['status'] == True:
            return ("Completed")
    option = input("Press enter to return")

# def task_complete(week, task):

#     if dayCount >= 0 and dayCount < 8-1:
#         week = tasksW1
#     if dayCount >= 8 and dayCount < 15-1:
#         week = tasksW2
#     if dayCount >= 15 and dayCount < 22-1:
#         week = tasksW3
#     if dayCount >= 22 and dayCount < 29-1:
#         week = tasksW4
#     if stats[2] >= week[task]['req']:
#         stats[2] = stats[2] - week[task]['req']
#         week[task]['status'] = True
#         return("Task has been completed successfully")
#     elif stats[2] < week[task]['req']:
#         return("Oh no! You don't meet the requirements to complete this task!")
#         ####GAME END####  #######NEED ANNOE'S CODE############

def taskDisplay():
    if week() == 'W1':
        for i in tasksW1:
            if dayCount+1 == tasksW1[i]['deadlineDay']:
                print('{} is due!'.format(i))
    elif week() == 'W2':
        for i in tasksW2:
            if dayCount+1 == tasksW2[i]['deadlineDay']:
                print('{} is due!'.format(i))
    elif week() == 'W3':
        for i in tasksW3:
            if dayCount+1 == tasksW3[i]['deadlineDay']:
                print('{} is due!'.format(i))
    elif week() == 'W4':
        for i in tasksW4:
            if dayCount+1 == tasksW4[i]['deadlineDay']:
                print('{} is here!'.format(i))

    # if dayCount+1 == 5:
    #     print("{Physics Homework 1} is due!")
    #     # task_complete(tasksW1, 'PhysicsHW1')
            
    # elif dayCount+1 == 7:
    #     print("Maths Homework 1 is due!")
    #     # task_complete(tasksW1, 'MathHW1')

    # elif dayCount+1 == 12:
    #     print("CTD Quiz 1 is due!")
    #     # task_complete(tasksW2, 'CTD_Quiz1')

    # elif dayCount+1 == 14:
    #     print("Physics Homework 2 is due!")
    #     # task_complete(tasksW2, 'PhysicsHW2')

    # elif dayCount+1 == 19:
    #     print("Maths Homework 2 is due!")
    #     # task_complete(tasksW3, 'MathHW2')

    # elif dayCount+1 == 21:
    #     print("CTD Quiz 2 is due!")
    #     # task_complete(tasksW3, 'CTD_Quiz2')

    # elif dayCount+1 == 24:
    #     print("Maths Exam is here!")
    #     # task_complete(tasksW4, 'Math Exam')

    # elif dayCount+1 == 26:
    #     print("Physics Exam is here!")
    #     # task_complete(tasksW4, 'Physics Exam')


def menu1():
    print("===============================================================================")
    print("                     WELCOME TO THE SUTD LIFE SIMULATOR     \n")
    print("In this game, you are an SUTDent. Your objective is to survive the onslaught \nthat is SUTD life. Good luck and godspeed. \n")
    print("===============================================================================\n")
    print("[1] Start Game")
    print("[2] Exit")
    
def menu2():
    print("===============================================================================")
    print(f"Day:{dayCount+1}, {days[getDayNo()][0]}                         Free Time: {hours}")
    # print("Placeholder text\n"+str(knowledge)) #Just using this to show the stats
    taskDisplay()
    print("===============================================================================\n")
    print("Actions (Hours will be subtracted off your free time)")
    print("[1] Study") #1 hour = 1 knowledge
    print("[2] Hang Out with Friends") #1 hour = 1 social
    print("[3] Exercise") #1 hour = 1 physical health
    print("[4] Go for Fifth Row") #1 hour = 0.5 knowledge + 0.5 social
    print("[5] Nap") #1 point = 1 mental
    print("===============================================================================\n")
    print("Miscellaneous Actions")
    print("[6] Check SUTDent Tasks")
    print("[7] Show Stats")
    print("[8] Instructions")
    print("[9] Sleep (End the Day)")

def tasks():
    ls_tasksW1 = list(tasksW1.keys())
    ls_tasksW2 = list(tasksW2.keys())
    ls_tasksW3 = list(tasksW3.keys())
    ls_tasksW4 = list(tasksW4.keys())
    print("\nYou have the following tasks:")
    print("===============================================================================")
    print("Week 1 Tasks:")
    print(ls_tasksW1[0])
    print("Deadline: Day {}".format(tasksW1[ls_tasksW1[0]]['deadlineDay']))
    print("Requirements: {} knowledge points".format(tasksW1[ls_tasksW1[0]]['req']))
    print("Status: {}".format(done_status(tasksW1, ls_tasksW1[0])))
    print("")
    print(ls_tasksW1[1])
    print("Deadline: Day {}".format(tasksW1[ls_tasksW1[1]]['deadlineDay']))
    print("Requirements: {} knowledge points".format(tasksW1[ls_tasksW1[1]]['req']))
    print("Status: {}".format(done_status(tasksW1, ls_tasksW1[1])))
    print("")
    print("===============================================================================")
    print("Week 2 Tasks:")
    print(ls_tasksW2[0])
    print("Deadline: Day {}".format(tasksW2[ls_tasksW2[0]]['deadlineDay']))
    print("Requirements: {} knowledge points".format(tasksW2[ls_tasksW2[0]]['req']))
    print("Status: {}".format(done_status(tasksW2, ls_tasksW2[0])))
    print("")
    print(ls_tasksW2[1])
    print("Deadline: Day {}".format(tasksW2[ls_tasksW2[1]]['deadlineDay']))
    print("Requirements: {} knowledge points".format(tasksW2[ls_tasksW2[1]]['req']))
    print("Status: {}".format(done_status(tasksW2, ls_tasksW2[1])))
    print("")
    print("===============================================================================")
    print("Week 3 Tasks:")
    print(ls_tasksW3[0])
    print("Deadline: Day {}".format(tasksW3[ls_tasksW3[0]]['deadlineDay']))
    print("Requirements: {} knowledge points".format(tasksW3[ls_tasksW3[0]]['req']))
    print("Status: {}".format(done_status(tasksW3, ls_tasksW3[0])))
    print("")
    print(ls_tasksW3[1])
    print("Deadline: Day {}".format(tasksW3[ls_tasksW3[1]]['deadlineDay']))
    print("Requirements: {} knowledge points".format(tasksW3[ls_tasksW3[1]]['req']))
    print("Status: {}".format(done_status(tasksW3, ls_tasksW3[1])))
    print("")
    print("===============================================================================")
    print("Week 4 Tasks:")
    print(ls_tasksW4[0])
    print("Deadline: Day {}".format(tasksW4[ls_tasksW4[0]]['deadlineDay']))
    print("Requirements: {} knowledge points".format(tasksW4[ls_tasksW4[0]]['req']))
    print("Status: {}".format(done_status(tasksW4, ls_tasksW4[0])))
    print("")
    print(ls_tasksW4[1])
    print("Deadline: Day {}".format(tasksW4[ls_tasksW4[1]]['deadlineDay']))
    print("Requirements: {} knowledge points".format(tasksW4[ls_tasksW4[1]]['req']))
    print("Status: {}".format(done_status(tasksW4, ls_tasksW4[1])))
    print("===============================================================================\n")
    option = input('Press Enter to continue: ')

#Random events
def Bobsbirthday():
    print("===============================================================================\n")
    print("You got a last minute invite to Bob's birthday!\n")
    print("You gained 5 mental and social points!\n")
    cont = input('Press enter to continue: ')
    mental[1] += 5
    social[1] += 5
def physicsremedial():
    print("===============================================================================\n")
    print("You went for a physics remedial because your physics is baddd.\n")
    print("Franklin - Your knowledge of physics concepts went up by 5! \n")
    cont = input('Press enter to continue: ')
    knowledge[1] += 5
    mental[1] += -5    
def headverypain():
    print("===============================================================================\n")
    print("Oh nooo you have a terrible headache!!!\n")
    print("Your mental health goes down by 5!\n")
    cont = input('Press enter to continue: ')
    mental[1] += -5    
def adhocrun():
    print("===============================================================================\n")
    print("Bob has invited you for a short run around SUTD!\n")
    print("Your physical health goes up by 5!\n")
    cont = input('Press enter to continue: ')
    physical[1] += 5   
def glassesbroke():
    print("===============================================================================\n")
    print("Ooops your glasses broke, you can study no more! Haha..\n")
    print("Your knowledge goes down by 5!\n")
    cont = input('Press enter to continue: ')
    knowledge[1] += -5   
def ifartinurface():
    print("===============================================================================\n")
    print("You accidentally took a shit in class!!!!\n")
    print("Social points minus 10\n")
    cont = input('Press enter to continue: ')
    social[1] += -10
def guessinggamez():
    print("===============================================================================\n")
    guess_the_number()
    cont = input('Press enter to continue: ')
def papaDied():
    print("===============================================================================\n")
    print("Oh Bummerrrrrrr, your Grandpa has passed away.\n")
    print("Your mental health has taken a hit of -20.\n")
    cont = input('Press enter to continue: ')
    mental[1] += -15

def wrongSideOfBed():
    print("===============================================================================\n")
    print("Oh no, you woke up on the wrong side of the bed.\n")
    print("Your physical health and mental health take a hit of -5.\n")
    cont = input('Press enter to continue: ')
    physical[1] += -5
    mental[1] += -5

def python_in_ceiling():
    print("===============================================================================\n")
    print("Oh no! a python fell through your ceiling.\n")
    print("Your physical health has taken a hit of -5.\n")
    print("Your mental health has taken a hit of -5.\n")
    cont = input('Press enter to continue: ')
    mental[1] += -5
    physical[1] += -5
    
def fall_into_drain():
    print("===============================================================================\n")
    print("Oh no! you fell into a drain on your way to school.\n")
    print("Your physical health has taken a hit of -5.\n")
    cont = input('Press enter to continue: ')
    physical[1] += -5
def concussion():
    print("===============================================================================\n")
    print("Oh no! You hit your head and got a concussion.\n")
    print("Your physical health has taken a hit of -5.\n")
    print("Your knowledge has taken a hit of -5.\n")
    cont = input('Press enter to continue: ')
    knowledge[1] += -5
    physical[1] += -5
    
def extranotes():
    print("===============================================================================\n")
    print("Yay! you found notes that will help you in the upcoming test.\n")
    print("Your knowledge increased by 10.\n")
    cont = input('Press enter to continue: ')
    knowledge[1] += 10
def newfriend():
    print("===============================================================================\n")
    print("Yay! you made friends with someone you accidentally bump into on the way to school.\n")
    print("Your social level increase by 5.\n")
    cont = input('Press enter to continue: ')
    social[1] += 10

## number game function
def guess_the_number():
    secret_number = random.randint(1, 10)
    attempts = 0
    print("You have been asked to guessed a number between 1 to 10, you have 3 tries! \nIf you fail, you looseeeee haha.\n")
    i = 0
    while attempts < 3 and i == 0:
        guess = int(input("Please input your number! "))
        attempts += 1
        print(f"Attempt number: {attempts}")
        if guess == secret_number:
            print(f"Congratulations! the right number is {secret_number} \n5 socials points to you!")
            social[1] += 5
            i = 1
            # attempt = 4
            return
        elif guess < secret_number:
            print("Too low. Try again.")
            
        elif guess > secret_number:
            print("Too high. Try again.")
        elif guess == None:
            print("You didnt guess a number.")           
    if attempts == 3:
        print("Sorry, you lost the game, minus 5 social points for youn")
        social[1] += -5


events = {
    1: 'papaDied',
    2: 'wrongSideOfBed', 
    3: 'Bobsbirthday', 
    4: 'physicsremedial', 
    5: 'headverypain', 
    6: 'adhocrun', 
    7: 'glassesbroke', 
    8: 'ifartinurface', 
    9: 'ifartinurface', 
    10: 'guessinggamez',
    11: 'python_in_ceiling', 
    12: 'fall_into_drain', 
    13: 'concussion', 
    14: 'extranotes',
    15: 'newfriend'
    # 15: ''
    } #Put your event name (without the () into this dictionary using the same format

# events = [papaDied()'',wrongSideOfBed()]
# randEvent = random.randint(1,len(events))
# print(events[1])
# function_name = events[randEvent]
# result = eval(function_name + "()")



#Endings

#social=social[1]
social_ending = {1: 'IT Girl / IT boy !! everybody wanna be you ', 2: 'You are well-liked by many! Congrats', 3: 'You made some friends and fit in okay', 4:'You only have a few friends and thats fine :)', 5:'Oh no... you are a loner :('}
def socialEnding():
    if social[1]>100:
        return (social_ending [1])
    elif social[1]>=85:
        return (social_ending [2])
    elif social[1]>=50:
        return (social_ending [3])
    elif social[1]>=30:
        return (social_ending [4])
    elif social[1]>=0:
        return (social_ending [5])
    else:
        return (None)
    pass


#knowledge =knowledge[1]
knowledge_ending = {1: 'otw to become valedictorian', 2: 'graduated with honors', 3: 'graduated with average results ', 4:'barely graduated', 5:'dropped out of SUTD'}
def knowEnding():
    if knowledge[1]>100:
        return (knowledge_ending [1])
    elif knowledge[1]>=85:
        return (knowledge_ending [2])
    elif knowledge[1]>=50:
        return (knowledge_ending [3])
    elif knowledge[1]>=30:
        return (knowledge_ending [4])
    elif knowledge[1]>=0:
        return (knowledge_ending [5])
    else:
        return (None)
    pass

    
#Physical =physical[1]
physicalhealth_ending = {1: 'DAMN you have a sexy and fit body !', 2: 'wow... have you been working out?', 3: 'You have an average body :) ', 4:'You have been quite sickly these days!', 5:'OH NO!! you have to be hospitalised'}
def phyEnding():
    if physical[1]>100:
        return (physicalhealth_ending [1])
    elif physical[1]>=85:
        return (physicalhealth_ending [2])
    elif physical[1]>=50:
        return (physicalhealth_ending [3])
    elif physical[1]>=30:
        return (physicalhealth_ending [4])
    elif physical[1]>=0:
        return (physicalhealth_ending [5])
    else:
        return (None)
    pass
    
#Mental =mental[1]
emotionalhealth_ending = {1: 'You always have a great peace of mind', 2: 'You mostly live a peaceful life in SUTD', 3: 'You struggle at times due to stress and work ', 4:'You suffer from many panic attacks and anxiety :( ', 5:'Knock knock... IMH is calling'}
def emoEnding():
    if mental[1]>100:
        return (emotionalhealth_ending [1])
    elif mental[1]>=85:
        return (emotionalhealth_ending [2])
    elif mental[1]>=50:
        return (emotionalhealth_ending [3])
    elif mental[1]>=30:
        return (emotionalhealth_ending [4])
    elif mental[1]>=0:
        return (emotionalhealth_ending [5])
    else:
        return (None)
    pass


while exitvar == 0:    
    while menuPage == 1:
        try:
            hours = days[getDayNo()][1] - hoursSpent
            clearOutput()
            randNo =random.randint(0,100)
            if randNo > 35 and sleep == True:
                sleep = False
                randEvent = random.randint(1,len(events))
                function_name = events[randEvent]
                result = eval(function_name + "()")
            taskFailTest(hwFailCount)
            deathcheck = deathCheck()
            if deathcheck == True:
                suddenDeath(exitvar, menuPage, dayCount, hours, hoursSpent, hwFailCount, twocounter, sleep, stats, stats_orig, money, social, knowledge, physical, mental)
                break
            # print(f'DayCount = {dayCount}')
            # print(f'getDayNo = {getDayNo()}')
            menu2()
            # print(stats)
            option = int(input("Select your option: ")) 

            if option == 1: #Study
                menuPage = 'Study'

            elif option == 2: #Friends
                menuPage = 'Friends'

            elif option == 3: #Exercise
                menuPage = 'Exercise'

            elif option == 4: #Fifth Row
                menuPage = '5Row'

            elif option == 5: #Nap
                menuPage = 'Nap'

            elif option == 6: #Check Tasks
                menuPage = 'Tasks'

            elif option == 7: #Show Stats
                menuPage = 'Statss'

            elif option == 8: #Instructions
                menuPage = 'Instructions'

            elif option == 9:
                sleep = True
                taskFailTest(hwFailCount)
                dayCount += 1
                hours = getHours()
                hoursSpent = 0
                if dayCount == 28: # to get ending
                    clearOutput()
                    print("===============================================================================")
                    print('THANK YOU FOR PLAYING!')
                    print('THE GAME HAS ENDED')
                    print("===============================================================================")
                    print(phyEnding())
                    print(emoEnding())
                    print(socialEnding())
                    print(knowEnding())
                    print("===============================================================================")
                    print('You have reached the end of the game')
                    print(input('Press enter to continue.'))
                    gameExit(exitvar, menuPage, dayCount, hours, hoursSpent, hwFailCount, twocounter, sleep, stats, stats_orig, money, social, knowledge, physical, mental)

        except ValueError:
            print("Please choose enter an option shown above")

    while menuPage == 0:
        try:
            menu1()
            option = input("Select your option: ")
            clearOutput()
            if int(option) == 1:
                webbrowser.open('https://www.youtube.com/watch?v=oZAGNaLrTd0')
                menuPage +=1 
            elif int(option) == 2:
                twocounter +=1
                if twocounter == 1:
                    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUJcmljayByb2xs')
                    print("===============================================================================\n")
                    print("HA. You thought you could escape!? WELL YOU THOUGHT WRONG MUAHAHAHAHAHAHAHA!\n") 
                elif twocounter >= 2:
                    print("===============================================================================\n")
                    print(f"Seriously?????? You have pressed the same option {twocounter} times. Don't you have \nsomething better to do with your life?\n")
        except ValueError:
            print("Please choose enter an option shown above")

                

    

    while menuPage == 'Study':
        try:
            # os.system('cls')
            # clear_output(wait=True) #This line clears previous outputs
            clearOutput()
            print("===============================================================================\n")
            print(f'You have {hours} free hours')
            # print(knowledge)
            option = int(input("How many hours do you want to study for? (Enter 0 to go back): "))
            if option <= hours and option >= 0 or option == '':
                hoursSpent += option
                knowledge[1] += float(option)
                menuPage = 1
        except ValueError:
            print("Please input a whole number.")

    while menuPage == 'Friends':
        try:
            # os.system('cls')
            # clear_output(wait=True) #This line clears previous outputs
            clearOutput()
            print("===============================================================================\n")
            print(f'You have {hours} free hours')
            # print(social)
            option = int(input("How long do you want to spend with your friends (hours)? (Enter 0 to go back): "))
            if option <= hours and option >= 0 or option == '':
                hoursSpent += option
                social[1] += float(option)
                menuPage = 1
        except ValueError:
            print("Please input a whole number.")

    while menuPage == 'Exercise':
        try:
            # os.system('cls')
            # clear_output(wait=True) #This line clears previous outputs
            clearOutput()
            print("===============================================================================\n")
            print(f'You have {hours} free hours')
            # print(physical)
            option = int(input("How long do you want to exercise? (Enter 0 to go back): "))
            if option <= hours and option >= 0 or option == '':
                hoursSpent += option
                physical[1] += float(option)
                menuPage = 1
        except ValueError:
            print("Please input a whole number.")

    while menuPage == '5Row':
        try:
            # os.system('cls')
            # clear_output(wait=True) #This line clears previous outputs
            clearOutput()
            print("===============================================================================\n")
            print(f'You have {hours} free hours')
            # print(knowledge)
            option = int(input("How many hours do you want to study for? (Enter 0 to go back): "))
            if option <= hours and option >= 0 or option == '':
                hoursSpent += option
                knowledge[1] += float(option) /2
                social[1] += float(option) /2
                menuPage = 1
        except ValueError:
            print("Please input a whole number.")

    while menuPage == 'Nap':
        try:
            # os.system('cls')
            # clear_output(wait=True) #This line clears previous outputs
            clearOutput()
            print("===============================================================================\n")
            print(f'You have {hours} free hours')
            # print(mental)
            option = int(input("How many hours do you want to nap for? (Enter 0 to go back): "))
            if option <= hours and option >= 0 or option == '':
                hoursSpent += option
                mental[1] += float(option)
                menuPage = 1
        except ValueError:
            print("Please input a whole number.")

    while menuPage == 'Tasks':
        # os.system('cls')
        # clear_output(wait=True) #This line clears previous outputs
        clearOutput()
        tasks()
        menuPage = 1

    while menuPage == 'Statss': #A menu option number
        #Change some stats
        clearOutput()
        print("===============================================================================\n")
        print("Here are Your Stats!")
        # print("Your money stats are: {}".format(money[1])) 
        print("Your social stats are: {}".format(social[1]))
        print("Your knowledge stats are: {}".format(knowledge[1])) 
        print("Your physical health stats are: {}".format(physical[1])) 
        print("Your mental health stats are: {}".format(mental[1]))
        option = input("Press enter to return ")
        menuPage = 1

### Rebs part
    while menuPage == 'Instructions': #A menu option number
        try:
            #Change some stats
            clearOutput()
            print("===============================================================================\n"
                  "                     HOW TO PLAY THE SUTD LIFE SIMULATOR                       \n"
                  "===============================================================================\n"
                  "MAIN OBJECTIVE\n\n"
                  "Complete all your tasks and survive the SUTDent life.\n\n"
                  "-------------------------------------------------------------------------------\n"
                  "TASKS\n\n"
                  "For the entire duration of the game, there is a list of tasks that you have to\n"
                  "do in order to graduate successfully as a SUTDent. If you do not complete these\n"
                  "tasks, you will be EXPELLED!!!\n\n"
                  "-------------------------------------------------------------------------------\n"
                  "TIME\n\n"
                  "There is a limited amount of time(hours) that you have in each day of the game.\n"
                  "and a set of actions that you can choose to do with that time. It's up to you \n"
                  "to decide on how you want to use your free time. \n\n"
                  "-------------------------------------------------------------------------------\n"
                  "HOW TO GAIN POINTS\n\n"
                  "[1] Study: 1 Hour = 1 Knowledge\n"
                  "[2] Hang Out with Friends: 1 Hour = 1 Social\n" 
                  "[3] Exercise: 1 Hour = 1 Physical Health\n" 
                  "[4] Go for Fifth Row: 1 Hour = 0.5 Knowledge + 0.5 Social\n"
                  "[5] Nap: 1 Hour = 1 Mental\n\n"
                  "-------------------------------------------------------------------------------\n"
                  "RANDOM EVENTS\n\n"
                  "At the start of each day, there can be a random event that will be thrown at you.\n"
                  "It can affect your statistics either positively or negatively, and there is nothing\n"
                  "you can do about it. Welcome to the uncertainties of life!\n\n"
                  "-------------------------------------------------------------------------------\n"
                  "HOW TO QUIT\n\n"
                  "If you want to drop out of SUTD (or in other words, stop playing), feel free to\n"
                  "to end the kernel.\n\n"
                  "===============================================================================\n\n")
            option = input("Press enter to return ")
            menuPage = 1
        except ValueError:
            print('something')




