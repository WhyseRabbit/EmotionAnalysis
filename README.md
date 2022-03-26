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
