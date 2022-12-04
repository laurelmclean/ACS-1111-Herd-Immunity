import random
# random.seed(42)
from virus import Virus

# Represents the people that make up the population that the virus is spreading through.

class Person(object):
    # Define a person. 
    def __init__(self, _id, is_vaccinated, infection = None):
        self._id = _id  # int
        self.is_vaccinated = is_vaccinated #boolean
        self.infection = infection #none by deafult
        self.is_alive = True #true because they start alive

    # check if person survived infection and update is alive, is infected, and is vaccainted based on interaction
    def did_survive_infection(self):
        random_infection = random.random()
        if self.infection:
            if random_infection <= self.infection.mortality_rate:
                self.is_alive = False
                self.is_infected = False
            else:
                self.is_vaccinated = True
                self.is_alive = True
                self.is_infected = False

            return self.is_alive

# Three additional tests on person class

if __name__ == "__main__":
    # Define a vaccinated person and check their attributes
    vaccinated_person = Person(1, True)
    assert vaccinated_person._id == 1
    assert vaccinated_person.is_alive is True
    assert vaccinated_person.is_vaccinated is True
    assert vaccinated_person.infection is None
    print(vaccinated_person.is_vaccinated)

    # Create an unvaccinated person and test their attributes
    unvaccinated_person = Person(2, False)
    assert unvaccinated_person._id ==2
    assert unvaccinated_person.is_alive is True
    assert unvaccinated_person.is_vaccinated is False
    assert unvaccinated_person.infection is None
    print(unvaccinated_person.is_vaccinated)

    # Create a Virus object to give a Person object an infection
    virus = Virus("SmallPox", 5.8, 0.15)
    # Create a Person object and give them the virus infection
    infected_person = Person(3, False, virus)
    assert infected_person._id == 3
    assert infected_person.is_alive is True
    assert infected_person.is_vaccinated is False
    assert infected_person.infection is virus
    print(infected_person.infection.name)

    #additional person to test:
    another_infected_person = Person(12, False, virus)
    assert another_infected_person._id == 12
    assert another_infected_person.is_alive is True
    assert another_infected_person.is_vaccinated is False
    assert another_infected_person.infection is virus
    print(another_infected_person._id)

    # check the survival of an infected person. 
    people = []
    for i in range(1, 101):
        people.append(Person(i, False, virus))


    # Check survival rate
    did_survived = 0
    did_not_survive = 0

    for person in people:
        survived = person.did_survive_infection()
        if person.is_alive == True:
            did_survived += 1
        else:
            did_not_survive += 1


    print(did_survived)
    print(did_not_survive)


    # Stretch challenge! 
    # Check the infection rate of the virus by making a group of 
    # unifected people. 

    uninfected_people = []
    for i in range(1, 101):
        uninfected_people.append(Person(i, False))

    uninfected_number = 100
    infected_number = 0

    for person in uninfected_people:
        random_infection = random.random()
        if random_infection < virus.repro_rate:
            person.infection = virus
            infected_number += 1
        pass

    uninfected_total = uninfected_number - infected_number
    print(f"Uninfected: {uninfected_total}")
    print(f"Infected total: {infected_number}")
