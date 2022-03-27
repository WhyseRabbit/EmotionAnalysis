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

        Switching to a simpler emotion wheel for now:
        https://www.interaction-design.org/literature/article/putting-some-emotion-into-your-design-plutchik-s-wheel-of-emotions
        """
        self.serenity = 0
        self.acceptance = 0
        self.interest = 0
        self.distracted = 0
        self.pensive = 0
        self.bored = 0
        self.annoyed = 0
        self.apprehensive = 0

        # Basic emotion increases
        if self.serenity == 3:
            self.serenity = self.joy = 3
            self.stress -= 1
        if self.joy == 7:
            self.joy = self.ecstasy = 7 # this poses a question: how long can this state last?
            self.stress -= 4
        
        if self.acceptance == 3:
            self.acceptance = self.trust = 3
            self.stress -= 5
        if self.trust == 7:
            self.trust = self.admire = 7
            self.stress += 1
        
        if self.apprehensive == 3:
            self.apprehensive = self.fear = 3
            self.stress += 3
        if self.fear == 7:
            self.fear = self.terrified = 7
            self.stress += 7
        
        if self.distracted == 3:
            self.distracted = self.surprised = 3
        if self.surprised % 2 == 2:
            self.stress += 2
        if self.surprised == 7:
            self.surprised = self.amazed = 7
            self.stress -= 2
        
        if self.pensive == 3:
            self.pensive = self.sad = 3
            self.stress += 1
        if self.sad == 9:
            self.sad = self.grief = 10
            self.stress += 3 * (self.stress // 2)
            self.griefTime = self.stress - self.confidence
            while self.griefTime > 0:
                self.denialTime = (self.griefTime // 3)
                while self.denialTime > 0:
                    self.griefTime, self.denialTime -= 1
                    if self.denialTime == 1:
                        self.anger += (self.griefTime // 2)
                        if self.anger >= 10:
                            self.eventExtremity = (self.anger % 10) # idea = introduce a random, stress-induced event
                if self.eventExtremity > 2:
                    self.angerTime = self.eventExtremity
        
        if self.bored == 3:
            self.bored = self.disgusted = 3
        if self.disgusted == 7:
            self.disgusted = self.loathing = 7
            self.stress += 3
        
        if self.annoyed == 3:
            self.annoyed = self.anger = 3
            self.stress += 5
        if self.anger == 5:
            self.stress += 10
        if self.anger == 7:
            self.anger = self.rage = 7
            self.stress += 2 * (self.stress // 2)
        
        if self.interest == 3:
            self.interest = self.anticipation = 3
            self.stress -= 1
        if self.anticipation == 7:
            self.anticipation = self.vigilance = 7
            self.stress += 1

        # Serenity + Acceptance = Love
        if self.serenity and self.acceptance == 1:
            self.love = 1
        if self.serenity and self.acceptance == 3:
            self.joy = 4
            self.trust = 4
            self.love = 4
        if self.joy and self.trust == 7:
            self.love = 9
            self.ecstasy = 9
            self.admire = 9
        
        # Acceptance + Apprehensive = Submission
        if self.acceptance and self.apprehensive == 1:
            self.submission = 1
        if self.trust and self.fear == 3:
            self.submission = 4
            self.trust = 4
            self.fear = 4
