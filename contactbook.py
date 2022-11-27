# %%
#basics
class ContactBook:
    def __init__(self, firstName, lastName, emailAddress, mobileNo):
        self.firstName = firstName
        self.lastName = lastName
        self.emailAddress = emailAddress
        self.mobileNo = mobileNo

    def displayFullContactInformation(self):
        print("First name: ", self.firstName)
        print("Last name: ", self.lastName)
        print("Email address: ", self.emailAddress)
        print("Mobile number:", self.mobileNo)

contact_1 = ContactBook("Keith", "Richards", "nothing_will_kill_me@gmail.com", 5555551234)
contact_2 = ContactBook("Mick", "Jagger", "i_have_tried_every_drug_on_the_planet@hotmail.com", 5555551235)

contact_1.displayFullContactInformation()

# %%
#simple contact book
class Contacts:
    def __init__(self, firstName, lastName, emailAddress, mobileNo):
        self.firstName = firstName
        self.lastName = lastName
        self.emailAddress = emailAddress
        self.mobileNo = mobileNo

class ContactBook:
    def __init__(self):
        self.contact_book = []
    
    def add_contact(self, firstName, lastName, emailAddress, mobileNo):
        added_contact = Contacts(firstName, lastName, emailAddress, mobileNo)
        self.contact_book.append(added_contact)

    def delete_contact(self, firstName):
        for p in self.contact_book:
            if p.firstName == firstName:
                self.contact_book.remove(p)

    def search_contact_by_name(self, firstName):
        for name in self.contact_book:
            if name.firstName == firstName:
                return vars(name)
    
    def search_contact_by_phonenumber(self, mobileNo):
        for number in self.contact_book:
            if number.mobileNo == mobileNo:
                return vars(number)
    
    def displayAllContacts(self):
        for contacts in self.contact_book:
            print (vars(contacts))

friendsAndFamily = ContactBook()

friendsAndFamily.add_contact("Keith", "Richards", "nothing_will_kill_me@gmail.com", 5555551234)
friendsAndFamily.add_contact("Mick", "Jagger", "i_have_tried_every_drug_on_the_planet@hotmail.com", 5555551235)
friendsAndFamily.add_contact("Charlie", "Watts", "charlie_mccharles@charlie.com", 5555551236)
friendsAndFamily.add_contact("Ronnie", 'Wood', "i_love_my_guitar@yahoo.com", 5555551236)

friendsAndFamily.delete_contact('Charlie')

#print(friendsAndFamily.search_contact_by_phonenumber(5555551236))

#print(friendsAndFamily.search_contact_by_name('Mick'))

friendsAndFamily.displayAllContacts()
# %%
