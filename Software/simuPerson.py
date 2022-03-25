class SimuPerson:
    """
    SimulatedCharacter, for now, will need age (int) and mental health (int)
    later, could include confidence index to reduce strain to mental health
    this will need to come with an if/else statement on how negative situations
    are handled, especially early on in the "sim" life
    """
    def __init__(self):
        self.age = 0.00
        self.stress = 0
        self.confidence = 0
