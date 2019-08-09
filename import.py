from app import db, User, Business, Organization, Fundraiser, Follows
import datetime as date

# Creates rows for User Table
'''
Bob = User(email="bob@gmail.com", password="password", name="Bob Smith")
John = User(email="John@gmail.com", password="password", name="John Rogers")
Fred = User(email="fred@gmail.com", password="password", name="Fred O'Reily")
Sara = User(email="sara@gmail.com", password="password", name="Sara George")
Madeline = User(email="madeline@gmail.com", password="password", name="Madeline Cohen")
Connor = User(email="connor@gmail.com", password="password", name="Connor George")
Ryan = User(email="Ryan@gmail.com", password="password", name="Ryan Cohen")
Jeff = User(email="jeff@gmail.com", password="password", name="Jeff Smith")
Abby = User(email="abby@gmail.com", password="password", name="Abby Pennsly")
Kyra = User(email="kyra@gmail.com", password="password", name="Kyra Mccable")

lst = []
lst.append(Bob)
lst.append(John)
lst.append(Fred)
lst.append(Sara)
lst.append(Madeline)
lst.append(Connor)
lst.append(Ryan)
lst.append(Jeff)
lst.append(Abby)
lst.append(Kyra)

for name in lst:C
	db.session.add(name)
	print("Added!")
db.session.commit()
print("Finished")
'''

# Creates rows for Business Table
'''
chipotle = Business(title="Chipotle", address="1735 N Lynn St Lbby 15, Rosslyn, VA 22209")
mcdonalds = Business(title="McDonalds", address = "750 17th St NW, Washington, DC 20006")
cheesecakeFactory = Business(title="Cheesecake Factory", address = " 2900 Clarendon Blvd, Arlington, VA 22201")
cava = Business(title = "Cava", address = "2940 Clarendon Blvd, Arlington, VA 22201")
#greenPigBistro = Business(title="Green Pig Bistro", address = "2940 Clarendon Blvd, Arlington, VA 22201")
ambarClaredon = Business(title=" Ambar Clarendon", address = "2901 Wilson Blvd, Arlington, VA 22201")
libertyTavern = Business(title="Liberty Tavern", address = "3195 Wilson Blvd, Arlington, VA 22201")
lyonHall = Business(title = "Lyon Hall", address = "3100 Washington Blvd, Arlington, VA 22201")
pamplona = Business(title = "Pamplona", address = "3100 Clarendon Blvd, Arlington, VA 22201")
circaAtClarendon = Business(title = "CIRCA At Clarendon", address = "3010 Clarendon Blvd, Arlington, VA 22201")

lst2 = []
lst2.append(chipotle)
lst2.append(mcdonalds)
lst2.append(cheesecakeFactory)
lst2.append(cava)
#lst2.append(greenPigBistro)
lst2.append(ambarClaredon)
lst2.append(libertyTavern)
lst2.append(lyonHall)
lst2.append(pamplona)
lst2.append(circaAtClarendon)

for name in lst2:
	db.session.add(name)
	print("Added!")
db.session.commit()
print("Finished")
'''

# Creates rows for Organization Table
'''
bsaTroop281 = Organization(title = "Boy Scouts of America Troop 281")
redCross = Organization(title = "Red Cross")
dallasHighSchoolCrossCountry = Organization(title = "Dallas High School Cross Country")
lakeLehmanBoysLacrosse = Organization(title = "Lake Lehman Boys Lacrosse Team")
bsaTroop331 = Organization(title = "Boy Scouts of America Troop 331")
highSchoolGirlsVolleyBall = Organization(title = "High School Girls Volleyball")
codeForEveryone = Organization(title = "Code for Everyone")
michaelScottDunderMifflinScrantonMeredithPalmerMemorialCelebrityRabiesAwarenessProAMFunRunRaceForTheCure = Organization(id = "9", title = "Michael ScottDunder Mifflin Scranton Meredith Palmer Memorial Celebrity Rabies Awareness Pro AM Fun Run Race For The Cure")

lst3 = []
lst3.append(bsaTroop281)
lst3.append(redCross)
lst3.append(dallasHighSchoolCrossCountry)
lst3.append(lakeLehmanBoysLacrosse)
lst3.append(bsaTroop331)
lst3.append(highSchoolGirlsVolleyBall)
lst3.append(codeForEveryone)
lst3.append(michaelScottDunderMifflinScrantonMeredithPalmerMemorialCelebrityRabiesAwarenessProAMFunRunRaceForTheCure)

for name in lst3:
	db.session.add(name)
	print("Added")
db.session.commit()
print("Finished!")
'''

# Creates rows for Fundraiser Table
'''
lst4 = []
chipotlefund1 = Fundraiser(business_id="16",organization_id="1", start_date=date.datetime(2019,8,8), end_date=date.datetime(2019,8,9), description="50 percent towards organzation")
mcdonaldsfund2 = Fundraiser(business_id="17", organization_id="2", start_date=date.datetime(2019,8,23), end_date=date.datetime(2019,8,24), description="50 percent towards organzation")
cheesecakeFactoryfund3 = Fundraiser(business_id="18", organization_id="3", start_date=date.datetime(2019,9,5), end_date=date.datetime(2019,9,7), description="50 percent towards organzation")
cavafund4 = Fundraiser(business_id="19", organization_id="4", start_date=date.datetime(2019,9,12), end_date=date.datetime(2019,9,13), description="50 percent towards organzation")
#greenPigBistrofund5 = Fundraiser(business_id="5", organization_id="5", start_date=date.datetime(2019,10,1), end_date=date.datetime(2019,10,2), description="50 percent towards organzation")
ambarClaredonfund6 = Fundraiser(business_id="20", organization_id="6", start_date=date.datetime(2019,10,5), end_date=date.datetime(2019,10,6), description="50 percent towards organzation")
libertyTavernfund7 = Fundraiser(business_id="21", organization_id="7", start_date=date.datetime(2019,10,10), end_date=date.datetime(2019,10,10), description="50 percent towards organzation")

chipotlefund2 = Fundraiser(business_id="16",organization_id="7", start_date=date.datetime(2019,8,8), end_date=date.datetime(2019,8,9), description="25 percent towards organzation")
db.session.add(chipotlefund2)
db.session.commit()

lst4.append(chipotlefund1)
lst4.append(mcdonaldsfund2)
lst4.append(cheesecakeFactoryfund3)
lst4.append(cavafund4)
lst4.append(ambarClaredonfund6)
lst4.append(libertyTavernfund7)

for name in lst4:
	db.session.add(name)
	print("Added")
db.session.commit()
print("Finished")
'''

# Creates rows for Follow Table
'''
bobfollows1 = Follows(user_id = 1, organization_id=1)
bobfollows2 = Follows(user_id = 1, organization_id=2)
bobfollows3 = Follows(user_id = 1, organization_id=3)
bobfollows4 = Follows(user_id = 1, organization_id=4)
bobfollows5 = Follows(user_id = 1, organization_id=5)
bobfollows6 = Follows(user_id = 1, organization_id=6)
bobfollows7 = Follows(user_id = 1, organization_id=7)
bobfollows9 = Follows(user_id = 1, organization_id=9)

lst5 = []
lst5.append(bobfollows1)
lst5.append(bobfollows2)
lst5.append(bobfollows3)
lst5.append(bobfollows4)
lst5.append(bobfollows5)
lst5.append(bobfollows6)
lst5.append(bobfollows7)
lst5.append(bobfollows9)

for name in lst5:
	db.session.add(name)
	print("Added")
db.session.commit()
print("Finished")
'''