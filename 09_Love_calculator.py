import sys
class Lover:
    def __init__(self, name, surname, date_of_birth):
        letters="abcdefghijklmnopqrstuwvxyz"
        self.name=name
        for i in range(0,len(name)):
            if self.name[i] not in letters: sys.exit("wrong character in name")
        self.surname=surname
        for i in range(0,len(surname)):
            if self.surname[i] not in letters: sys.exit("wrong character in surname")
        self.date_of_birth=date_of_birth
        if len(self.date_of_birth)!=10: sys.exit("wrong date lenght")
        elif self.date_of_birth[2]!="/" or self.date_of_birth[5]!="/": sys.exit("wrong date format")
        for i in range(0,len(self.date_of_birth)):
            if self.date_of_birth[i] in letters: sys.exit("wrong character in date")
    def print_data(self):
        print("Name: ",self.name,"\nSurname: ",self.surname,"\nDate of birth: ",self.date_of_birth)

    def compare(self, lover):
        counter=0
        letters_of_name=""
        for i in range(0, len(self.name)):
            if self.name[i] not in letters_of_name:
                letters_of_name+=self.name[i]
        for i in letters_of_name:
            if i in lover.name:
                counter+=1
        letters_of_surname=""
        for i in range(0, len(self.surname)):
            if self.surname[i] not in letters_of_surname:
                letters_of_surname+=self.surname[i]
        for i in letters_of_surname:
            if i in lover.surname:
                counter+=1
        if self.date_of_birth[0]==lover.date_of_birth[0] and self.date_of_birth[1]==lover.date_of_birth[1]:
            counter+=1
        if self.date_of_birth[3]==lover.date_of_birth[3] and self.date_of_birth[4]==lover.date_of_birth[4]:
            counter+=1
        if self.date_of_birth[6]==lover.date_of_birth[6] and self.date_of_birth[7]==lover.date_of_birth[7] and self.date_of_birth[8]==lover.date_of_birth[8] and self.date_of_birth[9]==lover.date_of_birth[9]:
            counter+=1
        return counter*100/(len(letters_of_name)+len(letters_of_surname)+8)
        
'''
L1=Lover(
    input("Write your name (only small letters): "),
    input("Write your surname (only small letters): "),
    input("Write your date of birth (DD/MM/YYYY): "))
'''
L1=Lover("john","shepard","02/12/1997")
L1.print_data()
'''
L2=Lover(
    input("Write your lover's name (only small letters): "),
    input("Write your lover's surname (only small letters): "),
    input("Write your lover's date of birth (DD/MM/YYYY): "))
'''
L2=Lover("jane","shepard","10/12/2000")
L2.print_data()

print("Yours match is: ", round(L1.compare(L2),2),"%")




    
    
