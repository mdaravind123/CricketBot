  
import random as r
import time as t

print("")
print("Welcome to Cricket Game!")
print("")

print("Choose one Format among these 3: ODI,T20 and Test")
print("")
chooseFormat=input("Choose format: ")                            #Choose Format
print("")

print("Toss time: ")
print("")
toss=r.randrange(1,3)
if(toss==1):
  result="head"
else:
  result="tail"
print("Type head or tail:  ")
print("")
tossinput=input("Enter your call!: ")
if(tossinput.lower()==result):
  print("Congratulations! You have won the toss!")
  print("")
  print("What you would like to do?")
  print("Batting or Bowling!")
  print("")
  userchoice=input("Enter your choice:  ")
  print("")
  if(userchoice.lower()=="batting"):
    player=1
    comp=0
  elif(userchoice.lower()=="bowling"):
    comp=1
    player=0
else:
  print("Computer won the toss! ")
  print("")
  compchoice=r.randrange(1,3)
  if(compchoice==1):
    comp=1
    player=0
  else:
    comp=0
    player=1
  if(comp==1):
    print("computer choose to bat first! ")
    print("")
  else:
    print("Computer choose to bowl first! ")
    print("")
  
  

noOfBalls=0
noOfRuns=0
Wkt=0

print("Great! Now the Game is about to Start! ")
print("")
if(chooseFormat.lower()=="t20"):
  print("Countdown starts! ")
  print("")
  t.sleep(2)
  print(5)
  t.sleep(2)
  print(4)
  t.sleep(2)
  print(3)
  t.sleep(2)
  print(2)
  t.sleep(2)
  print(1)
  t.sleep(2)
  print("")
  print("Let's start the Game!  ")
  print("")
  players=["Rohit Sharma","Shubman Gill","Virat Kohli","Shreyas Iyer","KL Rahul","Hardik Pandya","Ravindra Jadeja","Mohammed Shami",
           "Kuldeep Yadav","Jasprit Bumrah","Mohammed Siraj"]
  i=0
  j=1
  score=[0,0,0,0,0,0,0,0,0,0,0]
  balls=[0,0,0,0,0,0,0,0,0,0,0]
  strike=0
  score1=0
  score2=0
  ball1=0
  ball2=0
  batsman1=players[i]
  batsman2=players[j]
  
  noofballs=0
  noofruns=0
  maxballs=120
  wkt=0
  noofrunsperover=0
  if(comp==0):
    while(wkt<=10 or noofballs>=maxballs):
      indicator=0
      if(wkt==10):
        break
      if(noofballs>=maxballs):
        break
      playerinput=int(input("Enter 0 to 6: "))
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
            print(batsman1," ",score1,"(",ball1+1,") Out Gone!",sep="")
            print("")
            score[i]=score1
            balls[i]=ball1+1
            i=max(i,j)+1
            score1=0
            ball1=0
          else:
            print(batsman2," ",score2,"(",ball2+1,") Out Gone!",sep="")
            print("")
            score[j]=score2
            balls[j]=ball2+1
            j=max(i,j)+1
            score2=0
            ball2=0
            
        else:
          if(playerinput==0):
            r1=r.randrange(1,5)
            if(r1==1):
              print("Rock Solid Defence from the batsman!")
            elif(r1==2):
              print("That's a gem of a delivery! Beats the Batsman")
            elif(r1==3):
              print("Hit straight to the feilder!")
            elif(r1==4):
              print("Dot Ball!")
            print("")
          elif(playerinput==1):
            r2=r.randrange(1,5)
            if(r2==1):
              print("Single Taken!")
            elif(r2==2):
              print("Knocked down the ground for a single!")
            elif(r2==3):
              print("That's intelligent cricket! Just Drop and Run")
            elif(r2==4):
              print("Quick single!")
            print("")
          elif(playerinput==2):
            r3=r.randrange(1,5)
            print("Nice running between the wickets! A double!")
            print("")
          elif(playerinput==3):
            print("Superb running between the wickets! Three taken")
            print("")
          elif(playerinput==4):
            print("Superb shot for a Boundary! ")
            print("")
          elif(playerinput==5):
            print("Five runs")
            print("")
          elif(playerinput==6):
            print("That's a Six!")
            print("")
          noofruns+=playerinput
          noofballs+=1
        print("Your score: ",noofruns,"/",wkt," ",noofballs//6,".",noofballs%6," overs",sep="")
        print("")
        
        if(i<11 and j<11):
          batsman1=players[i]
          batsman2=players[j]
        elif(i==11):
          score[j]=score2
          balls[j]=ball2
          print(batsman2," ",score2,"(",ball2,")*",sep="")
          continue
        elif(j==11):
          print(batsman1," ",score1,"(",ball1,")*",sep="")
          score[i]=score1
          balls[i]=ball1
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
        
        if(noofballs%6==0):
          if(noofballs//6==1):
            print("End of ",noofballs//6,"st Over",sep="")
            print("")
          elif(noofballs//6==2):
            print("End of ",noofballs//6,"nd Over",sep="")
            print("")
          elif(noofballs//6==3):
            print("End of ",noofballs//6,"rd Over",sep="")
            print("")
          else:
            print("End of ",noofballs//6,"th Over",sep="")
            print("")
        
        if(noofballs%6==0):
          print(noofrunsperover+playerinput,"run over")
          if(strike==0):
            strike=1
          else:
            strike=0
          print("")
          print("-----------------------------------------------------------------------------------------------------------------------------")
          print("")
          noofrunsperover=0
        else:
          noofrunsperover+=playerinput
    if(wkt<10):
      score[i]=score1
      balls[i]=ball1
      score[j]=score2
      balls[j]=ball2
      
      
       
    if(wkt==10):
      print("-----------------------------------------------------------------------------------------------------------------------------")
      print("")
      print("End of 1st innings: ")
      print("")
      for i in range(11):
        print(players[i]," ",score[i],"(",balls[i],")",sep="")
      print("")
      print("Your score: ",noofruns," All out")
      print("")
      print("-----------------------------------------------------------------------------------------------------------------------------")
      print("")
    else:
      print("-----------------------------------------------------------------------------------------------------------------------------")
      print("")
      print("End of 1st innings: ")
      print("")
      for i in range(wkt+2):
        print(players[i]," ",score[i],"(",balls[i],")",sep="")
      print("")
      print("Your score: ",noofruns,"/",wkt)
      print("")
      print("-----------------------------------------------------------------------------------------------------------------------------")
      print("")
    target=noofruns
    
    noofballs1=0
    noofruns1=0
    maxballs1=120
    wkt1=0
    noofrunsperover=0
    print("Target: ",target+1)
    print("")
    print("Let's start the Chase! ")
    print("")
    
    players=["David Warner","Travis Head","Mitchell Marsh","Steven Smith","Marnus Labuchagne","Glenn Maxwell","Josh Inglis","Mitchell Starc",
           "Pat cummins","Adam Zampa","Josh Hazlewood"]
    i=0
    j=1
    score=[0,0,0,0,0,0,0,0,0,0,0]
    balls=[0,0,0,0,0,0,0,0,0,0,0]
    strike=0
    score1=0
    score2=0
    ball1=0
    ball2=0
    
    while(wkt1<=10 or noofballs1>=maxballs1 or noofruns1>target):
      indicator=0
      
      if(wkt1==10):
        break
      if(noofballs1>=maxballs1):
        break
      if(noofruns1>target):
        break
      playerbowl1=int(input("Enter 1 to 6: "))
      if(playerbowl1>6 and playerbowl1<0):
        print("Invalid Entry")
        print("")
      else:
        compbat1=r.randrange(0,7)
        if(compbat1==playerbowl1):
          
          wkt1+=1
          noofballs1+=1
          compbat1=0
          indicator=1
          if(strike==0):
            print(batsman1," ",score1,"(",ball1+1,") Out Gone!",sep="")
            print("")
            score[i]=score1
            balls[i]=ball1+1
            i=max(i,j)+1
            score1=0
            ball1=0
          else:
            print(batsman2," ",score2,"(",ball2+1,") Out Gone!",sep="")
            print("")
            score[j]=score2
            balls[j]=ball2+1
            j=max(i,j)+1
            score2=0
            ball2=0
            
        else:
          if(compbat1==0):
            print("Dot Ball!")
            print("")
          elif(compbat1==1):
            print("Single Taken!")
            print("")
          elif(compbat1==2):
            print("Nice running between the wickets! A double!")
            print("")
          elif(compbat1==3):
            print("Superb running between the wickets! Three taken")
            print("")
          elif(compbat1==4):
            print("Superb shot for a Boundary! ")
            print("")
          elif(compbat1==5):
            print("Five runs")
            print("")
          elif(compbat1==6):
            print("That's a Six!")
            print("")
          noofruns1+=compbat1
          noofballs1+=1
        print("Computer score: ",noofruns1,"/",wkt1," ",noofballs1//6,".",noofballs1%6," overs",sep="")
        print("")
        
        if(i<11 and j<11):
          batsman1=players[i]
          batsman2=players[j]
        elif(i==11):
          score[j]=score2
          balls[j]=ball2
          continue
        elif(j==11):
          score[i]=score1
          balls[i]=ball1
          continue
        
        if(compbat1%2==1 and indicator==0):
          if(strike==0):
            score1+=compbat1
            strike=1
            ball1+=1
          else:
            score2+=compbat1
            strike=0
            ball2+=1
        elif(compbat1%2==0 and indicator==0):
          if(strike==0):
            score1+=compbat1
            ball1+=1
          else:
            score2+=compbat1
            ball2+=1
            
        print(batsman1," ",score1,"(",ball1,")*",sep="")
        print(batsman2," ",score2,"(",ball2,")*",sep="")
        print("")
        
        if(noofballs1%6==0):
          if(noofballs1//6==1):
            print("End of ",noofballs1//6,"st Over",sep="")
            print("")
          elif(noofballs1//6==2):
            print("End of ",noofballs1//6,"nd Over",sep="")
            print("")
          elif(noofballs1//6==3):
            print("End of ",noofballs1//6,"rd Over",sep="")
            print("")
          else:
            print("End of ",noofballs1//6,"th Over",sep="")
            print("")
        if(noofballs1%6==0):
          print(noofrunsperover+compbat1,"run over")
          if(strike==0):
            strike=1
          else:
            strike=0
          print("")
          print("-----------------------------------------------------------------------------------------------------------------------------")
          print("")
          noofrunsperover=0
        else:
          noofrunsperover+=compbat1
    
    if(wkt<10):
      score[i]=score1
      balls[i]=ball1
      score[j]=score2
      balls[j]=ball2
    
    if(noofruns1>target):
      print("-----------------------------------------------------------------------------------------------------------------------------")
      print("")
      for i in range(wkt1+2):
        print(players[i]," ",score[i],"(",balls[i],")",sep="")
      print("")
      print("Computer won the game by",10-wkt1," wickets")
      print("")
      print("-----------------------------------------------------------------------------------------------------------------------------")
      print("")
    elif(noofruns1<target):
      print("-----------------------------------------------------------------------------------------------------------------------------")
      print("")
      for i in range(11):
        print(players[i]," ",score[i],"(",balls[i],")",sep="")
      print("")
      print("Congratulations! You have won the game by",target-noofruns1," runs")
      print("")
      print("-----------------------------------------------------------------------------------------------------------------------------")
      print("")
    else:
      print("-----------------------------------------------------------------------------------------------------------------------------")
      print("")
      for i in range(11):
        print(players[i]," ",score[i],"(",balls[i],")",sep="")
      print("")
      print("It's a Draw!")
      print("")
      print("-----------------------------------------------------------------------------------------------------------------------------")
      print("")
  elif(comp==1):
    noofballs1=0
    noofruns1=0
    maxballs1=120
    wkt1=0
    noofrunsperover1=0
    while(wkt1<=10 or noofballs1>=maxballs1):
      if(wkt1==10):
        break
      if(noofballs1>=maxballs1):
        break
      playerbowl1=int(input("Enter 1 to 6: "))
      if(playerbowl1>6 and playerbowl1<0):
        print("Invalid Entry")
        print("")
      else:
        compbat1=r.randrange(0,7)
        if(compbat1==playerbowl1):
          print("Out Gone!")
          print("")
          wkt1+=1
          noofballs1+=1
          compbat1=0
        else:
          if(compbat1==0):
            print("Dot Ball!")
            print("")
          elif(compbat1==1):
            print("Single Taken!")
            print("")
          elif(compbat1==2):
            print("Nice running between the wickets! A double!")
            print("")
          elif(compbat1==3):
            print("Superb running between the wickets! Three taken")
            print("")
          elif(compbat1==4):
            print("Superb shot for a Boundary! ")
            print("")
          elif(compbat1==5):
            print("Five runs")
            print("")
          elif(compbat1==6):
            print("That's a Six!")
            print("")
          noofruns1+=compbat1
          noofballs1+=1
        print("Computer score:",noofruns1,"/",wkt1," ",noofballs1//6,".",noofballs1%6," overs",sep="")
        print("")
         
        if(noofballs1%6==0):
          if(noofballs1//6==1):
            print("End of ",noofballs1//6,"st Over",sep="")
            print("")
          elif(noofballs1//6==2):
            print("End of ",noofballs1//6,"nd Over",sep="")
            print("")
          elif(noofballs1//6==3):
            print("End of ",noofballs1//6,"rd Over",sep="")
            print("")
          else:
            print("End of ",noofballs1//6,"th Over",sep="")
            print("")
        if(noofballs1%6==0):
          print(noofrunsperover1+compbat1,"run over")
          print("")
          print("-----------------------------------------------------------------------------------------------------------------------------")
          print("")
          noofrunsperover1=0
        else:
          noofrunsperover1+=compbat1
        
    if(wkt1==10):
      print("-----------------------------------------------------------------------------------------------------------------------------")
      print("")
      print("End of 1st innings: ")
      print("Computer score: ",noofruns1," All out")
      print("")
      print("-----------------------------------------------------------------------------------------------------------------------------")
      print("")
    else:
      print("-----------------------------------------------------------------------------------------------------------------------------")
      print("")
      print("End of 1st innings: ")
      print("Computer score: ",noofruns1,"/",wkt1)
      print("")  
      print("-----------------------------------------------------------------------------------------------------------------------------")
      print("")
    
    target=noofruns1
    print("Let's start the Chase! ")
    print("")
    noofballs=0
    noofruns=0
    maxballs=120
    wkt=0
    noofrunsperover=0
    while(wkt<=10 or noofballs>=maxballs or noofruns>target):
      if(wkt==10):
        break
      if(noofballs==maxballs):
        break
      if(noofruns>target):
        break
      playerinput=int(input("Enter 0 to 6: "))
      if(playerinput>6):
        print("Invalid Entry")
        print("")
      else:
        compbowl=r.randrange(1,7)
        if(compbowl==playerinput):
          print("Out Gone!")
          print("")
          wkt+=1
          noofballs+=1
          playerinput=0
        else:
          if(playerinput==0):
            print("Dot Ball!")
            print("")
          elif(playerinput==1):
            print("Single Taken!")
            print("")
          elif(playerinput==2):
            print("Nice running between the wickets! A double!")
            print("")
          elif(playerinput==3):
            print("Superb running between the wickets! Three taken")
            print("")
          elif(playerinput==4):
            print("Superb shot for a Boundary! ")
            print("")
          elif(playerinput==5):
            print("Five runs")
            print("")
          elif(playerinput==6):
            print("That's a Six!")
            print("")
          noofruns+=playerinput
          noofballs+=1
        print("Your score:",noofruns,"/",wkt," ",noofballs//6,".",noofballs%6," overs",sep="")
        print("")
        if(noofballs%6==0):
          if(noofballs//6==1):
            print("End of ",noofballs//6,"st Over",sep="")
            print("")
          elif(noofballs//6==2):
            print("End of ",noofballs//6,"nd Over",sep="")
            print("")
          elif(noofballs//6==3):
            print("End of ",noofballs//6,"rd Over",sep="")
            print("")
          else:
            print("End of ",noofballs//6,"th Over",sep="")
            print("")
        if(noofballs%6==0):
          print(noofrunsperover+playerinput,"run over")
          print("")
          print("-----------------------------------------------------------------------------------------------------------------------------")
          print("")
          noofrunsperover=0
        else:
          noofrunsperover+=playerinput
    if(noofruns>target):
      print("----------------------------------------------------------------------------------------------------------------------------------")
      print("")
      print("Congratulations! Player won the game by",10-wkt," wickets")
      print("")
      print("-----------------------------------------------------------------------------------------------------------------------------")
      print("")
    elif(noofruns<target):
      print("-----------------------------------------------------------------------------------------------------------------------------")
      print("")
      print("Computer has won the game by",target-noofruns," runs")
      print("")
      print("-----------------------------------------------------------------------------------------------------------------------------")
      print("")
    else:
      print("-----------------------------------------------------------------------------------------------------------------------------")
      print("")
      print("It's a Draw!")
      print("")     
      print("-----------------------------------------------------------------------------------------------------------------------------")
      print("")   
    
      
    
      
      
    
      
      
  
  
  
  



