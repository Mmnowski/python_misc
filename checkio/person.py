class Person:
    def __init__(self, first_name, last_name, birth_date, job, working_years, salary, country, city, gender='unknown'):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.job = job
        self.working_years = working_years
        self.salary = salary
        self.country = country
        self.city = city
        self.gender = gender

    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def age(self):
        age = self.birth_date.split('.')
        current_time = "01.01.2018".split('.')
        if age[1] < current_time[1]:
            return int(current_time[2]) - int(age[2]) - 2
        else:
            if age[0] < current_time[0]:
                return int(current_time[2]) - int(age[2]) - 2
            else:
                return int(current_time[2]) - int(age[2]) - 1

    def work(self):
        if self.gender == 'female':
            return "She is a {}".format(self.job)
        elif self.gender == 'male':
            return "He is a {}".format(self.job)
        else:
            return "Is a {}".format(self.job)

    def money(self):
        return format(self.salary*self.working_years*12, ',').replace(',', ' ')

    def home(self):
        return "Lives in {}, {}".format(self.city, self.country)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    p1 = Person("John", "Smith", "19.09.1979", "welder", 15, 3600, "Canada", "Vancouver", "male")
    p2 = Person("Hanna Rose", "May", "05.12.1995", "designer", 2.2, 2150, "Austria", "Vienna")
    assert p1.name() == "John Smith", "Name"
    assert p1.age() == 38, "Age"
    assert p2.work() == "Is a designer", "Job"
    assert p1.money() == "648 000", "Money"
    assert p2.home() == "Lives in Vienna, Austria", "Home"
    print("Coding complete? Let's try tests!")
