# This is an algorithm testing

import random

dentures = "I suggest that you have dentures" # missing tooth
clean = "I suggest that you clean your teeth" # cavity, decayed tooth 
dental_fillings = "I suggest that you have a dental filling" # cavity
mouthwash = "I suggest that you buy a mouthwash" # cavity, decayed tooth 
soft_toothbrush = "I suggest that you buy a soft bristled toothbrush" # very bruised tooth 
hard_toothbrush = "I suggest that you buy a hard bristled toothbrush" # uncleaned tooth surface
medium_toothbrush = "I suggest that you buy a medium bristled toothbrush" # very bruised tooth
braces = "I suggest that you inquire for braces" # crooked teeth 
crown = "I suggest that you get a crown" # decayed tooth

class Patient():
    def __init__(self,decayed_tooth,missing_tooth,cavity,very_bruised_tooth,badly_cleaned_tooth,crooked_teeth):
        self.decayed_tooth = decayed_tooth
        self.missing_tooth = missing_tooth
        self.cavity = cavity
        self.very_bruised_tooth = very_bruised_tooth
        self.badly_cleaned_tooth = badly_cleaned_tooth
        self.crooked_teeth = crooked_teeth

        self.suggestions_list = []

    def calculator(self):
        if self.decayed_tooth >= 1:
            self.suggestions_list.append(clean)
        if self.missing_tooth >= 2: 
            self.suggestions_list.append(dentures)
        if self.cavity >= 1:
            self.suggestions_list.append(dental_fillings)
        if self.very_bruised_tooth >= 1:
            self.suggestions_list.append(soft_toothbrush)


    def suggestions(self):
        random_number = random.randint(0,len(self.suggestions_list)-1)
        print(self.suggestions_list[random_number])
        print(self.suggestions_list)

           # decayed_tooth  ,  missing_tooth  ,  cavity  ,  very_bruised_tooth  ,  badly_cleaned_tooth  ,  crooked_teeth
patient_1 = Patient(5,3,3,0,10,0)
patient_1.calculator()
patient_1.suggestions()


