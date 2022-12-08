import pytest
from person import Person
from logger import Logger
from virus import Virus
from simulation import Simulation

#testing logger with sample data and asserting lines are correct
# run pytest

def test_file_creation():
    # test file name is properly created
    logger_test = Logger('logger_test.txt')
    assert logger_test.file_name == 'logger_test.txt'


def test_metadata():
    # test metadata is properly displayed
    logger_test = Logger('logger_test.txt')
    logger_test.write_metadata(100, 0.01, 'Sniffles', 0.1, 0.60)
    
    with open('logger_test.txt') as log_file:
        data = log_file.readlines()
        assert data[1] == 'Virus name: Sniffles\n'

def test_log_interactions():
    # test log interactions is properly displayed
    logger_test = Logger('logger_test.txt')
    logger_test.log_interactions(1, 10, 3)
    
    with open('logger_test.txt') as log_file:
        data = log_file.readlines()
        assert data[8] == 'Time Step: 1.\n'

def test_log_infection_survival():
    # test log infection survivial is properly displayed
    logger_test = Logger('logger_test.txt')
    logger_test.log_infection_survival(2, 15, 3)
    
    with open('logger_test.txt') as log_file:
        data = log_file.readlines()
        assert data[14] == 'Current deaths: 3 \n'

def test_final_data():
    # test final data is properly displayed
    logger_test = Logger('logger_test.txt')
    logger_test.final_data(30, 12, 22, 233, 12, 123)
    
    with open('logger_test.txt') as log_file:
        data = log_file.readlines()
        assert data[16] == 'Number of survivors: 30.\n'
