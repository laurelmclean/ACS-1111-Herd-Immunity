import random, sys
# random.seed(42)
from person import Person
from logger import Logger
from virus import Virus

# Highest level of abstraction. The main class that runs the entire simulation.

class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        self.logger = Logger('logger')
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected
        self.population = self._create_population()
        self.newly_infected = []
        self.dead_people = []
        self.average_interactions = 100
        self.total_interactions = 0
        self.total_infected = 0 
        self.total_immune = 0
        self.newly_dead = 0
        self.total_dead = 0
        self.saved = 0
        

    def _create_population(self):
        # Creates population based on total vaccinated, uninfected and infected
        people = []
        self.vaccinated =[]
        number_vaccinated = int((self.vacc_percentage/100) * self.pop_size)
        id = 0
        for infected_person in range(self.initial_infected):
            infected_people = Person(id, False, self.virus)
            people.append(infected_people)
            id += 1
        for vaccinated_person in range(number_vaccinated):
            vaccinated_people = Person(id, True)
            people.append(vaccinated_people)
        for uninfected_person in range(self.pop_size - self.initial_infected - number_vaccinated):
            uninfected_people = Person(id, False)
            people.append(uninfected_people)
        for person in people:
            if person.is_vaccinated == True:
                self.vaccinated.append(person)
        return people

    def _simulation_should_continue(self):
        # The simulation should not continue if all of the people are dead, 
        # or if all of the living people have been vaccinated. 
        for person in self.population:
            if person.is_alive == True and person.is_vaccinated == False:
                return True      
        return False
        

    def run(self):
        # This method starts the simulation, tracks the number of 
        # steps the simulation has run and check if the simulation should 
        # continue at the end of each step. 
        # It also sends data to logger

        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate, self.virus.repro_rate)

        time_step_counter = 0
        should_continue = True

        while should_continue:
            time_step_counter += 1
            self.time_step()
            self.logger.log_interactions(time_step_counter, self.total_interactions, len(self.newly_infected))
            self.logger.log_infection_survival(time_step_counter, len(self.population), self.total_dead)
            self.current_infected = []
            self._infect_newly_infected()
            self.newly_dead = 0
            should_continue = self._simulation_should_continue()
        
        self.logger.final_data(len(self.population), self.total_dead, self.total_immune, self.total_interactions, self.total_infected, self.saved)


    def time_step(self):
        # This method will simulate interactions between people, calulate 
        # new infections, and determine vaccinations and fatalities from infections
        # The goal here is have each infected person interact with a number of other 
        # people in the population

        for person in self.population:
            if person.infection != None and person.is_alive:
                if len(self.population) < self.average_interactions:
                    random_interaction = random.sample(self.population, len(self.population))
                else:
                    random_interaction = random.sample(self.population, self.average_interactions)
                for random_person in random_interaction:
                    self.interaction(random_person)
                random_death = random.random()
                if random_death < virus.mortality_rate:
                    person.is_alive = False
                    self.total_dead += 1
                    self.dead_people.append(person)
                    self.population.remove(person)
                else:
                    self.total_immune += 1
                    person.is_vaccinated = True
                    person.infection = None
 

    def interaction(self, random_person):
        # Based on current infection and vaccination status, random person is either infected with virus or not
        self.total_interactions += 1
        if (random_person.is_vaccinated == False) and (random_person.infection == None) and (random_person.is_alive == True):
            infection = random.random()
            if infection < self.virus.repro_rate and random_person not in self.newly_infected:
                self.newly_infected.append(random_person)
                self.total_infected += 1
        elif (random_person.is_vaccinated == True) and (random_person.infection == None) and (random_person.is_alive):
            self.saved +=1

    def _infect_newly_infected(self):
        # Updated infected people to vaccinated and infection
        for person in self.newly_infected:
            person.infection = self.virus
            person.is_vaccinated = True
        
        self.newly_infected =[]


virus_name = 'Small Pox'
repro_rate = 5.8
mortality_rate = 0.15

virus = Virus(virus_name, repro_rate, mortality_rate)

population_size = 10000
vacc_percentage = 20
initial_infected = 4

sim = Simulation (virus, population_size, vacc_percentage, initial_infected)


sim.run()