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


if __name__ == "__main__":
    # This section is incomplete finish it and use it to test your Person class
    # TODO Define a vaccinated person and check their attributes
    vaccinated_person = Person(1, True)
    assert vaccinated_person._id == 1
    assert vaccinated_person.is_alive is True
    assert vaccinated_person.is_vaccinated is True
    assert vaccinated_person.infection is None

    # Create an unvaccinated person and test their attributes
    unvaccinated_person = Person(2, False)
    # TODO Test unvaccinated_person's attributes here...
    assert unvaccinated_person._id ==2
    assert unvaccinated_person.is_alive is True
    assert unvaccinated_person.is_vaccinated is False
    assert unvaccinated_person.infection is None

    # Test an infected person. An infected person has an infection/virus
    # Create a Virus object to give a Person object an infection
    virus = Virus("Dysentery", 0.7, 0.2)
    # Create a Person object and give them the virus infection
    infected_person = Person(3, False, virus)
    # TODO: complete your own assert statements that test
    # the values of each attribute
    # assert ...
    assert infected_person._id == 3
    assert infected_person.is_alive is True
    assert infected_person.is_vaccinated is False
    assert infected_person.infection is virus

    # You need to check the survival of an infected person. Since the chance
    # of survival is random you need to check a group of people. 
    # Create a list to hold 100 people. Use the loop below to make 100 people
    people = []
    for i in range(1, 101):
        people.append(Person(i, False, virus))
        # TODO Make a person with an infection
        # TODO Append the person to the people list
    

    # Now that you have a list of 100 people. Resolve whether the Person 
    # survives the infection or not by looping over the people list. 
    did_survived = 0
    did_not_survive = 0

    for person in people:
        # For each person call that person's did_survive_infection method
        survived = person.did_survive_infection()
        if survived:
            did_survived += 1
        else:
            did_not_survive += 1


    print(did_survived)
    print(did_not_survive)
    # Count the people that survived and did not survive: 
   


    # TODO Loop over all of the people 
    # TODO If a person is_alive True add one to did_survive
    # TODO If a person is_alive False add one to did_not_survive

    # TODO When the loop is complete print your results.
    # The results should roughly match the mortality rate of the virus
    # For example if the mortality rate is 0.2 rough 20% of the people 
    # should succumb. 

    # Stretch challenge! 
    # Check the infection rate of the virus by making a group of 
    # unifected people. Loop over all of your people. 
    # Generate a random number. If that number is less than the 
    # infection rate of the virus that person is now infected. 
    # Assign the virus to that person's infection attribute. 

    # Now count the infected and uninfect people from this group of people. 
    # The number of infectedf people should be roughly the same as the 
    # infection rate of the virus.