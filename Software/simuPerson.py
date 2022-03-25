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
    
    def emotions(self):
        """
        Information gathered/resources:
        https://positivepsychology.com/emotion-wheel/
        using the principles of the link above, using the base eight
        emotions to build upon others
        For now, the floats are simple, unfounded estimates that will certainly
        change through trial, error, and research
        """
        self.joy = 0
        self.trust = 0
        self.fear = 0
        self.surprise = 0
        self.sadness = 0
        self.disgust = 0
        self.anger = 0
        self.anticipation = 0
        if self.joy >= 1 and self.trust >= 1:
            self.love = 1
        if self.joy >= 1 and self.trust >= 1:
            self.aroused = 1
