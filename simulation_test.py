import pytest
from person import Person
from logger import Logger
from virus import Virus
from simulation import Simulation

# Test Simulation Class
# Run pytest

def test_simulation_instance():
    # Test instantiation without error
    sim = Simulation ('Sick', 1000, 0.1, 12)
    assert sim

def test_virus_name():
    # Test for Correct Name
    sim = Simulation ('Sick', 1000, 0.1, 12)
    assert sim.virus == 'Sick'

def test_pop_size():
    # Test for population size
    sim = Simulation ('Sick', 1000, 0.1, 12)
    assert sim.pop_size == 1000