from Card_Class import *
#all card images from: https://heroup.fandom.com/wiki
def loadClasses():
#returns a list of Card objects
    #special
    card1 = Card("Ace of Hearts", 6, 5, ["Energy"], "Speed", 
                    'images/Ace_of_hearts.JPG.webp')
    #special
    card2 = Card("Adrenaline Rush", 1, 2, ["Speed"], "Strength", 
                    "images/Adrenaline_Rush.webp")
    card3 = Card("Ahahahahahaha!", 7, 10, ["Speed"], "Animal", 
                "images/Ahahaha!.webp")
    #special
    card4 = Card("Animal Instinct", 3, 2, ["Animal"], "Tech", 
                    "images/Animal_Instinct.webp")
    card5 = Card("Anti-Metal Claws", 3, 5, ["Tech"], "Elemental", 
                    "images/Anti-Metal_Claws.webp")
    card6 = Card("Arachnophobia", 10, 7, ["Animal", "Elemental"], "Speed",
                    "images/Arachnophobia.webp")
    card7 = Card("Armored Tank", 7, 10, ["Strength"], "Tech", 
                    "images/Armored_Tank.webp")
    #special
    card8 = Card("Arms Race", 1, 2, ["Tech"], "Elemental", 
                "images/Arms_Race.webp")
    #special
    card9 = Card("Astonishing Spidergirl", 1, 2, ["Strength"], "Tech", 
                    "images/Astonishing_Spider-Girl.webp")
    card10 = Card("Attack of the 2 Inch Woman", 1, 3, ["Elemental"], "Energy",
                    "images/2_Inch_Woman.webp")
    #special !?
    card11 = Card("Avengers' Courage", 1, 2, ["Elemental"], "Tech", 
                    "images/Avengers_Courage.webp")
    card12 = Card("Blademaster", 7, 10, ["Animal"], "Tech", 
                    "images/Blademaster.webp")
    card13 = Card("Blazing Intellect", 9, 6, ["Elemental", "Tech"], "Speed",
                    "images/Blazing_Intellect.webp")
    #special
    card14 = Card("Blind Date", 7, 2, ["Speed"], "Animal", 
                    "images/Blind_Date.webp")
    #special
    card15 = Card("Body of Steel", 6, 3, ["Strength"], "Energy", 
                    "images/Body_of_Steel.webp")
    card16 = Card("Borrowed Strength", 4, 6, ["Strength"], "Energy", 
                    "images/Borrowed_Strength.webp")
    card17 = Card("Crimson Couple", 7, 4, ["Animal", "Speed"], "Elemental",
                    "images/Crimson_Couple.webp")
    #special
    card18 = Card("Dancing with the Ninja Stars", 10, 5, ["Speed", "Speed"], 
                    "Energy", "images/Dancing_with_the_Ninja.webp")
    card19 = Card("Dino Spikes", 1, 3, ["Animal"], "Strength", 
                    "images/Dino_Spikes.webp")
    #special
    card20 = Card("Doom Shall Prevail!", 14, 14, ["Tech"], "Animal", 
                    "images/Doom_Shall_Prevail.webp")
    #special
    card21 = Card("Double Slam Sandwich", 1, 3, ["Strength"], "Tech", 
                    "images/Double_Slam_Sandwich.webp")
    card22 = Card("Drop the Hulk Bomb", 9, 6, ["Strength", "Speed"],
                    "Animal", "images/Drop_the_Hulk_Bomb.webp")
    #special
    card23 = Card("Electrical Storm", 4, 2, ["Elemental"], "Animal",
                    "images/Electrical_Storm.webp")
    card24 = Card("Explosive Leap", 4, 6, ["Speed"], "Tech", 
                    "images/Explosive_Leap.webp")
    card25 = Card("Fierce Competitor", 2, 4, ["Animal"], "Strength", 
                    "images/Fierce_Competitor.webp")
    #special
    card26 = Card("Flipping Out", 6, 6, ["Speed"], "Strength", 
                    "images/Flipping_Out.png")
    card27 = Card("Fly Girls", 7, 4, ["Speed", "Strength"], "Tech",
                    "images/Fly_Girls.webp")
    #special
    card28 = Card("Fragile Boombot", 3, 2, ["Tech"], "Strength",
                     "images/Fragile_Boombot.webp")
    #special
    card29 = Card("Friends or Enemies?", 9, 6, ["Energy"], "Elemental",
                    "images/Friends_Enemies.webp")
    #special
    card30 = Card("Gotcha!", 1, 2, ["Speed"], "Animal", "images/Gotcha.webp")
    #special
    card31 = Card("Grand Theft", 6, 3, ["Speed", "Speed"], "Animal",
                    "images/Grand_Theft.webp")
    card32 = Card("Group Hug", 7, 10, ["Strength"], "Speed", 
                    "images/Group_Hug.webp")
    #special
    card33 = Card("Hanging Around", 1, 2, ["Speed"], "Tech", 
                    "images/Hanging_Around.webp")
    #special
    card34 = Card("I'll Take That", 3, 4, ["Energy"], "Elemental", 
                    "images/Take_That.webp")
    #special
    card35 = Card("Improbability Field", 2, 3, ["Elemental"], "Tech",
                    "images/Improbability_Field.webp")
    #special
    card36 = Card("Itsy-Bitsy Teeny-Weeny", 3, 2, ["Tech"], "Strength",
                    "images/Itsy-Bitsy.webp")
    card37 = Card("Jab of Justice", 2, 4, ["Strength"], "Speed",
                    "images/Jab_of_Justice.webp")
    card38 = Card("Just One More Bite", 4, 6, ["Animal"], "Strength",
                    "images/Just_One_More.webp")
    #special
    card39 = Card("King_and_Queen", 2, 2, ["Animal"], "Strength", 
                    "images/King_and_Queen.webp")
    card40 = Card("Lay Down the Law", 9, 6, ["Energy, Tech"], "Animal",
                    "images/Lay_Down.webp")
    card41 = Card("Let's Play Twister", 2, 4, ["Speed"], "Elemental",
                    "images/Lets_Play_Twister.webp")
    #special
    card42 = Card("Magnetic Personality", 1, 2, ["Elemental"], "Speed",
                    "images/Magnetic_Personality.webp")
    card43 = Card("Marvelous Strength", 5, 7, ["Strength"], "Animal",
                    "images/Marvelous_Strength.webp")
    #special
    card44 = Card("Maximum Firepower", 4, 2, ["Tech", "Tech"], "Animal",
                    "images/Maximum_Firepower.webp")
    #special
    card45 = Card("Metldown", 3, 2, ["Elemental"], "Strength", 
                    "images/Meltdown.webp")
    card46 = Card("Moonlit Guardian", 6, 8, ["Animal"], "Speed", 
                    "images/Moonlit_Guardian.webp")
    #special
    card47 = Card("Mutant Healing Ability", 4, 2, ["Energy"], "Strength",
                    "images/Mutant_Healing.webp")
    #special
    card48 = Card("Nucleons Going Critical!", 2, 3, ["Tech"], "Speed",
                    "images/Nucleons.webp")
    #special
    card49 = Card("Perfect Imitation", 6, 2, ["Energy"], "Strength", 
                    "images/Perfect_Imitation.webp")
    #special
    card50 = Card("Perfect Solution", 6, 2, ["Tech"], "Elemental",
                    "images/Perfect_Solution.webp")
    #special
    card51 = Card("Power Grab", 11, 5, ["Energy"], "Speed", 
                    "images/Power_Grab.webp")
    #special
    card52 = Card("Prey on the Weak", 8, 3, ["Animal"], "Energy", 
                    "images/Prey_on_Weak.webp")
    card53 = Card("Psychi Cupcake Bomb", 6, 8, ["Energy"], "Strength",
                    "images/Psychic_Cupcake_Bomb.webp")
    #special
    card54 = Card("Pull into Mists", 1, 2, ["Tech"], "Speed", 
                    "images/Pull_into_Mists.webp")
    card55 = Card("Pure Justice", 12, 10, ["Elemental", "Speed"], "Energy",
                    "images/Pure_Justice.webp")
    card56 = Card("Quick as a Wink", 1, 3,["Speed"], "Energy", 
                    "images/Quick_as_Wink.webp")
    #special
    card57 = Card("Rogue's Gallery", 5, 4, ["Energy"], "Strength", 
                    "images/Rogues_Gallery.webp")
    #special
    card58 = Card("Sabotage", 2, 2, ["Energy"], "Elemental", 
                    "images/Sabotage.webp")
    #too special
    # card59 = Card("Seeing with New Eyes", 2, "*", ["Energy"], "Speed", 
    #                 "Seeing_with_New.webp")
    card60 = Card("Size Matters", 7, 4, ["Strength", "Animal"], "Elemental",
                    "images/Size_Matters.webp")
    card61 = Card("Sky Strike", 5, 7, ["Speed"], "Energy", 
                    "images/Sky_Strike.webp")
    card62 = Card("Spectacular Spider-Man", 8, 12, ["Speed"], "Energy", 
                    "images/Spectacular_Spider.webp")
    #special
    card63 = Card("Spider Biter", 2, 3, ["Strength"], "Elemental", 
                    "images/Spider_Biter.webp")
    #special
    card64 = Card("Spider-Sense", 1, 2, ["Animal"], "Elemental", 
                    "images/Spider-Sense.webp")
    #special
    card65 = Card("Spider Swing", 1, 3, ["Strength"], "Animal", 
                    "images/Spider-Swing.webp")
    #special
    card66 = Card("Steel Yourself for Battle", 2, 2, ["Strength"], "Energy",
                    "images/Steel_Yourself.webp")
    card67 = Card("Stunning Beauty", 6, 8, ["Energy"], "Animal", 
                    "images/Stunning_Beauty.webp")
    #special
    card68 = Card("Super Spider Squad", 1, 2, ["Strength"], "Elemental",
                    "images/Super_Spider_Squad.webp")
    #special
    card69 = Card("Supporting Fire", 8, 6, ["Tech"], "Energy", 
                    "images/Supporting_Fire.webp")
    card70 = Card("Surf's Up!", 7, 10, ["Speed"], "Strength", 
                    "images/Surf_Up.webp")
    #special
    card71 = Card("Team Beam", 1, 2, ["Tech"], "Speed", "images/Team_Beam.webp")
    #special
    card72 = Card("The Man without Fear", 6, 5, ["Animal"], "Energy", 
                    "images/The_Man.webp")
    card73 = Card("Trickweb", 1, 3, ["Tech"], "Speed", "images/Trickweb.webp")
    card74 = Card("Weather Prediction? Pain", 8, 12, ["Energy"], "Tech",
                    "images/Weather_Prediction.webp")
    #special
    card75 = Card("Webstacle Course", 5, 3, ["Tech"], "Speed", 
                    "images/Webstacle.webp")
    #special
    card76 = Card("Whisk on the Winds", 6, 3, ["Elemental"], "Speed", 
                    "images/Whisk_on.webp")
    #special
    card77 = Card("Woe is Doom!", 1, 2, ["Strength"], "Tech", 
                    "images/Woe_Is_Doom.webp")
    #special
    card78 = Card("Yoink!", 1, 2, ["Tech"], "Animal", "images/Yoink.webp")
    #special
    card79 = Card("You Can Count on Me", 3, 2, ["Speed"], "Animal", 
                    "images/You_Can_Count.webp")
    #special
    card80 = Card("You Gotta Be Kidding Me!", 3, 3, ["Animal"], "Speed", 
                    "images/You_Gotta_Be.webp")
    return [card3, card5, card6, card7,
            card10, card12, card13, card16, 
            card17, card19, card22, card24, 
            card25, card27, card37, card38, 
            card38, card40, card41, card43, 
            card46, card53, card55, 
            card56, card60, card61, card62, 
            card67, card70, card73, card74] 