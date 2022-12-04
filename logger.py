# A helper class for logging all events that happen in the simulation.

class Logger(object):
    def __init__(self, file_name):
        self.file_name = file_name

    # The methods below are just suggestions. You can rearrange these or 
    # rewrite them to better suit your code style. 
    # What is important is that you log the following information from the simulation:
    # Meta data: This shows the starting situtation including:
    #   population, initial infected, the virus, and the initial vaccinated.
    # Log interactions. At each step there will be a number of interaction
    # You should log:
    #   The number of interactions, the number of new infections that occured
    # You should log the results of each step. This should inlcude: 
    #   The population size, the number of living, the number of dead, and the number 
    #   of vaccinated people at that step. 
    # When the simulation concludes you should log the results of the simulation. 
    # This should include: 
    #   The population size, the number of living, the number of dead, the number 
    #   of vaccinated, and the number of steps to reach the end of the simulation. 

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, repro_rate):
        
        file = open(self.file_name, 'w')
        file.write('Herd Immunity Simulation\n')

        # virus and population statistics
        file.write(f'Virus name: {virus_name}\n')
        file.write(f'Reproduction Rate: {repro_rate}\n')
        file.write(f'Mortality Rate: {mortality_rate * 100}%\n')
        file.write(f'Initial size of Population: {pop_size}\n')
        file.write(f'Vaccination Rate: {vacc_percentage}%\n')
        # add date and # of infected eople
                   
        file.close()


    def log_interactions(self, time_step_counter, number_of_interactions, number_of_new_infections):
        # TODO: Finish this method. Think about how the booleans passed (or not passed)
        # represent all the possible edge cases. Use the values passed along with each person,
        # along with whether they are sick or vaccinated when they interact to determine
        # exactly what happened in the interaction and create a String, and write to your logfile.
        file = open(self.file_name, 'a')
        file = open(self.file_name, 'a')
        file.write(f'\nTime Step: {time_step_counter}.\n')
        file.write(f'Number of Interactions: {number_of_interactions} \n')
        file.write(f'New Infections: {number_of_new_infections} \n')

        file.close()

    def log_infection_survival(self, time_step_counter, population_count, total_deaths):
        # TODO: Finish this method. If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile
        file = open(self.file_name, 'a')
        file.write(f'\nTime Step: {time_step_counter}.\n')
        file.write(f'Current number of survivors: {population_count} \n')
        file.write(f'Current deaths:{total_deaths} \n')
        file.close()

    def final_data(self, survivors, deaths, vaccinated, interactions, infections, saved):
        file = open(self.file_name, 'a')
        file.write(f'\nsurvivors: {survivors}.\n')
        file.write(f'Number of deaths: {deaths} \n')
        file.write(f'New of vaccinated:: {vaccinated} \n')
        file.write(f'Interactions: {interactions} \n')
        file.write(f'Infections: {infections} \n')
        file.write(f'Vaccines saved: {saved} \n')
        file.close()

   
test = Logger('test_log')
test.write_metadata(11,12,'Virus',0.1,41)