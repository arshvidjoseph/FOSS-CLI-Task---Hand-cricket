import random
import mysql.connector as m
con=m.connect(host="localhost",user="root",password="student")
c=con.cursor()
c.execute("CREATE DATABASE IF NOT EXISTS ArshvidFOSS")
c.execute("USE ArshvidFOSS")
c.execute("""CREATE TABLE IF NOT EXISTS results(
        match_id INT AUTO_INCREMENT PRIMARY KEY,
        toss_winner VARCHAR(20),
        game_winner VARCHAR(20),
        your_score INT,
        computer_score INT,
        played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
con.commit()
con.close()
def score(tw,gw,s,s1):
    con=m.connect(host="localhost",user="root",password="student",database="ArshvidFOSS")
    c=con.cursor()
    q='INSERT INTO results(toss_winner, game_winner, your_score, computer_score) VALUES ("{}","{}",{},{})'.format(tw,gw,s,s1)
    c.execute(q)
    con.commit()
    con.close()
def view_score():
    con=m.connect(host="localhost",user="root",password="student",database="ArshvidFOSS")
    c=con.cursor()
    c.execute("""SELECT match_id, toss_winner, game_winner, your_score, computer_score, played_at
        FROM results
        ORDER BY match_id DESC""")
    r=c.fetchall()
    print("\n"+"="*90)
    print("MATCH HISTORY")
    print("="*90)
    if len(r)==0:
        print("No match records found.")
    else:
        for i in r:
            print("Match ID:",i[0])
            print("Toss winner:",i[1])
            print("Game winner:",i[2])
            print("Your score:",i[3])
            print("Computer score:",i[4])
            print("Played at:",i[5])
            print("-"*90)
    con.close()
def startgame():
    x=input("Select Head or Tails(H/T):")
    a=random.randint(1,2)
    if a==1:
        y="H"
    else:
        y="T"
    if x.upper()==y:
        print("You won the toss","\n")
        tw="You"
        w=input("You would like bat or bowl(B/BO):")
        while w.upper() not in ["B","BO"]:
            print("INVALID CHOOSE , CHOOSE AGAIN")
            w=input("You would like bat or bowl(B/BO):")
        if w.upper()=="B":
            print("You choose batting","\n")
            s=0
            s1=0
            while True:
                i=random.randint(1,6)
                print("Computer has choose its number , now its your turn","\n")
                j=int(input("Enter a random number from 1-6(including 1 and 6):"))
                if j==i:
                    print("OUTTTT!!!!")
                    break
                else:
                    if j==1:
                        print("Single")
                        s+=1
                    elif j==2:
                        print("2 runs . Good running between the wickets")
                        s+=2
                    elif j==3:
                        print("3 runs!! . Thats absolute brilliant running between the wicket")
                        s+=3
                    elif j==4:
                        print("And thats in the gap , 4 runs")
                        s+=4
                    elif j==5:
                        print("Poor from the bowler , 5 runs")
                        s+=5
                    else:
                        print("And thats a six")
                        s+=6
            print("Its computers turns to bat")
            print("Computer needs",s-s1+1,"runs to win")
            while True:
                i=random.randint(1,6)
                print("Computer has choose its number , now its your turn","\n")
                j=int(input("Enter a random number from 1-6(including 1 and 6):"))
                if j==i:
                    print("OUTTTT!!!!")
                    break
                else:
                    if j==1:
                        print("Single")
                        s1+=1
                    elif j==2:
                        print("2 runs . Good running between the wickets")
                        s1+=2
                    elif j==3:
                        print("3 runs!! . Thats absolute brilliant running between the wicket")
                        s1+=3
                    elif j==4:
                        print("And thats in the gap , 4 runs")
                        s1+=4
                    elif j==5:
                        print("Poor from the bowler , 5 runs")
                        s1+=5
                    else:
                        print("And thats a six")
                        s1+=6
                    if s1>s:
                        break
                    print("Computer needs",s-s1+1,"runs to win")
            print("Your score:",s)
            print("Computer score:",s1)
            if s>s1:
                print("YEAHHHHH , YOU WON !!!!!!!!")
                gw="You"
            elif s1>s:
                print("NAHHHH , YOU LOST :((((((")
                gw="Computer"
            else:
                print("Match tied :/")
                gw="Tie"
        else:
            print("You choose bowling")
            s=0
            s1=0
            while True:
                i=random.randint(1,6)
                print("Computer has choose its number , now its your turn","\n")
                j=int(input("Enter a random number from 1-6(including 1 and 6):"))
                if j==i:
                    print("OUTTTT!!!!")
                    break
                else:
                    if j==1:
                        print("Single")
                        s1+=1
                    elif j==2:
                        print("2 runs . Good running between the wickets")
                        s1+=2
                    elif j==3:
                        print("3 runs!! . Thats absolute brilliant running between the wicket")
                        s1+=3
                    elif j==4:
                        print("And thats in the gap , 4 runs")
                        s1+=4
                    elif j==5:
                        print("Poor from the bowler , 5 runs")
                        s1+=5
                    else:
                        print("And thats a six")
                        s1+=6
            print("Its your turn to bat")
            print("You need",s1-s+1,"runs to win")
            while True:
                i=random.randint(1,6)
                print("Computer has choose its number , now its your turn","\n")
                j=int(input("Enter a random number from 1-6(including 1 and 6):"))
                if j==i:
                    print("OUTTTT!!!!")
                    break
                else:
                    if j==1:
                        print("Single")
                        s+=1
                    elif j==2:
                        print("2 runs . Good running between the wickets")
                        s+=2
                    elif j==3:
                        print("3 runs!! . Thats absolute brilliant running between the wicket")
                        s+=3
                    elif j==4:
                        print("And thats in the gap , 4 runs")
                        s+=4
                    elif j==5:
                        print("Poor from the bowler , 5 runs")
                        s+=5
                    else:
                        print("And thats a six")
                        s+=6
                    if s>s1:
                        break
                    print("You need",s1-s+1,"runs to win")
            print("Your score:",s)
            print("Computer score:",s1)
            if s>s1:
                print("YEAHHHHH , YOU WON !!!!!!!!")
                gw="You"
            elif s1>s:
                print("NAHHHH , YOU LOST :((((((")
                gw="Computer"
            else:
                print("Match tied :/")
                gw="Tie"
    else:
        print("You lost the toss","\n")
        tw="Computer"
        u=random.randint(1,2)
        if u==1:
            k="BO"
        else:
            k="B"
        s=0
        s1=0
        if k=="BO":
            print("Computer choose bowling")
            while True:
                i=random.randint(1,6)
                print("Computer has choose its number , now its your turn","\n")
                j=int(input("Enter a random number from 1-6(including 1 and 6):"))
                if j==i:
                    print("OUTTTT!!!!")
                    break
                else:
                    if j==1:
                        print("Single")
                        s+=1
                    elif j==2:
                        print("2 runs . Good running between the wickets")
                        s+=2
                    elif j==3:
                        print("3 runs!! . Thats absolute brilliant running between the wicket")
                        s+=3
                    elif j==4:
                        print("And thats in the gap , 4 runs")
                        s+=4
                    elif j==5:
                        print("Poor from the bowler , 5 runs")
                        s+=5
                    else:
                        print("And thats a six")
                        s+=6
            print("Its computers turn to bat")
            print("Computer needs",s-s1+1,"runs to win")
            while True:
                i=random.randint(1,6)
                print("Computer has choose its number , now its your turn","\n")
                j=int(input("Enter a random number from 1-6(including 1 and 6):"))
                if j==i:
                    print("OUTTTT!!!!")
                    break
                else:
                    if j==1:
                        print("Single")
                        s1+=1
                    elif j==2:
                        print("2 runs . Good running between the wickets")
                        s1+=2
                    elif j==3:
                        print("3 runs!! . Thats absolute brilliant running between the wicket")
                        s1+=3
                    elif j==4:
                        print("And thats in the gap , 4 runs")
                        s1+=4
                    elif j==5:
                        print("Poor from the bowler , 5 runs")
                        s1+=5
                    else:
                        print("And thats a six")
                        s1+=6
                    if s1>s:
                        break
                    print("Computer needs",s-s1+1,"runs to win")
            print("Your score:",s)
            print("Computer score:",s1)
            if s>s1:
                print("YEAHHHHH , YOU WON !!!!!!!!")
                gw="You"
            elif s1>s:
                print("NAHHHH , YOU LOST :((((((")
                gw="Computer"
            else:
                print("Match tied :/")
                gw="Tie"
        else:
            print("Computer choose bating")
            while True:
                i=random.randint(1,6)
                print("Computer has choose its number , now its your turn","\n")
                j=int(input("Enter a random from 1-6(including 1 and 6):"))
                if j==i:
                    print("OUTTTT!!!!")
                    break
                else:
                    if j==1:
                        print("Single")
                        s1+=1
                    elif j==2:
                        print("2 runs . Good running between the wickets")
                        s1+=2
                    elif j==3:
                        print("3 runs!! . Thats absolute brilliant running between the wicket")
                        s1+=3
                    elif j==4:
                        print("And thats in the gap , 4 runs")
                        s1+=4
                    elif j==5:
                        print("Poor from the bowler , 5 runs")
                        s1+=5
                    else:
                        print("And thats a six")
                        s1+=6
            print("Its your turns to bat")
            print("You need",s1-s+1,"runs to win")
            while True:
                i=random.randint(1,6)
                print("Computer has choose its number , now its your turn","\n")
                j=int(input("Enter a random numberfrom 1-6(including 1 and 6):"))
                if j==i:
                    print("OUTTTT!!!!")
                    break
                else:
                    if j==1:
                        print("Single")
                        s+=1
                    elif j==2:
                        print("2 runs . Good running between the wickets")
                        s+=2
                    elif j==3:
                        print("3 runs!! . Thats absolute brilliant running between the wicket")
                        s+=3
                    elif j==4:
                        print("And thats in the gap , 4 runs")
                        s+=4
                    elif j==5:
                        print("Poor from the bowler , 5 runs")
                        s+=5
                    else:
                        print("And thats a six")
                        s+=6
                    if s>s1:
                        break
                    print("You need",s1-s+1,"runs to win")
            print("Your score:",s)
            print("Computer score:",s1)
            if s>s1:
                print("YEAHHHHH , YOU WON !!!!!!!!")
                gw="You"
            elif s1>s:
                print("NAHHHH , YOU LOST :((((((")
                gw="Computer"
            else:
                print("Match tied :/")
                gw="Tie"
    score(tw,gw,s,s1)
def menu():
    while True:
        print("\n"+"="*50)
        print("HAND CRICKET MENU")
        print("="*50)
        print("1. Start Game")
        print("2. View Scores")
        print("3. Exit")
        ch=input("Enter your choice: ")
        if ch=="1":
            startgame()
        elif ch=="2":
            view_score()
        elif ch=="3":
            print("Thank you for playing Hand Cricket!")
            break
        else:
            print("Invalid choice. Please try again.")
menu()
