import random as r

def batting(chooseFormat):
  if(chooseFormat.lower()=="t20"):
    noofballs=0
    noofruns=0
    maxballs=120
    wkt=0
    while(wkt!=10 or noofballs!=maxballs):
      playerinput=int(input("Enter 0 to 6: "))
      if(playerinput>6):
        print("Invalid Entry")
      else:
        compbowl=r.randrange(1,7)
        if(compbowl==playerinput):
          print("Out Gone!")
          wkt+=1
          noofballs+=1
        else:
          if(playerinput==0):
            print("Dot Ball!")
          elif(playerinput==1):
            print("Single Taken!")
          elif(playerinput==2):
            print("Nice running between the wickets! A double!")
          elif(playerinput==3):
            print("Superb running between the wickets! Three taken")
          elif(playerinput==4):
            print("Superb shot for a Boundary! ")
          elif(playerinput==5):
            print("Five runs")
          elif(playerinput==6):
            print("That's a Six!")
          noofruns+=playerinput
          noofballs+=1
        print("Your score:",noofruns,"/",wkt,noofballs/6,".",noofballs%6," overs",sep="")
    return(noofruns)
      
        
        
  elif(chooseFormat.lower()=="odi"):
    noofballs=0
    noofruns=0
    maxballs=300
    wkt=0
  elif(chooseFormat.lower()=="test"):
    noofballs=0
    noofruns=0
    wkt=0
    