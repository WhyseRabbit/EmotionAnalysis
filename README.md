2022/23/03
This project is an attempt to practice, understand and troubleshoot the finer points of Python and Computer Science as a whole. Due to my lifelong love of role-playing games, both in table-top and video game form, it will be my primary focus. My ultimate goal is to break into the Psychology/Psychiatry/Mental Health field. As such, this is going to begin as a text-based entry where the user enter binary strings. Depending on the action, mental health will increase (or improve) or decrease (meaning mental health will begin to suffer).

The long-term goal is to create a complex text-based game where the user makes choices. The complexities will be increased as the project continues.

This project is an ambitious undertaking, one that will start small with simple addition and subtraction. The goal is, however, to make it seem as realistic as possible (within professional standard reason). Things I look to implement: random events outside the character's/player's expectations or control, higher weights for negative scores early on in life (leading towards biases, representing how early trauma can inform adult actions and decisions), as well as more abstract concepts like Maslow's Hierarchy of needs and Nature vs. Nurture ideas.

Ultimately, it would be nice to "teach" AI about emotions, psychology, and maybe avoid a SkyNet situation. (Kidding. Kind of. But not really.)

2022/03/24
The SimuPerson class has been created, along with a function called "eventTrigger," which asks a question to determine stress. Currently, with the prototype, if stress exceeds 0, user will be asked if they coped well with the challenges of the day. The answer to this query will determine confidence.

Within SimuPerson class, will include emotion function to track such things as joy, pride(will have direct correlation with confidence), amusement, sadness, anger, and fear.

2022/03/25
SimuPerson class now has an "emotions" method that has eight basic feelings with some mixed emotions introduced by comparing float scores of the "main" attributes. This will be a complex set of checks and balances that will be adjusted and rewritten many times before a viable product is possible.
(Reasearch link)[https://positivepsychology.com/emotion-wheel/]

Changed emotions to flat ints for now.

https://www.noldus.com/blog/how-emotions-are-made
Some elements within this article might be of use. Neural Networking will be a future goal if product functions well.
https://chicagoeft.com/the-four-components-of-emotion-guest-blogger-josh-marder-lmft/
Four components: cognition, bodily experience, limbic experience, and action.

Consider the 5 stages of grief: https://www.greatlakespsychologygroup.com/grief/5-stages-grief/
One must, then, also question what counts as tragic enough to "warrant" grief. For every person, this "threshold" is different. One must naturally include a "stressThreshold" and include cross-functionality between "negative" emotions and the "stress" attribute. In an attempt to solve the "timing" of grief, a counter must be included, counting up to a random integer. In the future, mental health issues or lack of coping skills might add to this time if research supports such a thing. For now, we are assuming our SimuPerson is without mental abnormality.

(Intermission: please forgive the random flow of this README file; for now, it is a diary of thoughts, queries, research, and ideas. It will be organized for better flow as the project approaches completion.)

Why are floats the preferred method of measuring the emotions?
Two words that everyone knows well: mixed emotions. Who hasn't heard a friend, relative, or coworker is going on vacation somewhere you've always dreamed, or at least somewhere cool, and been, to some degree, jealous? Depending on the relationship, you might be mostly happy for them, or, depending on your memories of the individual, it might be the triggering event to tell him how pompous he is.

Relationships between things and "people" need to be established to store previous values of emotion. This can likely be done through implementing a dictionary, the "triggeringEvent" being the key and the updated "value" of emotions stored to either increase or decrease as more memories are made with that thing or person.

But what about "ambient" emotion?
Ever have that day where you wake up and just feel like it's going to be a bad day? And then, many time, you're provn right. This is due to perception and "cognitive bias" https://www.verywellmind.com/what-is-a-cognitive-bias-2794963

AGAIN, for now, we are assuming our SimuPerson is well-adjusted, stable, and in a "neutral" state.

2022/03/26

Using emotion wheels as inspiration, basic and more complicated emotions are being built. According to WebMD article, "Depression is not a normal part of grief, but a complication of it." https://www.webmd.com/special-reports/grief-stages/20190711/how-grief-affects-your-body-and-mind
Speculation: perhaps the amount of stress the grief produces (on top of the stress from before the triggeringEvent) and confidence levels affect whether or not depression will become a symptom. If our stressTreshold is 100, 65 seems like a reasonable stress score to trigger depression. Anything under 50 will allow our SimuPerson to pass through the depression phase with relative ease. For the sake of argument, the timing of grief will equal stress - confidence.

What if stress is over 50, but confidence is over 25?
Perhaps depression comes from the time spent under stress from the grieving process?
Need to begin networking for interviews. Could use professional insights to clarify, point out fallacies, and improve direction for this project.
