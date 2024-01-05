def choosecountry(country):
  if(country=="India"):
    players=["Rohit Sharma","Shubman Gill","Virat Kohli","Shreyas Iyer","KL Rahul","Hardik Pandya","Ravindra Jadeja","Mohammed Shami",
           "Kuldeep Yadav","Jasprit Bumrah","Mohammed Siraj"]
  elif(country=="Australia"):
    players=["David Warner","Travis Head","Mitchell Marsh","Steven Smith","Marnus Labuchagne","Glenn Maxwell","Josh Inglis","Mitchell Starc",
           "Pat cummins","Adam Zampa","Josh Hazlewood"]
  elif(country=="England"):
    players=["Jos Butler","Johny Bairstow","Harry Brook","Ben Stokes","Liam Livingstone","Moeen Ali","Sam Curran","Chris Woakes","Adil Rashid","Mark Wood","Reece Topley"]
  elif(country=="South Africa"):
    players=["Quinton De Cock","Reeza Hendricks","Rassie VanderDussen","Aiden Markram","Henreich Klassen","David Miller","Marco Jansen","Gerald Coetzee","Keshav Maharaj","Kaghiso Rabada","Lungi Ngidi"]
  elif(country=="pakisthan"):
    players=["Fakhar Zaman","Mohammed Rizwan","Babar Azam","Shan Masood","Ifthikhar Ahmmed","Asif Ali","Mohammed Nawaz","Shadab Khan","Haris Rauf","Shaheen Afridi","Naseem Shah"]
  elif(country=="New Zealand"):
    players=["Devon Conway","Rachin Ravindra","Kane Williamson","Daryl Mitchell","Glenn Phillips","James Neesham","Mark Chapman","Mitchell Santner","Tim Southee","Trent Boult","Lockie Ferguson"]
  elif(country=="Sri Lanka"):
    players=["Pathum Nissanka","Kusal Perera","Kusal Mendis","Sadeera Samarawickrama","Charith Assalanka","Dhananjaya De Silva","Wanindu Hasaranga","Maheesh Theekshana","Dushmanta Chammera","Kasun Rajitha","Dilshan Madushanka"]
  elif(country=="bangladesh"):
    players=["Liton Das","Soumya Sarkar","Najmul Hossain Shanto","Shakib Al Hasan","Mushfiqiur Rahman","Mahmadullah","Mehidi Hasan Miraz","Mahedi Hasan","Taskin Ahmed","Mustafizur Rahman","Shoriful Islam"]
  return players

def playersinput():
  answer=True
  while(type(answer)!=int):
    st=input("Enter 0 to 6: ")
    if(st.isdigit()==True and int(st)>=0 and int(st)<7):
      answer=int(st)
    else:
      print("Invalid Entry! ")
      print("")
  return answer

import random as r

players=["Jos Butler","Johny Bairstow","Harry Brook","Ben Stokes","Liam Livingstone","Moeen Ali","Sam Curran","Chris Woakes","Adil Rashid","Mark Wood","Reece Topley"]

bowling=[0,0,0,0,0,1,1,1,1,1,1]
bowling="ben stokes"
def bowlindex(bowl):
  for i in players:
    if(i.islower()==bowling.islower()):
      return players.index(i)

bowler=bowlindex()
def checkbowling(bowler):
  if(bowling[bowler]==0):
    return False
  else:
    return True



def maxlength(players):
  lst=[]
  for i in players:
    lst+=[len(i)]
  return max(lst)

maxlength(players)

k=0
l=1
score=[0,0,0,0,0,0,0,0,0,0,0]
balls=[0,0,0,0,0,0,0,0,0,0,0]
strike=0
score1=0
score2=0
ball1=0
ball2=0
runsperover=[]
batsman1=players[k]
batsman2=players[l]
noofballs=0
noofruns=0
maxballs=120
wkt=0
for i in range(1,21):
  if(wkt==10):
    break
  noofrunsperover=0
  for j in range(1,7):
    indicator=0
    if(wkt==10):
      break
    if(noofballs>=maxballs):
      break
    playerinput=playersinput()
    if(playerinput>6 and playerinput<0):
      print("Invalid Entry")
      print("")
    else:
      compbowl=r.randrange(1,7)
      if(compbowl==playerinput):
        wkt+=1
        noofballs+=1
        playerinput=0
        indicator=1
        if(strike==0):
          print("")
          print(batsman1," ",score1,"(",ball1+1,") Out Gone!",sep="")
          print("")
          score[k]=score1
          balls[k]=ball1+1
          k=max(k,l)+1
          score1=0
          ball1=0
        else:
          print(batsman2," ",score2,"(",ball2+1,") Out Gone!",sep="")
          print("")
          score[l]=score2
          balls[l]=ball2+1
          l=max(k,l)+1
          score2=0
          ball2=0
      else:
        if(playerinput==0):
            r1=r.randrange(1,5)
            print("")
            if(r1==1):
              print("Commentator: Rock Solid Defence from the batsman!")
            elif(r1==2):
              print("Commentator: That's a gem of a delivery! Beats the Batsman")
            elif(r1==3):
              print("Commentator: Hit straight to the feilder!")
            elif(r1==4):
              print("Commentator: Dot Ball!")
            print("")
        elif(playerinput==1):
            r2=r.randrange(1,5)
            print("")
            if(r2==1):
              print("Commentator: Single Taken!")
            elif(r2==2):
              print("Commentator: Knocked down the ground for a single!")
            elif(r2==3):
              print("Commentator: That's intelligent cricket! Just Drop and Run")
            elif(r2==4):
              print("Commentator: Quick single!")
            print("")
        elif(playerinput==2):
            r3=r.randrange(1,5)
            print("")
            print("Commentator: Nice running between the wickets! A double!")
            print("")
        elif(playerinput==3):
            print("")
            print("Commentator: Superb running between the wickets! Three taken")
            print("")
        elif(playerinput==4):
          print("")
          print("Commentator: Superb shot for a Boundary! ")
          print("")
        elif(playerinput==5):
          print("")
          print("Commentator: Five runs")
          print("")
        elif(playerinput==6):
          print("")
          print("Commentator: That's a Six!")
          print("")
        noofruns+=playerinput
        noofballs+=1
        if(indicator==0):
          noofrunsperover+=playerinput
    if(j!=6):
      print("Your score: ",noofruns,"/",wkt," ",i-1,".",j," overs",sep="")
      print("")
    else:
      print("Your score: ",noofruns,"/",wkt," ",i,".",0," overs",sep="")
      print("")
    
    if(k<11 and l<11):
      batsman1=players[k]
      batsman2=players[l]
    elif(k==11):
      score[l]=score2
      balls[l]=ball2
      print(batsman2," ",score2,"(",ball2,")*",sep="")
      print("")
      continue
    elif(l==11):
      print(batsman1," ",score1,"(",ball1,")*",sep="")
      print("")
      score[k]=score1
      balls[k]=ball1
      continue
    
    if(playerinput%2==1 and indicator==0):
      if(strike==0):
        score1+=playerinput
        strike=1
        ball1+=1
      else:
        score2+=playerinput
        strike=0
        ball2+=1
    elif(playerinput%2==0 and indicator==0):
      if(strike==0):
        score1+=playerinput
        ball1+=1
      else:
        score2+=playerinput
        ball2+=1
    
    print(batsman1," ",score1,"(",ball1,")*",sep="")
    print(batsman2," ",score2,"(",ball2,")*",sep="")
    print("")
  
  if(i==1):
    print("End of ",i,"st Over",sep="")
    print("")
  elif(i==2):
    print("End of ",i,"nd Over",sep="")
    print("")
  elif(i==3):
    print("End of ",i,"rd Over",sep="")
    print("")
  else:
    print("End of ",i,"th Over",sep="")
    print("")
    
  print(noofrunsperover,"run Over")
  print("")
  if(strike==0):
    strike=1
  else:
    strike=0
  print("")
  print("-"*150)
  print("")
  runsperover+=[noofrunsperover]
if(wkt<10):
  score[k]=score1
  balls[k]=ball1
  score[l]=score2
  balls[l]=ball2

if(wkt==10):
  print("-"*150)
  print("")
  print("End of 1st innings: ")
  print("")
  for i in range(11):
    print(players[i]," "*(10+maxlength(players)-len(players[i])),score[i],"(",balls[i],")",sep="")
  print("")
  print("Your score: ",noofruns," All out")
  print("")
  for i in runsperover:
    print(i)
  print("")
  print("-"*150)
  print("")
else:
  print("-"*150)
  print("")
  print("End of 1st innings: ")
  print("")
  for i in range(wkt+2):
    print(players[i]," "*(10+maxlength(players)-len(players[i])),score[i],"(",balls[i],")",sep="")
  print("")
  print("Your score: ",noofruns,"/",wkt)
  print("")
  for i in runsperover:
    print(i)
  print("")
  print("-"*150)
  print("")
    
    

    