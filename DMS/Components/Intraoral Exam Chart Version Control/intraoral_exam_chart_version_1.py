class Intraoral():
    def __init__(self):
        pass 

    def initialize(self):
        self.fill_chart()

    def show_legends(self):
        print("""
        Conditions:
            / : Present Teeth
            D : Decayed Teeth
            M : Missing due to Caruies
            MO : Missing due to Other Causes
            Im : Impacted Tooth
            Sp : Supernumerary Tooth
            Rf : Root Fragment
            Un : Unerupted
        
        
        Restorations & Prosthetics:     
            Am : Amaigam Filling
            Co : Composite Filling
            JC : Jacket Crown
            Ab : Abutment
            Att : Attatchment
            P : Pontic
            In : Inlay
            Imp : Implant
            S : Sealants
            Rm : Removable Denture
            None : none
        
              
        Surgery: 
            X : Extraction due to Caries
            XO : Extraction due to Caries Causes
            None : none
        
        """)

    def fill_chart(self):
        while True:
            
            while True: 

                self.show_legends()
                conditions = input("Conditions: ").upper()
                if conditions == "/" or conditions == "D" or conditions == "M" or conditions == "MD" or conditions == "IM" or conditions == "SP" or conditions == "RF" or conditions == "UN": 
                    print(f"This input is valid: {conditions}")
                    break
                
                else: 
                    print(f"This input is NOT valid: {conditions}. Try Again.")

            while True: 

                self.show_legends()
                restorations_and_prosthetics = input("Restorations & Prosthetics: ").upper()
                if restorations_and_prosthetics == "AM" or restorations_and_prosthetics == "CO" or restorations_and_prosthetics == "JC" or restorations_and_prosthetics == "AB" or restorations_and_prosthetics == "ATT" or restorations_and_prosthetics == "P" or restorations_and_prosthetics == "IN" or restorations_and_prosthetics == "IMP" or restorations_and_prosthetics == "S" or restorations_and_prosthetics == "RM": 
                    print(f"This input is valid: {restorations_and_prosthetics}")
                    break
                elif restorations_and_prosthetics == "NONE":
                    print(f"This input is valid: {restorations_and_prosthetics}")
                    break
                else: 
                    print(f"This input is NOT valid: {restorations_and_prosthetics}. Try Again.")

            while True: 

                self.show_legends()
                surgery = input("Surgery: ").upper()
                if surgery == "X" or surgery == "XO":
                    print(f"This input is valid: {surgery}")
                    break
                elif surgery == "NONE":
                    print(f"This input is valid: {surgery}")
                    break
                else: 
                    print(f"This input is NOT valid: {surgery}. Try Again.")


            
            print(f"This is the user input: {conditions} {restorations_and_prosthetics} {surgery}")

            self.legends(conditions,restorations_and_prosthetics,surgery)
            break


    def legends(self,value_conditions,value_restorations_and_prosthetics,value_surgery):

        conditions = {
            "/" : "Present Teeth",
            "D" : "Decayed Teeth",
            "M" : "Missing due to Caruies",
            "MO" : "Missing due to Other Causes",
            "IM" : "Impacted Tooth",
            "SP" : "Supernumerary Tooth",
            "RF" : "Root Fragment",
            "UN" : "Unerupted",
        }

        restorations_and_prosthetics = {
            "AM" : "Amaigam Filling",
            "CO" : "Composite Filling",
            "JC" : "Jacket Crown",
            "AB" : "Abutment",
            "ATT" : "Attatchment",
            "P" : "Pontic",
            "IN" : "Inlay",
            "IMP" : "Implant",
            "S" : "Sealants",
            "RM" : "Removable Denture",
            "NONE" : "No Restorations and Prosthetics"
        }

        surgery = {
            "X" : "Extraction due to Caries",
            "XO" : "Extraction due to Caries Causes",
            "NONE" : "No Surgery"
        }

        print(f" \nTeeth Condition: {conditions[value_conditions]}")
        print(f"Teeth Restorations & Prosthetics: {restorations_and_prosthetics[value_restorations_and_prosthetics]}")
        print(f"Teeth Surgery: {surgery[value_surgery]} \n ")



    def data_save_to_database(self):
        pass



# RIGHT SET

teeth_5_1 = ""
teeth_5_2 = ""
teeth_5_3 = ""
teeth_5_4 = ""
teeth_5_5 = ""

teeth_1_1 = ""
teeth_1_2 = ""
teeth_1_3 = ""
teeth_1_4 = ""
teeth_1_5 = ""
teeth_1_6 = ""  
teeth_1_7 = ""
teeth_1_8 = ""

teeth_4_1 = ""
teeth_4_2 = ""
teeth_4_3 = ""
teeth_4_4 = ""
teeth_4_5 = ""
teeth_4_6 = ""
teeth_4_7 = ""
teeth_4_8 = ""

teeth_8_1 = ""
teeth_8_2 = ""
teeth_8_3 = ""
teeth_8_4 = ""
teeth_8_5 = ""


# LEFT SET

teeth_6_1 = ""
teeth_6_2 = ""
teeth_6_3 = ""
teeth_6_4 = ""
teeth_6_5 = ""

teeth_2_1 = ""
teeth_2_2 = ""
teeth_2_3 = ""
teeth_2_4 = ""
teeth_2_5 = ""
teeth_2_6 = ""
teeth_2_7 = ""
teeth_2_8 = ""

teeth_3_1 = ""
teeth_3_2 = ""
teeth_3_3 = ""
teeth_3_4 = ""
teeth_3_5 = ""
teeth_3_6 = ""
teeth_3_7 = ""
teeth_3_8 = ""

teeth_7_1 = ""
teeth_7_2 = ""
teeth_7_3 = ""
teeth_7_4 = ""
teeth_7_5 = ""


teeth_1_1 = Intraoral().initialize()
