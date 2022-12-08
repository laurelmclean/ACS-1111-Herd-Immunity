from datetime import date

# A helper class for logging all events that happen in the simulation.

class Logger(object):
    def __init__(self, file_name):
        self.file_name = file_name


    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, repro_rate):
        today_date = date.today()
        file = open(self.file_name, 'w')
        file.write('Herd Immunity Simulation\n')

        # virus and population statistics
        file.write(f'Virus name: {virus_name}\n')
        file.write(f'Reproduction Rate: {repro_rate}\n')
        file.write(f'Mortality Rate: {mortality_rate * 100}%\n')
        file.write(f'Initial size of Population: {pop_size}\n')
        file.write(f'Vaccination Rate: {vacc_percentage}%\n')
        file.write(f'Date of Simulation: {today_date}\n')
                   
        file.close()


    def log_interactions(self, time_step_counter, number_of_interactions, number_of_new_infections):
        # Logs number of interactions and new infections at each time step
        file = open(self.file_name, 'a')
        file = open(self.file_name, 'a')
        file.write(f'\nTime Step: {time_step_counter}.\n')
        file.write(f'Number of Interactions: {number_of_interactions} \n')
        file.write(f'Number of new Infections: {number_of_new_infections} \n')

        file.close()

    def log_infection_survival(self, time_step_counter, population_count, total_deaths):
        # Logs popualtion count and total death at each time step
        file = open(self.file_name, 'a')
        file.write(f'\nTime Step: {time_step_counter}.\n')
        file.write(f'Current number of survivors: {population_count} \n')
        file.write(f'Current deaths: {total_deaths} \n')
        file.close()

    def final_data(self, survivors, deaths, vaccinated, interactions, infections, saved):
        # logs final data including survivors, deaths, total vaccinated, interactions, infections
        file = open(self.file_name, 'a')
        file.write(f'\nNumber of survivors: {survivors}.\n')
        file.write(f'Number of deaths: {deaths} \n')
        file.write(f'Number of vaccinated people: {vaccinated} \n')
        file.write(f'Total Interactions: {interactions} \n')
        file.write(f'Total Infections: {infections} \n')
        file.write(f'Number of interactions vaccines prevented infection: {saved} \n')
        file.close()

   