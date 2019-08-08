from app import User

lst = []

Bob = User("bob@gmail.com", "password", "Bob Smith")
John = User("John@gmail.com", "password", "John Rogers")
Fred = User("fred@gmail.com", "password", "Fred O'Reily")
Sara = User("sara@gmail.com", "password", "Sara George")
Madeline = User("madeline@gmail.com", "password", "Madeline Cohen")
Connor = User("connor@gmail.com", "password", "Connor George")
Ryan = User("Ryan@gmail.com", "password", "Ryan Cohen")
Jeff = User("jeff@gmail.com", "password", "Jeff Smith")
Abby = User("abby@gmail.com", "password", "Abby Pennsly")
Kyra = User("kyra@gmail.com", "password", "Kyra Mccable")

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



for name in lst:
	db.session.add(name)
	print("Added!")
db.session.commit()

