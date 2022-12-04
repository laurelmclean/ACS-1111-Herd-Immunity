# Models the properties of the virus we wish to simulate.

class Virus(object):
    # Properties and attributes of the virus used in Simulation.
    def __init__(self, name, repro_rate, mortality_rate):
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate


# Test this class
if __name__ == "__main__":
    # Test your virus class by making an instance and confirming 
    # it has the attributes you defined

    # two additional tests added

    virus = Virus("HIV", 3.5, 0.02)
    assert virus.name == "HIV"
    assert virus.repro_rate == 3.5
    assert virus.mortality_rate == 0.02
    print(virus.mortality_rate)

    another_virus = Virus("E. Coli", 1, 0.05)
    assert another_virus.name == "E. Coli"
    assert another_virus.repro_rate == 1
    assert another_virus.mortality_rate == 0.05
    print(another_virus.repro_rate)

    sars = Virus("SARS", 2.5, 0.1)
    assert sars.name == "SARS"
    assert sars.repro_rate == 2.5
    assert sars.mortality_rate == 0.1
    print(sars.name)
