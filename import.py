from app import db, User, Business, Organization, Fundraiser
import datetime as date

lst = []
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

lst2 = []
chipotle = Business(title="Chipotle", address="1735 N Lynn St Lbby 15, Rosslyn, VA 22209")
mcdonalds = Business(title="McDonalds", address = "750 17th St NW, Washington, DC 20006")
cheesecakeFactory = Business(title="Cheesecake Factory", address = " 2900 Clarendon Blvd, Arlington, VA 22201")
cava = Business(title = "Cava", address = "2940 Clarendon Blvd, Arlington, VA 22201")
greenPigBistro = Business(title="Green Pig Bistro", address = "2940 Clarendon Blvd, Arlington, VA 22201")
ambarClaredon = Business(title=" Ambar Clarendon", address = "2901 Wilson Blvd, Arlington, VA 22201")
libertyTavern = Business(title="Liberty Tavern", address = "3195 Wilson Blvd, Arlington, VA 22201")
lyonHall = Business(title = "Lyon Hall", address = "3100 Washington Blvd, Arlington, VA 22201")
pamplona = Business(title = "Pamplona", address = "3100 Clarendon Blvd, Arlington, VA 22201")
circaAtClarendon = Business(title = "CIRCA At Clarendon", address = "3010 Clarendon Blvd, Arlington, VA 22201")
lst.append(chipotle)
lst.append(mcdonalds)
lst.append(cheesecakeFactory)
lst.append(cava)
lst.append(greenPigBistro)
lst.append(ambarClaredon)
lst.append(libertyTavern)
lst.append(lyonHall)
lst.append(pamplona)
lst.append(circaAtClarendon)

for name in lst2:
	db.session.add(name)
	print("Added!")
db.session.commit()
print("Finished")

lst3 = []
bsaTroop281 = Organization(title = "Boy Scouts of America Troop 281")
redCross = Organization(title = "Red Cross")
dallasHighSchoolCrossCountry = Organization(title = "Dallas High School Cross Country")
lakeLehmanBoysLacrosse = Organization(title = "Lake Lehman Boys Lacrosse Team")
bsaTroop331 = Organization(title = "Boy Scouts of America Troop 331")
highSchoolGirlsVolleyBall = Organization(title = "High School Girls Volleyball")
codeForEveryone = Organization(title = "Code for Everyone")
michaelScottDunderMifflinScrantonMeredithPalmerMemorialCelebrityRabiesAwarenessProAMFunRunRaceForTheCure = Organization(id = "9", title = "Michael ScottDunder Mifflin Scranton Meredith Palmer Memorial Celebrity Rabies Awareness Pro AM Fun Run Race For The Cure")
lst.append(bsaTroop281)
lst.append(redCross)
lst.append(dallasHighSchoolCrossCountry)
lst.append(lakeLehmanBoysLacrosse)
lst.append(bsaTroop331)
lst.append(highSchoolGirlsVolleyBall)
lst.append(codeForEveryone)
lst.append(michaelScottDunderMifflinScrantonMeredithPalmerMemorialCelebrityRabiesAwarenessProAMFunRunRaceForTheCure)

for name in lst3:
	db.session.add(name)
	print("Added")
db.session.commit()
print("Finished!")

lst4 = []
chipotlefund1 = Fundraiser(business_id="1", organization_id="1", start_date=date.datetime(2019,8,8), end_date=date.datetime(2019,8,9))
mcdonaldsfund2 = Fundraiser(business_id="2", organization_id="2", start_date=date.datetime(2019,8,23), end_date=date.datetime(2019,8,24))
cheesecakeFactoryfund3 = Fundraiser(business_id="3", organization_id="3", start_date=date.datetime(2019,9,5), end_date=date.datetime(2019,9,7))
cavafund4 = Fundraiser(business_id="4", organization_id="4", start_date=date.datetime(2019,9,12), end_date=date.datetime(2019,9,13))
greenPigBistrofund5 = Fundraiser(business_id="5", organization_id="5", start_date=date.datetime(2019,10,1), end_date=date.datetime(2019,10,2))
ambarClaredonfund6 = Fundraiser(business_id="6", organization_id="6", start_date=date.datetime(2019,10,5), end_date=date.datetime(2019,10,6))
libertyTavernfund7 = Fundraiser(business_id="7", organization_id="7", start_date=date.datetime(2019,10,10), end_date=date.datetime(2019,10,10))
lyonHallfund8 = Fundraiser(business_id="8", organization_id="8", start_date=date.datetime(2019,11,12), end_date=date.datetime(2019, 11, 13))

for name in lst4:
	db.session.add(name)
	print("Added")
db.session.commit()
print("Finished")









