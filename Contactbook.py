''' Command line Python Project to store contact datails like Id, Name, Number in a remote device. Database I used
    for this project is Sqlite3, this is the software which can be used without installing just we need to download the source file. '''

# Importing neccessary libraries
import sqlite3
from sqlite3 import Error

# Intializing and Connecting to the database or Creating if not exists
try:                                              
    conn = sqlite3.connect('ContactBook.db')         
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Contact (      
    			ID text,
                Name text NOT NULL,
                Num integer NOT NULL)''')
except Error as e:
    print(e)

class Contact:

	def setup(self):
		while True:
			print("")
			print("                                    |***********************|")
			print("                                    |* 1 :: Add Contact    *|")
			print("                                    |* 2 :: Change Contact *|")
			print("                                    |* 3 :: Delete Contact *|")
			print("                                    |* 4 :: Veiw Contacts  *|")
			print("                                    |***********************|")
			op = int(input(" Enter your Option :: "))
			print("")
			a = self.switch(op)
			print("")
			print(" |----------------|")
			proc = str(input(" Want to continue Y/N :: "))
			proc = proc.lower()
			print(" |----------------|")
			if proc == "y":
				continue
			else :
				break

	# Method to call respective methods depending on our selection
	def switch(self, op):
		if op == 1:
			self.add()
			return
		elif op == 2:
			self.change()
			return
		elif op == 3:
			self.delete()
			return
		elif op == 4:
			self.veiw()
			return

	# Method to add Contact details into Database
	def add(self):
		mail = str(input(" Enter Contact Mail ID to add :: "))
		mail = mail.lower()
		name = str(input(" Enter Contact name to add :: "))
		name = name.lower()
		number = int(input(" Enter Contact number to add :: "))
		stnumber = str(number)
		length = len(stnumber)
		length2 = len(name)
		while(length2 == 0 & length != 10):       # Checking whether name and number are valid or not
			print(" ")
			print("******************Enter Correct Contact Information to add!!**************************")
			name = str(input(" Enter Contact name to add :: "))
			number = int(input(" Enter Contact number to add :: "))
			stnumber = str(number)
			length = len(stnumber)
		sqlcheck = '''SELECT Name, Num FROM Contact WHERE Name=? AND Num=?'''
		c.execute(sqlcheck, (name, number))
		data = c.fetchall()
		if len(data)!=0:
			print("Contact list already exists !!")
			return
		sql = '''INSERT INTO Contact(ID,Name,Num) VALUES(?,?,?)'''    # Sql query to add new data to table
		c.execute(sql, (mail, name, number))
		conn.commit()
		print(" Added")

	# Method to Updata data on database
	def change(self):
		update = str(input("Want to Update Id or Name or Number :: "))
		update = update.lower()
		if update == "id":
			mail = str(input(" Enter Contact Mail ID to Update :: "))
			mail = mail.lower()
			name = str(input(" Enter Contact name to Update Id :: "))
			name = name.lower()
			length = len(mail)
			length2 = len(name)
			while(length2 == 0 & length == 0):     # Checking whether details are valid or not
				print(" ")
				print("******************Enter Correct Contact Information to Change!!**************************")
				mail = str(input(" Enter Contact mail to Update :: "))
				name = int(input(" Enter Contact name to Update Id :: "))
				length = len(mail)
				length2 = len(name)
			sql = '''UPDATE Contact SET ID = ? WHERE Name = ? '''
			c.execute(sql, (mail, name))
			conn.commit()
			print(" Updated")
			return

		elif update == "name":
			name = str(input(" Enter Contact name to Update :: "))
			name = name.lower()
			number = int(input(" Enter Contact number to Update Name :: "))
			length = len(str(number))
			length2 = len(name)
			while(length2 == 0 & length != 10):     # Checking whether name and number are valid or not
				print(" ")
				print("******************Enter Correct Contact Information to Change!!**************************")
				name = str(input(" Enter Contact name to Update :: "))
				number = int(input(" Enter Contact number to Update Name :: "))
				stnumber = str(number)
				length = len(stnumber)
			sql = '''UPDATE Contact SET Name = ? WHERE Num = ? '''
			c.execute(sql, (name, number))
			conn.commit()
			print(" Updated")
			return

		elif update == "number":
			number = int(input(" Enter Contact number to Update :: "))
			name = str(input(" Enter Contact name to Update Number :: "))
			name = name.lower()
			length = len(str(number))
			length2 = len(name)
			while(length2 == 0 & length != 10):     # Checking whether name and number are valid or not
				print(" ")
				print("******************Enter Correct Contact Information to Change!!**************************")
				number = str(input(" Enter Contact number to Update :: "))
				name = int(input(" Enter Contact number to Update Number :: "))
				stnumber = str(number)
				length = len(stnumber)
			sql = '''UPDATE Contact SET Num = ? WHERE Name = ? '''
			c.execute(sql, (number, name))
			conn.commit()
			print(" Updated")
			return		

	# Method to delete Contact details from Database
	def delete(self):
		mail = str(input(" Enter Contact Mail ID to add :: "))
		mail = mail.lower()
		name = str(input(" Enter Contact name to delete :: "))
		name = name.lower()
		number = int(input(" Enter Contact number to delete :: "))
		stnumber = str(number)
		length = len(stnumber)
		length2 = len(name)
		while(length2 == 0 & length != 10):      # Checking whether name and number are valid or not
			print(" ")
			print("******************Enter Correct Contact Information to delete!!**************************")
			name = str(input(" Enter Contact name to delete :: "))
			number = int(input(" Enter Contact number to delete :: "))
			stnumber = str(number)
			length = len(stnumber)
		sqlcheck = '''SELECT Name, Num FROM Contact WHERE Name=? AND Num=?'''
		c.execute(sqlcheck, (name, number))
		data = c.fetchall()
		if len(data)==0:
			print("There is no such data present !!")
			return
		sql = '''DELETE FROM Contact WHERE Name=? AND Num=?'''  # Sql query to delete data
		c.execute(sql, (name, number))
		conn.commit()
		print(" Deleted")

	# Method the Contacts present in the Database
	def veiw(self):
		print("	|----- Printing the Entire data present in the database -----|")
		sql = '''SELECT * FROM Contact'''     # Sql query to select entire data from given table
		c.execute(sql)
		rows = c.fetchall()
		for row in rows:
			print(row)


if __name__ == '__main__':
	print("|----------------------------- Project Title :: Contact List ------------------------------|")
	cont = Contact()      # Intializing the Contact class
	cont.setup()
