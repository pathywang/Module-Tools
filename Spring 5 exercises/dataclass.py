from dataclasses import dataclass
from datetime import date

@dataclass
class Person:
    name : str
    date_of_birth: date
    preferred_operating_system: str

    def is_adult(self) -> bool :
        today = date.today()
        age = today.year - self.date_of_birth.year

        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age-=1

        return age>=18   

imaran= Person("Imaran", date(2011,11,23), "Ubuntun")  
imara2= Person("Imaran", date(2011,11,23), "Ubuntun") 

print(imaran)
print(imara2)
print(imaran==imara2)
print(imaran.is_adult())


           
