from simuPerson import SimuPerson

def eventTrigger() -> list:
    """
    input : str upon binary good/bad, true/false statements
    output : increase age and increase or decrease stress
    
    Simple input message of "Things went well, (True/False)"
    Both statements will increase age, but the answer will change
    whether stress goes up or down

    Program successfully ages up and tracks the "stress" attribute
    Successfully added confidence attribute. Triggers if stress exceeds 0
    will increase if user feels they coped well with the challenges.
    New goal = 
    Nitpicky goal = add a .lower() function
    """
    simPers = SimuPerson()
    affirm = ["Good", "good", "Yes", "yes", "y", "True", "true", "t"]
    deny = ["Bad", "bad", "No", "no", "n", "False", "false", "f"]
    mainQuery = input("How was your day?: ")
    simPers.age += 0.01
    if len(mainQuery) == 1:
        if mainQuery in deny:
            simPers.stress += 1
        elif mainQuery in affirm:
            simPers.stress -= 1
    else:
        listedQuery = mainQuery.split()
        for w in listedQuery:
            if w in deny:
                simPers.stress += 1
            elif w in affirm:
                simPers.stress -= 1
    
    if simPers.stress > 0:
        secQuery = input("I coped well with today's challenges: ")
        if len(secQuery) == 1:
            if secQuery in affirm:
                simPers.confidence += 1
            elif secQuery in deny:
                simPers.confidence -= 1
        else:
            querListTwo = secQuery.split()
            for _ in querListTwo:
                if _ in affirm:
                    simPers.confidence += 1
                elif _ in deny:
                    simPers.confidence -= 1
    
    return [simPers.stress, simPers.confidence, simPers.age]

print(eventTrigger())
