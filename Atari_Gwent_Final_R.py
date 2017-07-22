#Atari-Gwent
import sys
import random
from random import randint    
import random
import time

#ph = placeholder

##ALL FACTIONS##  
FACTIONS = ['''   

        Nilfgaard  

''', '''   

        Nothern Realms 

''', '''  

        Scoia'tael

''', '''    

        Monsters

''']  

directions = ["""Gwent is originally a card game from the Witcher franchise. This version of the game (Atari Gwent) is the game reimagned as a game on the Atari 2600 (although the Atari 2600 would of had better graphics, the name 'Atati Gwent' sounded good.)
                Anyway, here are the rules:
                
                I. General Rules
                The game begins with each player randomly drawing 10 cards from their deck, and ends when both players have either both passed or used all of their cards. 
                Each card has 3 values: Damage, Row, and the Hero status.

                First, the damage: The sum of the all the damage values from your cards determines your victory status. Whoever ends up with more damage at the end of the round wins.

                Second, the rows: All cards have a specific 'row' belonging to one of the 3 rows which are Melee, Ranged, and Siege rows. A card's damage values will only count towards the corresponding row.

                Third, the hero status: Cards with the 'Hero' (Marked by the 'H' in their names) do not get affected by special cards.
                
                There are 2 decks in this version of the game. Northern Realms and Nilfgaard.

                II. Placing cards
                Both players take turns, and one must place down a single card on their turn.
                If a player wishes to stop placing cards, they can 'pass'. When a player passes, they can no longer place cards for the rest of the game.
                If player 1 passes, it is constantly player 2's turn until either player 2 passes or the game ends.

                III. Special Cards
                There are 4 special cards in this game. Frost, Fog, Rain and Clear Weather.

                Frost: Sets all the damage values of the cards in the Melee row to 1. (Excluding hero cards)
                Fog: Sets all the damage values of the cards in the Ranged row to 1. (Excluding hero cards)
                Rain: Sets all the damage values of the cards in the Siege row to 1. (Excluding hero cards)
                Clear Weather: Clears all current weather effects.

                IV. Reading Gwent cards in Atari Gwent:
                Here is an example of a gwent card in Atari Gwent:

                      Vernon Roche_1_1H(10)
                          ^       ^  ^^  ^
                          ^       ^  ^^  ^
                          ^       ^  ^^  Damage 
                          ^       ^  ^^
                          ^       ^  ^^
                          ^       ^  ^Hero value 
                          ^       ^  ^
                          ^       ^ Row
                          ^       ^
                      Card name  Draw number 

                V. And the most important rule:
                Have fun.
                """]
                    
##CARDS FOR EACH DECK## 
class northern:
    def __init__(self, name, nickName, drawNum, damage, row, weatherDamage):
        self.name = name
        self.nickName = nickName 
        self.drawNum = drawNum
        #if userNum = listcard[x].drawNum -> How the user will draw the cards
        self.damage = damage 
        self.row = row
        self.weatherDamage = weatherDamage
      
    def get_damage(self):
        return self.damage

#Some cards in the Northern deck have been nerfed/buffed for balance reasons.
Vernon_1_1H = northern("Vernon Roche_1_1H(10)", "Ver(10)", 1, 10, 1,10)#HERO
John_2_1H = northern("John Natalis_2_1H(10)", "John(10)", 2, 10, 1,10)#HERO
Esterad_3_1H = northern("Esterad Thyssen_3_1H(10)", "Est(10)", 3 , 10, 1,10)#HERO 
Philippa_4_2H = northern("Philippa Eilhart_4_2H(10)", "Phi(10)",4, 10, 2,10)#HERO
Ves_5_1 = northern("Ves_5_1(5)","Ves(5)",5,5,1,1)
Siegfried_6_1 = northern("Siegfried of Denesle_6_1(5)","Sieg(5)",6,5,1,1)
Yarpen_7_1 = northern("Yarpen Zigrin_7_1(2)","Yar(2)",7,2,1,1)
Keira_8_2 = northern("Keira Metz_8_2(5)","Keira(5)",8,5,2,1)
Síle_9_2 = northern("Síle de Tansarville_9_2(5)","Sile(5)",9,5,2,1)
Sabrina_10_2 = northern("Sabrina Glevissig_10_2(4)","Sabri(4)",10,4,2,1)
Sheldon_11_2 =  northern("Sheldon Skaggs_11_2(4)","Shelly(4)",11,4,2,1) 
Dethmold_12_2 = northern("Dethmold_12_2(6)","Deth(6)",12,6,2,1)
Trebuchet_13_3 = northern("Trebuchet_13_3(5)","Trebuchet(5)",13,5,3,1) 
Trebuchet_14_3 = northern("Trebuchet_14_3(5)","Trebuchet(5)",14,5,3,1) 
Redanian_15_1 = northern("Redanian Foot Soldier_15_1(1)","Red(1)",15,1,1,1) 
Ballista_16_3 = northern("Ballista_16_3(6)","Ball(6)",16,6,3,1)
Ballista_17_3 = northern("Ballista_17_3(6)","Ball(6)",17,6,3,1)
Expert_18_3 = northern("Kaedweni Siege Expert_18_3(1)","Expert(1)",18,1,3,1)
Tower_19_3 = northern("Siege Tower_19_3(6)","Tower(6)",19,6,3,1)
Infantry_20_1 = northern('Not so poor Infantry_20_1(4)',"Infantry(4)",20,4,1,1)
Infantry_21_1 = northern('Not so poor infantry_21_1(4)',"Infantry(4)",21,4,1,1)
Hunter_22_2 = northern('Dragon Hunter_22_2(5)','Hunter(5)',22,5,2,1)
Hunter_23_2 = northern('Dragon Hunter_23_2(5)','Hunter(5)',23,5,2,1)
Commando_24_1 = northern('Blue Stripes Commando_24_1(5)','Commando(5)',24,5,1,1)
Commando_25_1 = northern('Blue Stripes Commando_25_1(7)','Commando(5)',25,5,1,1)#Buffed from 5 to 7
Catapult_26_3 = northern('Catapult_26_3(8)','Catapult(8)',26,8,3,1)
Catapult_27_3 = northern('Catapult_27_3(8)','Catapult(8)',27,8,3,1)
Infantry_28_1 = northern('Not so poor Infantry_28_1(6)',"Infantry(6)",28,4,1,1)#Buffed from 1 to 5 to 6
Geralt_29_1H = northern('Geralt_29_1H(15)', 'Geralt(15)', 29, 15, 1,15)#HERO
Ciri_30_1H = northern('Ciri_30_1H(15)', 'Ciri(15)', 30, 15, 1,15)#HERO
Frost_31 = northern('Frost_31','Frost',31,0,4,0)#SPECIAL
Fog_32 = northern('Fog_32', 'Fog',32,0,4,0)#SPECIAL
Rain_33 = northern('Rain_33','Rain',33,0,4,0)#SPECIAL
ClearWeather_34 = northern('Clear_Weather_34', 'Clear Weather', 34, 0, 4,0)#SPECIAL

north_deck = [Vernon_1_1H,John_2_1H,Esterad_3_1H,Philippa_4_2H,Ves_5_1,Siegfried_6_1,Yarpen_7_1,Keira_8_2,Síle_9_2,Sabrina_10_2,Sheldon_11_2,Dethmold_12_2,Trebuchet_13_3,Trebuchet_14_3,Redanian_15_1,Ballista_16_3,Ballista_17_3,Expert_18_3,Tower_19_3,Infantry_20_1,Infantry_21_1,Hunter_22_2,Hunter_23_2,Commando_24_1,Commando_25_1,Catapult_26_3,Catapult_27_3,Infantry_28_1,Geralt_29_1H,Ciri_30_1H,Frost_31,Fog_32,Rain_33,ClearWeather_34]  

Letho_1_1H = northern('Letho_1_1H(10)','Letho(10)',1,10,1,10)#HERO
Menno_2_1H = northern('Menno Coehoorn_2_1H(10)','Menno(10)',2,10,1,10)#HERO
Morvan_3_3H = northern('Morvan Voorhis_3_3H(10)','Morvan(10)',3,10,3,10)#HERO
Tigor_4_2 = northern('Tigor Eggebracht_4_2H(10)','Tigor(10)',4,10,2,10)#HERO
Albrich_5_2 = northern('Albrich_5_2(2)','Albrich(2)',5,2,2,1)
Assire_6_2 = northern('Assire var Anahid_6_2(6)','Ass(6)',6,6,2,1)
Cynthia_7_2 = northern('Cynthia_7_2(4)','Cynth(4)',7,4,2,1)#You know who keeps the cap off the toothpaste? Cynths.
Fringilla_8_2 = northern('Fringilla Vigo_8_2(6)','Fringilla(6)',8,6,2,1)
Mort_9_1 = northern('Morteisen_9_1(3)','Mort(3)',9,3,1,1)
Rainfarn_10_1 = northern('Rainfarn_10_1(4)','Rainfarn(4)',10,4,1,1)
Renuald_11_2 = northern('Renuald aep Mastsen_11_2(5)','Ren(5)',11,5,2,1)
Rotten_12_3 = northern('Rotten_12_3(3)','Rot(3)',12,3,3,1)
Sweers_13_2 = northern('Sweers_13_2(2)','Sweers(2)',13,2,2,1)
Vanhemar_14_2 = northern('Vanhemar_14_2(4)','Van(4)',14,4,2,1)
Vreemde_15_1 = northern('Vreemde_15_1(2)','Vreemde(2)',15,2,1,1)
Cahir_16_1 = northern('Cahir_16_1(6)','Carhir(6)',16,6,1,1)
Puttkammer_17_2 = northern('Puttkammer_17_2(3)','Putt(3)',17,3,2,1)
Archer_18_2 = northern('Archer_18_2(10)','Archer(10)',18,10,2,1)
Archer_19_2 = northern('Archer_19_2(10)','Archer(10)',19,10,2,1)
Scorpion_20_3 = northern('ZekScorpion_20_3(10)','Scorpion(10)',20,10,3,1)
Brigade_21_1 = northern('Brigade_21_1(6)','Brigade(6)',21,6,1,1)#Buffed from 4 to 6
Brigade_22_1 = northern('Brigade_22_1(4)','Brigade(4)',22,4,1,1)
Cavalry_23_1 = northern('Calvalry_23_1(5)','Calvalry(5)',23,5,1,1)
Cavalry_24_1 = northern('Calvalry_24_1(5)','Calvalry(5)',24,5,1,1)
Engineer_25_3 = northern('Engineer_25_3(8)','Engineer(8)',25,8,3,1)#Buffed from 5 to 8
Emissary_26_1 = northern('Emissary_26_1(5)','Emissary(5)',26,5,1,1)
Emissary_27_1 = northern('Emissary_27_1(5)','Emissary(5)',27,5,1,1)
Geralt_28_1H = northern("Geralt_28_1(15)", 'Geralt(15)',28,15,1,15)#HERO
Ciri_29_1H = northern('Ciri_29_1(15)','Ciri(15)',29,15,1,15)#HERO
Frost_30 = northern('Frost_31','Frost',30,0,4,0)#SPECIAL
Fog_31 = northern('Fog_32', 'Fog',31,0,4,0)#SPECIAL
Rain_32 = northern('Rain_33','Rain',32,0,4,0)#SPECIAL
ClearWeather_33 = northern("Clear_Weather_33", 'Clear Weather',33,0,4,0)#SPECIAL

nilfgaard_deck = [Letho_1_1H,Menno_2_1H,Morvan_3_3H,Tigor_4_2,Albrich_5_2,Assire_6_2,Cynthia_7_2,Fringilla_8_2,Mort_9_1,Rainfarn_10_1,Renuald_11_2,Rotten_12_3,Sweers_13_2,Vanhemar_14_2,Vreemde_15_1,Cahir_16_1,Puttkammer_17_2,Archer_18_2,Archer_19_2,Scorpion_20_3,Brigade_21_1,Brigade_22_1,Cavalry_23_1,Cavalry_24_1,Engineer_25_3,Emissary_26_1,Emissary_27_1,Geralt_28_1H,Ciri_29_1H,Frost_30,Fog_31,Rain_32,ClearWeather_33]

#The lists for keeping track of cards & other global variables
#For the player
placed_cards = []
placed_melee = []
placed_ranged = []
placed_seige = []
player_hand = []
placed_hero = []
placed_special = []
player_pass = []
picked_int = 0 


#For the AI
enemy_placed = []
enemy_melee = []
enemy_ranged = []
enemy_seige = []
enemy_hand = []
enemy_hero = []
enemy_special = []
enemy_pass = []
enemys_card_list = []
enemy_index = 0
enemys_placed_cards = 0

#For the dupe
dupe_placed = [] 
dupe_enemy_placed = []
dupe_damage_total = 0
dupe_damage_totale = 0

#For everyone
placed_weather = []
dupe_placed_weather = placed_weather
damage_total = 0
enemy_damage_total = 0
turn_number = 0
players_placed_cards = 0

#WORKING
def get_hand():
  player_deck = north_deck #northDeck
  enemy_deck = nilfgaard_deck #GaardDeck 
  maxnum = len(player_deck)
  maxnum_2 = len(enemy_deck) 

  #Gets a random number, matches it with the card's drawNum, the draws the card.
  drewnum = random.sample(range(1, maxnum), 10)
  for num in drewnum:
    for card in north_deck:
      if card.drawNum == num:
        player_hand.append(card)

  drewnum_2 = random.sample(range(1, maxnum_2), 10)
  for num in drewnum_2:
    for card in enemy_deck:
      if card.drawNum == num:
        enemy_hand.append(card)


def choose_turn():
  if random.randint(0,1) == 0:
    return 'player'
  else:
    return 'computer'

#WORKING
def place_card():
  check_card = []
  global players_placed_cards
  global turn_number
  global player_pass
  
  print("Here are the cards that are currently in your hand:\n")
  for card in player_hand:
    print(card.name) 
  print()  

  print('Just type pass if you are all out of cards.')
  pickedNum = input("Please enter the Draw Number of the card you wish to place down (Or type pass if you wish to pass, and make sure you don't make a typo because it could crash the game).\n")

  #Check if the user choosed to pass or not
  if pickedNum == 'pass':
    player_pass.append('yes')
  else:
    picked_int = int(pickedNum)

    for card in player_hand:
      check_card.append(card.drawNum)

    if picked_int in check_card:
      for card in north_deck:
        if card.drawNum == picked_int:
          if card.row == 1:
            placed_cards.append(card)
            placed_melee.append(card) 
            player_hand.remove(card)
            players_placed_cards += 1
            turn_number += 1
            turn = 'computer'

          elif card.row == 2:
            placed_cards.append(card)
            placed_ranged.append(card)
            player_hand.remove(card)
            players_placed_cards += 1
            turn_number += 1
            turn = 'computer'

          elif card.row == 3:
            placed_cards.append(card)
            placed_seige.append(card)
            player_hand.remove(card)
            players_placed_cards += 1
            turn_number += 1
            turn = 'computer'

          else:
            placed_cards.append(card)
            placed_weather.append(card)
            player_hand.remove(card)
            players_placed_cards += 1
            turn_number += 1
            turn = 'computer'
    else:  
      print()   
      print("The card you wish to place is currently not in your deck. Please try again.\n")
      time.sleep(1)
      place_card()

   

def place_card_ai():
  global turn_number
  global enemys_placed_cards
  global enemy_pass
  dupe_enemy_placed = enemy_placed
  dupe_placed = placed_cards

  check_card = []
  card_order = []
  card_order_2 = []
  
  not_weather_north = [Vernon_1_1H,John_2_1H,Esterad_3_1H,Philippa_4_2H,Ves_5_1,Siegfried_6_1,Yarpen_7_1,Keira_8_2,Síle_9_2,Sabrina_10_2,Sheldon_11_2,Dethmold_12_2,Trebuchet_13_3,Trebuchet_14_3,Redanian_15_1,Ballista_16_3,Ballista_17_3,Expert_18_3,Tower_19_3,Infantry_20_1,Infantry_21_1,Hunter_22_2,Hunter_23_2,Commando_24_1,Commando_25_1,Catapult_26_3,Catapult_27_3,Infantry_28_1,Geralt_29_1H,Ciri_30_1H]
  
  not_weather_nilfgaard = [Letho_1_1H,Menno_2_1H,Morvan_3_3H,Tigor_4_2,Albrich_5_2,Assire_6_2,Cynthia_7_2,Fringilla_8_2,Mort_9_1,Rainfarn_10_1,Renuald_11_2,Rotten_12_3,Sweers_13_2,Vanhemar_14_2,Vreemde_15_1,Cahir_16_1,Puttkammer_17_2,Archer_18_2,Archer_19_2,Scorpion_20_3,Brigade_21_1,Brigade_22_1,Cavalry_23_1,Cavalry_24_1,Engineer_25_3,Emissary_26_1,Emissary_27_1,Geralt_28_1H,Ciri_29_1H]


  #Setting the order of cards
  for card in enemy_hand:
    card_order.append(card)
  for card in card_order:
    card_order_2 = sorted(card_order, key=northern.get_damage)

  #Remove weather cards from card_order_2
  card_order_2 = [card for card in card_order_2 if card not in (Frost_30,Frost_31,Fog_31,Fog_32,Rain_32,Rain_33,ClearWeather_33,ClearWeather_34)]
  
  card_order = sorted(card_order_2, key=northern.get_damage)

  #Check if weather cards will be useful
  if turn_number > 6: 
    def weather_use():
      global enemy_pass
      global turn_number
      def check_frost():
        global enemy_pass
        global turn_number
        global enemys_placed_cards
        #Check for frost
        if Frost_30 in enemy_hand:
          dupe_enemy_placed.append(Frost_30)
          dupe_placed_weather.append(Frost_30)

          if dupe_damage_totale > dupe_damage_total:
            placed_weather.append(Frost_30)
            enemy_hand.remove(Frost_30)
            enemys_placed_cards += 1
            turn_number = turn_number + 1
            turn = 'player'

          else:
            only_weather = any(card in not_weather_north for card in enemy_hand)
            if only_weather == False:
              enemy_pass.append('yes')
              turn_number = turn_number + 1
              #print('weatherpass')
              turn = 'player'


        elif Frost_31 in enemy_hand:
          dupe_enemy_placed.append(Frost_31)
          dupe_placed_weather.append(Frost_31)

          if dupe_damage_totale > dupe_damage_total:
            placed_weather.append(Frost_31)
            enemy_hand.remove(Frost_31)
            enemys_placed_cards += 1
            turn_number = turn_number + 1
            turn = 'player'

          else:
            only_weather = any(card in not_weather_north for card in enemy_hand)
            if only_weather == False:
              enemy_pass.append('yes')
              turn_number = turn_number + 1
              #print('weatherpass')
              turn = 'player'          

      def check_fog():
        global enemy_pass
        global turn_number
        global enemys_placed_cards
        #Check for Fog
        if Fog_31 in enemy_hand:
          dupe_enemy_placed.append(Fog_31)
          dupe_placed_weather.append(Fog_31)
 
          if dupe_damage_totale > dupe_damage_total:
            placed_weather.append(Fog_31)
            enemy_hand.remove(Fog_31)
            enemys_placed_cards += 1
            turn_number = turn_number + 1
            turn = 'player'

          else:
            only_weather = any(card in not_weather_north for card in enemy_hand)
            if only_weather == False:
              enemy_pass.append('yes')
              turn_number = turn_number + 1
              #print('weatherpass')
              turn = 'player'

        elif Fog_32 in enemy_hand:
          dupe_enemy_placed.append(Fog_32)
          dupe_placed_weather.append(Fog_32)

          if dupe_damage_totale > dupe_damage_total:
            placed_weather.append(Fog_32)
            enemy_hand.remove(Fog_32)
            enemys_placed_cards += 1
            turn_number = turn_number + 1
            turn = 'player'

          else:
            only_weather = any(card in not_weather_north for card in enemy_hand)
            if only_weather == False:
              enemy_pass.append('yes')
              turn_number = turn_number + 1
              #print('weatherpass')
              turn = 'player'

      def check_rain():
        global enemy_pass
        global turn_number
        global enemys_placed_cards
        #Check for weather
        if Rain_32 in enemy_hand:
          dupe_enemy_placed.append(Rain_32)
          dupe_placed_weather.append(Rain_32)

          if dupe_damage_totale > dupe_damage_total:
            placed_weather.append(Rain_32)
            enemy_hand.remove(Rain_32)
            enemys_placed_cards += 1
            turn_number = turn_number + 1
            turn = 'player'

          else:
            only_weather = any(card in not_weather_north for card in enemy_hand)
            if only_weather == False:
              enemy_pass.append('yes')
              turn_number = turn_number + 1
              #print('weatherpass')
              turn = 'player'

        elif Rain_33 in enemy_hand:
          dupe_enemy_placed.append(Rain_33)
          dupe_placed_weather.append(Rain_33)

          if dupe_damage_totale > dupe_damage_total:
            placed_weather.append(Rain_33)
            enemy_hand.remove(Rain_33)
            enemys_placed_cards += 1
            turn_number = turn_number + 1
            turn = 'player'

          else:
            only_weather = any(card in not_weather_north for card in enemy_hand)
            if only_weather == False:
              enemy_pass.append('yes')
              turn_number = turn_number + 1
              #print('weatherpass')
              turn = 'player'

      def check_sunny():
        global enemy_pass
        global turn_number
        global enemys_placed_cards
        if ClearWeather_33 in enemy_hand:
          dupe_enemy_placed.append(ClearWeather_33)
          dupe_placed_weather.append(ClearWeather_33)

          if dupe_damage_totale > dupe_damage_total:
            placed_weather.append(ClearWeather_33)
            enemy_hand.remove(ClearWeather_33)
            enemys_placed_cards += 1
            turn_number = turn_number + 1
            turn = 'player'

          else:
            only_weather = any(card in not_weather_north for card in enemy_hand)
            if only_weather == False:
              enemy_pass.append('yes')
              turn_number = turn_number + 1
              #print('weatherpass')
              turn = 'player'

        elif ClearWeather_34 in enemy_hand:
          dupe_enemy_placed.append(ClearWeather_34)
          dupe_placed_weather.append(ClearWeather_34)

          if dupe_damage_totale > dupe_damage_total:
            placed_weather.append(ClearWeather_34)
            enemy_hand.remove(ClearWeather_34)
            enemys_placed_cards += 1
            turn_number = turn_number + 1
            turn = 'player'

          else:
            only_weather = any(card in not_weather_north for card in enemy_hand)
            if only_weather == False:
              enemy_pass.append('yes')
              turn_number = turn_number + 1
              #print('weatherpass')
              turn = 'player'

      check_frost()
      check_fog()
      check_rain()
      check_sunny()
    weather_use()

  #If using weather cards aren't beneficial
  else:
    #Function for incresing the index number the AI will use to draw cards each turn
    global enemy_index
    enemy_index += 1
    #Represents how many cards the AI has placed down. Used to determine if the AI has used up all of the cards. (Is 10 when all the cards are used)
    
    for card in card_order:
      enemys_card_list.append(card)
    enemy_card = enemys_card_list[enemy_index]

    if enemys_placed_cards < 11:
      if enemy_index == 11:
        enemy_pass.append('yes')
        turn = 'player'
      else:
        #Check if melee
        if enemy_card.row == 1:
          enemy_placed.append(enemy_card)
          enemy_melee.append(enemy_card)
          enemys_placed_cards += 1
          turn = 'player'
        #Check if ranged
        elif enemy_card.row == 2:
          enemy_placed.append(enemy_card)
          enemy_ranged.append(enemy_card)
          enemys_placed_cards += 1
          turn = 'player'
        #Check if siege
        elif enemy_card.row == 3:
          enemy_placed.append(enemy_card)
          enemy_seige.append(enemy_card)
          enemys_placed_cards += 1
          turn = 'player'
          

#function for drawing the board for the user.
def gwent_board(): 
  #Variable definitions
  global damage_total
  global enemy_damage_total
  damage_total = 0
  enemy_damage_total = 0
  placed_meleeTotal = 0
  placed_rangedTotal = 0
  placed_seigeTotal = 0
  enemy_melee_total = 0
  enemy_ranged_total = 0
  enemy_siege_total = 0

  weather_melee = 0
  weather_ranged = 0
  weather_siege = 0


  #Check for frost
  if Frost_30 in placed_weather:
    weather_melee = 1
  elif Frost_31 in placed_weather:
    weather_melee = 1

  #Check for fog
  if Fog_31 in placed_weather:
    weather_ranged = 1
  elif Fog_32 in placed_weather:
    weather_ranged = 1

  #Check for rain
  if Rain_32 in placed_weather:
    weather_siege = 1
  elif Rain_33 in placed_weather:
    weather_siege = 1
  
  #Check for Clear Weather  
  if ClearWeather_33 in placed_weather: 
    for card in placed_weather:
      placed_weather.remove(card)
  elif ClearWeather_34 in placed_weather:
    for card in placed_weather:
      placed_weather.remove(card)

  #Calculate Damage
  #For the player
  if weather_melee == 1:
    for card in placed_melee:
      placed_meleeTotal = placed_meleeTotal + card.weatherDamage
      damage_total = damage_total + card.weatherDamage
  else:
    for card in placed_melee:
      placed_meleeTotal = placed_meleeTotal + card.damage
      damage_total = damage_total + card.damage

  if weather_ranged == 1:
    for card in placed_ranged:
      placed_rangedTotal = placed_rangedTotal + card.weatherDamage
      damage_total = damage_total + card.weatherDamage  
  else:
    for card in placed_ranged:
      placed_rangedTotal = placed_rangedTotal + card.damage
      damage_total = damage_total + card.damage

  if weather_siege == 1:
    for card in placed_seige:
      placed_seigeTotal = placed_seigeTotal + card.weatherDamage
      damage_total = damage_total + card.weatherDamage
  else:
    for card in placed_seige:
      placed_seigeTotal = placed_seigeTotal + card.damage
      damage_total = damage_total + card.damage
    


  #For the AI
  if weather_melee == 1:
    for card in enemy_melee:
      enemy_melee_total = enemy_melee_total + card.weatherDamage
      enemy_damage_total = enemy_damage_total + card.weatherDamage
  else:
    for card in enemy_melee:
      enemy_melee_total = enemy_melee_total + card.damage
      enemy_damage_total = enemy_damage_total + card.damage

  if weather_ranged == 1:
    for card in enemy_ranged:
      enemy_ranged_total = enemy_ranged_total + card.weatherDamage
      enemy_damage_total = enemy_damage_total + card.weatherDamage
  else:
    for card in enemy_ranged:
      enemy_ranged_total = enemy_ranged_total + card.damage
      enemy_damage_total = enemy_damage_total + card.damage

  if weather_siege == 1:
    for card in enemy_seige:
      enemy_siege_total = enemy_siege_total + card.weatherDamage
      enemy_damage_total = enemy_damage_total + card.weatherDamage
  else:
    for card in enemy_seige:
      enemy_siege_total = enemy_siege_total + card.damage
      enemy_damage_total = enemy_damage_total + card.damage


  #Drawing the actual board
  MIDLINE ='        +------------------------------------------------------------------'
  SLINE ='        |' 
  row = ['MELEE', 'RANGED',  'SEIGE ']   


  #Display for the enemy faction
  enemyFaction = FACTIONS[0]
  print(enemyFaction)
  print("Weather effects:", end='')
  for card in placed_weather:
    cardName = card.nickName
    print(" {%s} " % (cardName) , end='')
  print()
  print()   
  print("TOTAL: %s" % (enemy_damage_total))
  print()
  print(MIDLINE)     

  #Works by literally just printing out each row every time. Cards don't find their way in.
  for x in range (3):
    print(SLINE)
    print(row[x] ,end = ' ')  
    
    if x == 0:
      print('  |', end = ' ')
      for card in enemy_melee:
        cardName = card.nickName
        print (" [%s] " % (cardName), end = ' ')
      print('   ROW TOTAL: %s ' % (enemy_melee_total), end = ' ') 
      print()
      print(SLINE)
      print(MIDLINE)

    elif x == 1:
      print(' |', end = ' ') 
      for card in enemy_ranged:
        cardName = card.nickName
        print (" [%s] " % (cardName), end = ' ')
      print('   ROW TOTAL: %s ' % (enemy_ranged_total), end = ' ') 
      print()
      print(SLINE)
      print(MIDLINE)

    elif x == 2:
      print(' |', end = ' ') 
      for card in enemy_seige:
        cardName = card.nickName
        print (" [%s] " % (cardName), end = ' ')
      print('   ROW TOTAL: %s ' % (enemy_siege_total), end = ' ') 
      print()
      print(SLINE)
      print(MIDLINE)


  #Display for the player's faction
  playerFaction = FACTIONS[1]
  print(playerFaction)
  print("Weather effects:", end='')
  for card in placed_weather:
    print(" [%s] " % (card.nickName) , end='')
  print()    
  print()
  print("TOTAL: %s" % (damage_total))
  print( )
  print(MIDLINE)    

  for x in range (3):
    print(SLINE)
    print(row[x] ,end = ' ')  
    

    if x == 0:
      print('  |', end = ' ') 
      for card in placed_melee:
        cardName = card.nickName
        print (" [%s] " % (cardName), end = ' ')
      print('   ROW TOTAL: %s ' % (placed_meleeTotal), end = ' ') 
      print()
      print(SLINE)
      print(MIDLINE)

    elif x == 1:
      print(' |', end = ' ') 
      for card in placed_ranged:
        cardName = card.nickName
        print (" [%s] " % (cardName), end = ' ')
      print('   ROW TOTAL: %s ' % (placed_rangedTotal), end = ' ') 
      print()
      print(SLINE)
      print(MIDLINE)

    elif x == 2:
      print(' |', end = ' ') 
      for card in placed_seige:
        cardName = card.nickName
        print (" [%s] " % (cardName), end = ' ')
      print('   ROW TOTAL: %s ' % (placed_seigeTotal), end = ' ')  
      print()
      print(SLINE)
      print(MIDLINE)
    

#The duplicate board that the AI will use to determine it's moves
def dupe_board():
  #Variable definitions
  global dupe_damage_total
  global dupe_damage_totale
  player_melee_total = 0
  player_ranged_total = 0
  player_siege_total = 0
  dupe_enemy_melee_total = 0
  dupe_enemy_ranged_total = 0
  dupe_enemy_siege_total = 0

  dupe_enemy_placed = enemy_placed
  dupe_placed = placed_cards
  #dupe_damage_totale = 0
  #dupe_damage_total = 0  

  weather_melee = 0
  weather_ranged = 0
  weather_siege = 0

 #Check for frost
  if Frost_30 in dupe_placed_weather:
    weather_melee = 1
  elif Frost_31 in dupe_placed_weather:
    weather_melee = 1

  #Check for fog
  if Fog_31 in dupe_placed_weather:
    weather_ranged = 1
  elif Fog_32 in dupe_placed_weather:
    weather_ranged = 1

  #Check for rain
  if Rain_32 in dupe_placed_weather:
    weather_siege = 1
  elif Rain_33 in dupe_placed_weather:
    weather_siege = 1
  
  #Check for Clear Weather  
  if ClearWeather_33 in dupe_placed_weather: 
    for card in placed_weather:
      placed_weather.remove(card)
  elif ClearWeather_34 in dupe_placed_weather:
    for card in placed_weather:
      placed_weather.remove(card)

  #Calculate Damage
  #For the player
  if weather_melee == 1:
    for card in placed_melee:
      player_melee_total = player_melee_total + card.weatherDamage
      dupe_damage_total = dupe_damage_total + card.weatherDamage
  else:
    for card in placed_melee:
      player_melee_total = player_melee_total + card.damage
      dupe_damage_total = dupe_damage_total + card.damage

  if weather_ranged == 1:
    for card in placed_ranged:
      player_ranged_total = player_ranged_total + card.weatherDamage
      dupe_damage_total = dupe_damage_total + card.weatherDamage
  else:
    for card in placed_ranged:
      player_ranged_total = player_ranged_total + card.damage
      dupe_damage_total = dupe_damage_total + card.damage

  if weather_siege == 1:
    for card in placed_seige:
      player_siege_total = player_siege_total + card.weatherDamage
      dupe_damage_total = dupe_damage_total + card.weatherDamage
  else:
    for card in placed_seige:
      player_siege_total = player_siege_total + card.damage
      dupe_damage_total = dupe_damage_total + card.damage
    


  #For the AI
  if weather_melee == 1:
    for card in enemy_melee:
      dupe_enemy_melee_total = dupe_enemy_melee_total + card.weatherDamage
      dupe_damage_totale = dupe_damage_totale + card.weatherDamage
  else:
    for card in enemy_melee:
      dupe_enemy_melee_total = dupe_enemy_melee_total + card.damage
      dupe_damage_totale = dupe_damage_totale + card.damage

  if weather_ranged == 1:
    for card in enemy_ranged:
      dupe_enemy_ranged_total = dupe_enemy_ranged_total + card.weatherDamage
      dupe_damage_totale = dupe_damage_totale + card.weatherDamage
  else:
    for card in enemy_ranged:
      dupe_enemy_ranged_total = dupe_enemy_ranged_total + card.damage
      dupe_damage_totale = dupe_damage_totale + card.damage

  if weather_siege == 1:
    for card in enemy_seige:
      dupe_enemy_siege_total = dupe_enemy_siege_total + card.weatherDamage
      dupe_damage_totale = dupe_damage_totale + card.weatherDamage
  else:
    for card in enemy_seige:
      dupe_enemy_siege_total = dupe_enemy_siege_total + card.damage
      dupe_damage_totale = dupe_damage_totale + card.damage



def play_again():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

#Game execution
while True:
  def ask_for_directions():
    ask_directions = input("Would you like the directions for Gwent? (Type yes or no)\n")
    print()
    print()
    if ask_directions.lower().startswith('y'):
      print(directions[0])
    elif ask_directions.lower().startswith('n'):
      print()
    else:
      print('Looks like you typed something wrong, try again!')
      print()
      ask_for_directions()
  ask_for_directions()
  
  game_on = True

  #Deciding who will go first
  turn = choose_turn()
  print("The " + turn + " will go first")

  #Getting the hand
  get_hand()

  while game_on:
    #Setting the game up
    dupe_board()
    player_cards = len(player_hand)
    enemy_cards = len(enemy_hand)
    
    #Turn-taking here
    if turn == 'player':
      if 'yes' in player_pass:
        print()
        print('You passed')
        if 'yes' in enemy_pass:
          if damage_total > enemy_damage_total:
            print()
            print('You win!')
            game_on = False
          if enemy_damage_total > damage_total:
            print()
            print('You lose!')
            game_on = False
          elif damage_total == enemy_damage_total:
            print()
            print('The game resulted in a tie!')
            game_on = False
        else:
          turn = 'computer'
      
      else:
        time.sleep(1)
        print()
        print('Your turn!')
        print()
        print('You placed:')
        print(players_placed_cards, end=' ')
        print(' card(s)')
        print('The enemy placed:')
        print(enemys_placed_cards, end=' ')
        print(' card(s)')
        print()
        place_card()
        print()
        print('Your card has been placed. (Or you passed)')
        print()
        time.sleep(1)
        gwent_board()
        
        #Check if the game is over
        if 'yes' in player_pass and 'yes' in enemy_pass:
          if damage_total > enemy_damage_total:
            print()
            print('You win!')
            game_on = False
          if enemy_damage_total > damage_total:
            print()
            print('You lose!')
            game_on = False
          elif damage_total == enemy_damage_total:
            print()
            print('The game resulted in a tie!')
            game_on = False
        elif players_placed_cards == 10 and enemys_placed_cards == 10:
          if damage_total > enemy_damage_total:
            print()
            print('You win!')
            game_on = False
          elif enemy_damage_total > damage_total:
            print()
            print('You lose!')
            game_on = False
          elif damage_total == enemy_damage_total:
            print()
            print('It results in a tie!')
            game_on = False
        else:
          turn = 'computer'
      
    #If it is the computer's turn
    elif turn == 'computer':
      if 'yes' in enemy_pass:
        print()
        print('The enemy passed')
        if 'yes' in player_pass:
          if damage_total > enemy_damage_total:
            print()
            print('You win!')
            game_on = False
          if enemy_damage_total > damage_total:
            print()
            print('You lose!')
            game_on = False
          elif damage_total == enemy_damage_total:
            print()
            print('The game resulted in a tie!')
            game_on = False
        else:
          turn = 'player'
          
      else:
        time.sleep(1)
        print()
        print()
        place_card_ai()
        print()
        print()
        print("The computer has made its move. (Or it passed)")
        print()
        print()
        time.sleep(1)
        gwent_board()
        
        #Check if the game is over
        if 'yes' in player_pass and 'yes' in enemy_pass:
          if damage_total > enemy_damage_total:
            print()
            print('You win!')
            game_on = False
          elif enemy_damage_total > damage_total:
            print()
            print('You lose!')
            game_on = False
          elif damage_total == enemy_damage_total:
            print()
            print('The game resulted in a tie!')
            game_on = False
        elif players_placed_cards == 10 and enemys_placed_cards == 10:
          if damage_total > enemy_damage_total:
            print()
            print('You win!')
            game_on = False
          elif enemy_damage_total > damage_total:
            print()
            print('You lose!')
            game_on = False
          elif damage_total == enemy_damage_total:
            print()
            print('It results in a tie!')
            game_on = False
        else:
          turn = 'player'
        
  #Ask if the user would like to play again
  print()
  print('Thank you for playing!')
  print()
  print('Press enter to end the game')
  input('')
  break