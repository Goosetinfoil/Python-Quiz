print("Hello, My name is Bhaskar")
print("Before I start let me tell you a joke. Why does a Python live on land")
print("Beacuse it is above C level")
print(
    "Now on to the reason you came to this code to be part of my amazing, astonishing, stunning, stupefying, "
    "phenomenal, mind-blowing data collection system printer")
name = input("First of what is your name?\n")
age = input("Secondly, what is your age?\n")
nationality = input("Last but not least, where are you from?\n")
print("Ok great, so your name is " + name + " and you are " + age + " and you are from " + nationality + ".")


def category():
    score: int = 0
    x = input("Now chose a Category to answer questions:\nSports, General knowledge or Video Games\n")
    if x == "Sports":
        s: str = input("Now chose a sport to answer questions about:\nFootball(Soccer), Basketball, Volleyball, "
                       "Swimming,Rugby, Tennis, Cricket\n")
        if s == "Football" or s == "football":
            print("Let's start with the questions")
            f1 = input("Q1: How many people are there on a Football team?\n")
            if f1 == "11":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            f2 = input("Q2: Which country won the first world cup?\n")
            if f2 == "Uruguay" or f2 == "uruguay":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            f3 = input("Q3: Which manager was famously said to have given players 'the Hairdryer Treatment'?\n")
            if f3 == "Sir Alex Ferguson":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            print("Next 2 question are 'Who am I' question where you have to guess the player(Pls give their full name)")
            f4 = input("Q4: I've the number 7,playing my football across, England, Spain, Italy,Portugal,"
                       "Saudi Arabia.\n")
            if f4 == "Cristiano Ronaldo" or f4 == "cristiano ronaldo":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            f5 = input(
                "Q5: I have won six Premier League Player of the Month awards. I am Tottenham third highest all-time "
                "goalscorer.\n")
            if f5 == "Harry Kane" or f5 == "harry kane":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            print(score)
            print("That's the number of questions you got right")
        if s == "Basketball" or s == "basketball":
            print("Let's start with the questions")
            b1 = input("Q1: When was basketball invented?\n")
            if b1 == "1891":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            b2 = input("Q2: How long is a basketball game?\n")
            if b2 == "2 and a half hour" or b2 == "2 hours 30 mins":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            b3 = input("Q3: How many players on a basketball team?\n")
            if b3 == "12":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            b4 = input("Q4: Who won the NBA finals 2021?\n")
            if b4 == "Milwaukee Bucks" or b4 == "Bucks":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            b5 = input("Q5: When did Basketball become an Olympic Sport?\n")
            if b5 == "1936":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            print(score)
            print("That's the number of questions you got right")
        elif s == "Volleyball" or s == "volleyball":
            print("Let's start with the questions")
            v1 = input("Q1: How many people on each team are in court?\n")
            if v1 == "6":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            v2 = input("Q2: What was the original name of Volleyball?\n")
            if v2 == "Mintonette" or v2 == "mintonette":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            v3 = input("Q3: When was volleyball created?\n")
            if v3 == "1895":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            v4 = input("Q4: When was the first volleyball World Championships held?\n")
            if v4 == "1949":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            v5 = input("Q5: What is the number of times a team can hit a ball without passing it over the net?\n")
            if v5 == "3":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            print(score)
            print("That's the number of questions you got right")
        elif s == "Rugby" or s == "rugby":
            print("Let's start with the questions")
            r1 = input("Q1: What country was the the world cup final played at in 2003?\n")
            if r1 == "Australia" or r1 == "australia":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            r2 = input("Q2: Which team is known as the ‘Brave Blossoms’?\n")
            if r2 == "Japan" or r2 == "japan":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            r3 = input("Q3: Which team in the north of England is named after an insect?\n")
            if r3 == "Preston Grasshoppers":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            r4 = input("Q4: How do players leave the pitch after every game of rugby?\n")
            if r4 == "Players clap each other off through a tunnel":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            r5 = input("Q5: What color is the Fijian national Rugby shirt?\n")
            if r5 == "White" or r5 == "white":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            print(score)
            print("That's the number of questions you got right")
        elif s == "Cricket" or s == "cricket":
            print("Let's start with the questions")
            c1 = input("Q1: When was the first women’s cricket match recorded ?\n")
            if c1 == "1745":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            c2 = input("Q2: What does IPL stand for?\n")
            if c2 == "Indian Premier League" or c2 == "indian premier league":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            c3 = input("Q3: In which country did cricket originate?\n")
            if c3 == "England" or c3 == "england":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            c4 = input("Q4: When did India win their first World cup?\n")
            if c4 == "1983":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            c5 = input("Q5: What was the speed of the fastest ball ever bowled?\n")
            if c5 == "161" or c5 == "161.3":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            print(score)
            print("That's the number of questions you got right")
    if x == "General Knowledge":
        gk = input("Now choose History or Geography\n")
        if gk == "History" or "history":
            print("Let's start with the questions")
            h1 = input("Which civilization is considered the oldest civilization in the world?\n")
            if h1 == "Mesopotamia Civilization":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            h2 = input("When was Rome founded(Give the exact year and month. Date is optional)?\n")
            if h2 == "21 April 753 BC" or h2 == "April 753":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            h3 = input("When did the Chinese Revolution take place(when it started to when it ended?\n")
            if h3 == "1948-1952":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            h4 = input("Which country has the oldest Dynasty still ruling?\n")
            if h4 == "Japan" or h4 == "japan":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            h5 = input("Who is the father of History?\n")
            if h5 == "Herodotus" or h5 == "herodotus":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            print(score)
            print("That's the number of questions you got right")
        if gk == "Geography" or gk == "geography":
            print("Let's start with the questions")
            g1 = input("Which is the largest island in the world?\n")
            if g1 == "Greenland" or g1 == "greenland":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            g2 = input("Which is the world’s smallest country?\n")
            if g2 == "Vatican City" or g2 == "vatican city":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            g3 = input("How many countries are present in Africa?\n")
            if g3 == "54":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            g4 = input("Name the river that is not crossed by any bridges?\n")
            if g4 == "Amazon" or g4 == "amazon":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            g5 = input("Name the city that is located in two countries?\n")
            if g5 == "Istanbul" or g5 == "istanbul":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            print(score)
            print("That's the number of questions you got right")
    if x == "Video Games" or x == "video games":
        vg = input("Now choose from Minecraft or Chess")
        if vg == "Minecraft" or vg == "minecraft":
            print("Let's start with the questions")
            m1 = input("Name the three bosses of Minecraft(Give in alphabetical order,)?\n")
            if m1 == "Elder Guardian, Ender dragon, Wither" or m1 == "Elder Guardian,Ender dragon,Wither" or m1 == "elder guardian,ender dragon,wither":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            m2 = input("What is the best armor you can get in Minecraft?\n")
            if m2 == "Netherite" or m2 == "netherite":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            m3 = input("What is a block you can't break in Minecraft?\n")
            if m3 == "End portal Frame" or m3 == "end portal frame":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            print(score)
            print("That's the number of questions you got right")
        elif vg == "Chess" or vg == "chess":
            print("Let's start with the questions(Don't need to add the infront of your answer")
            ch1 = input("What do you have to protect in chess otherwise you lose?\n")
            if ch1 == "King" or ch1 == "king":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            ch2 = input("Which piece is the strongest in the game?\n")
            if ch2 == "Queen" or ch1 == "queen":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            ch3 = input("Which piece moves in a straight line?\n")
            if ch3 == "Rook" or ch1 == "rook":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            ch4 = input("Which piece moves diagonally?\n")
            if ch4 == "Bishop" or ch1 == "bishop":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            ch5 = input("Which piece can only kill diagonally?\n")
            if ch5 == "Pawn" or ch1 == "pawn":
                print("That's correct")
                score += 1
            else:
                print("That's wrong")
            print(score)
            print("That's the number of questions you got right")


willing = input("Before we move on I need to ask you if you are willing to answer questions about Sports, "
                "General knowledge or Video Game(Yes or No)?\n")
if willing == "Yes" or willing == "yes":
    print("Great now we can start")
    category()
    print("Thank you for taking part in my data collection system")
else:
    print("So you are not willing to answer question to improve your knowledge, fine no problem with me. You can "
          "leave this alone and move on with your life")