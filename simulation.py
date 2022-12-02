import random, sys
# random.seed(42)
from person import Person
from logger import Logger
from virus import Virus

# Highest level of abstraction. The main class that runs the entire simulation.

class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        # TODO: Create a Logger object and bind it to self.logger.
        # Remember to call the appropriate logger method in the corresponding parts of the simulation.
        self.logger = Logger('logger')
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected
        self.population = self._create_population()
        self.newly_infected = []
        self.average_interactions = 100
        

    def _create_population(self):
        # TODO: Create a list of people (Person instances). This list 
        # should have a total number of people equal to the pop_size. 
        # Some of these people will be uninfected and some will be infected.
        # The number of infected people should be equal to the the initial_infected
        # TODO: Return the list of people
        people = []
        id = 0
        for infected_person in range(self.initial_infected):
            infected_people = Person(id, False, self.virus)
            people.append(infected_people)
            id += 1
        id = self.initial_infected + 1
        for uninfected_person in range(self.pop_size - self.initial_infected):
            uninfected_people = Person(id, False)
            people.append(uninfected_people)
            id += 1
        return people

    def _simulation_should_continue(self):
        # This method will return a booleanb indicating if the simulation 
        # should continue. 
        # The simulation should not continue if all of the people are dead, 
        # or if all of the living people have been vaccinated. 
        # TODO: Loop over the list of people in the population. Return True
        # if the simulation should continue or False if not.
        for person in self.population:
            if person.is_alive == True and person.is_vaccinated == False:
                print("Population still alive and unvaccinated")
                return True
        return False

    def run(self):
        # This method starts the simulation. It should track the number of 
        # steps the simulation has run and check if the simulation should 
        # continue at the end of each step. 
        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate, self.virus.repro_rate)

        time_step_counter = 1
        while self._simulation_should_continue() == True:
            print(f'TIME STEP: {time_step_counter}')
            time_step_counter += 1
            self.time_step()
            self.current_infected = []
            self._infect_newly_infected()
            self.logger.log_time_step(time_step_counter, len(self.newly_infected), self.newly_dead, self.total_infected, self.total_dead, self.total_immune, len(self.population), self.herd_immunity)
            self.newly_dead = 0

        # TODO: Write meta data to the logger. This should be starting 
        # statistics for the simulation. It should include the initial
        # population size and the virus. 

        
        # TODO: When the simulation completes you should conclude this with 
        # the logger. Send the final data to the logger. 
        # self.logger.final_data()

    def time_step(self):
        # This method will simulate interactions between people, calulate 
        # new infections, and determine if vaccinations and fatalities from infections
        # The goal here is have each infected person interact with a number of other 
        # people in the population
        # TODO: Loop over your population
        # For each person if that person is infected
        # have that person interact with 100 other living people 
        # Run interactions by calling the interaction method below. That method
        # takes the infected person and a random person
        for person in self.population:
            if person.infection != None and person.is_alive:
                random_interaction = random.sample(self.population, self.average_interactions)
                for random_person in random_interaction:
                    self.interaction(person, random_person)

    def interaction(self, infected_person, random_person):
        # TODO: Finish this method.
        if random_person.is_vaccinated == True:
            self.logger.log_interactions(infected_person, random_person)
        elif random_person.infection == True:
            self.logger.log_interactions(infected_person, random_person)
        else:
            random_number = random.random()
            if random_number <= self.virus.repro_rate:
                self.newly_infected.append(random_person)
                self.total_infected += 1
                self.logger.log_interactions(infected_person, random_person, infected=True)
        # The possible cases you'll need to cover are listed below:
            # random_person is vaccinated:
            #     nothing happens to random person.
            # random_person is already infected:
            #     nothing happens to random person.
            # random_person is healthy, but unvaccinated:
            #     generate a random number between 0.0 and 1.0.  If that number is smaller
            #     than repro_rate, add that person to the newly infected array
            #     Simulation object's newly_infected array, so that their infected
            #     attribute can be changed to True at the end of the time step.
        # TODO: Call logger method during this method.
        

    def _infect_newly_infected(self):
        for person in self.newly_infected:
            if person.did_survive_infection() == True:
                self.logger.log_infection_survival(person)
                self.current_infected.append(person)
                self.total_immune += 1
                
            else:
                self.logger.log_infection_survival(person, True)
                self.population.remove(person)
                self.newly_dead += 1
                self.total_dead += 1 




virus_name = 'COVID'
repro_rate = 0.5
mortality_rate = 0.12

virus = Virus(virus_name, repro_rate, mortality_rate)

population_size = 500
vacc_percentage = 0.1
initial_infected = 10

sim = Simulation (virus, population_size, vacc_percentage, initial_infected)


sim.run()