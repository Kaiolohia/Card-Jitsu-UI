import pygame
import os
import random

deck = []
selfhand = []
enemyhand = []
selfBank = []
enemyBank = []


width, height = 1080, 720
win = pygame.display.set_mode((width, height))

pygame.display.set_caption('Card Jitsu')

class Colors:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)

class Settings:
    FPS = 144

class Card:
  def __init__(self, givenColor, givenElement, givenValue):
    color = ['red', 'orange', 'yellow','green', 'blue', 'purple']
    element = ['Water', 'Fire', 'Snow']
    self.color = color[givenColor]
    self.element = element[givenElement]
    self.value = givenValue

  def getCard(self):
    returnThis = []
    returnThis.append(self.color)
    returnThis.append(self.element)
    returnThis.append(self.value)
    return returnThis

  def useCard(index, who):
    if who == 'self':
      deal.dealOneCardToSelf()
      return selfhand.pop(index)
    if who == 'enemy':
      deal.dealOneCardToEnemy()
      return enemyhand.pop(index)

class utils:
  def roundWinner(playedcard,enemyCard):
    currentSelfCard = selfhand[playedcard - 1]
    currentEnemyCard = enemyhand[enemyCard]
    if utils.typeWinCons(currentSelfCard, currentEnemyCard):
      return 'Won'
    if utils.typeWinCons(currentEnemyCard, currentSelfCard):
      return 'Lost'
    if currentSelfCard[2] == currentEnemyCard[2]:
      return 'Tied'
    if currentSelfCard[2] > currentEnemyCard[2]:
      return 'Won'
    return 'Lost'

  def typeWinCons(card1, card2): 
    if card1[1] == "Water" and card2[1] == "Fire" or card1[1] == "Fire" and card2[1] == "Snow" or card1[1] == "Snow" and card2[1] == "Water":
      return True

  def bankUpdate(roundwinner, selfcard, enemycard):
    if roundwinner == 'Won':
      selfBank.append(enemycard)
      return
    if roundwinner == 'Lost':
      enemyBank.append(selfcard)
      return
    return
  
  def didIWinYet(bank):
    #elements check
    Fire = False
    Water = False
    Snow = False
    FireColors = []
    WaterColors = []
    SnowColors = []
    for x in range(len(bank)):
      if bank[x][1] == "Fire":
        Fire = True
        FireColors.append(bank[x][0])
        FireColors = list(set(FireColors))
    for x in range(len(bank)):
      if bank[x][1] == "Water":
        Water = True
        WaterColors.append(bank[x][0])
        WaterColors = list(set(SnowColors))
    for x in range(len(bank)):
      if bank[x][1] == "Snow":
        Snow = True
        SnowColors.append(bank[x][0])
        SnowColors = list(set(SnowColors))
    if Fire == True and Water == True and Snow == True:
      return True
    if len(FireColors) == 3 or len(WaterColors) == 3 or len(SnowColors) == 3:
      return True
  
  def newDeck():
    deck.clear()
    for value in range(2,13):
      for color in range(6):
        for element in range(3):
          newCard = Card(color, element, value)
          deck.append(newCard.getCard())

  def newGame():
    utils.newDeck()
    selfhand.clear()
    enemyhand.clear()
    selfBank.clear()
    enemyBank.clear()  

  def isHovered(x1,x2,y1,y2,mouse_pos):
    if mouse_pos[0] >= x1 and mouse_pos[0] <= x2 and mouse_pos[1] >= y1 and mouse_pos[1] <= y2:
        return True
    return False    

  def dynamicSpacer(index):
    for x in index:
      returnValue += 15
    return returnValue

class ui:
  def displayCard(x, y,  color, element, number, bg):
    win.blit(color, (x,y))
    win.blit(number, (x + 5,y + 15))
    win.blit(bg,(x,y))
    win.blit(element, (x + 5, y + 50))

  def displayCardFormat(card, type):
    color = card[0]
    element = card[1]
    value = card[2]
    returnColor = card_border_red
    returnElement = element_fire
    returnValue = number_2
    returnBG = card_bg_fire
    if color == 'red':
      returnColor = card_border_red
    if color == 'blue':
      returnColor = card_border_blue
    if color == 'yellow':
      returnColor = card_border_yellow
    if color == 'green':
      returnColor = card_border_green
    if color == 'orange':
      returnColor = card_border_orange
    if color == 'purple':
      returnColor = card_border_purple
    if element == 'Fire':
      returnElement = element_fire
      returnBG = card_bg_fire
    if element == 'Water':
      returnElement = element_water
      returnBG = card_bg_water
    if element == 'Snow':
      returnElement = element_snow
      returnBG = card_bg_snow
    if value == 2:
      returnValue = number_2
    if value == 3:
      returnValue = number_3
    if value == 4:
      returnValue = number_4
    if value == 5:
      returnValue = number_5
    if value == 6:
      returnValue = number_6
    if value == 7:
      returnValue = number_7
    if value == 8:
      returnValue = number_8
    if value == 9:
      returnValue = number_9
    if value == 10:
      returnValue = number_10
    if value == 11:
      returnValue = number_11
    if value == 12:
      returnValue = number_12
    if type == 'color':
      return returnColor
    if type == 'element':
      return returnElement
    if type == 'value':
      return returnValue
    if type == 'bg':
      return returnBG
    
  def draw():
    win.fill(Colors.WHITE)
    mouse = pygame.mouse.get_pressed()
    ui.displayCard(50,500, ui.displayCardFormat(selfhand[0], 'color'),ui.displayCardFormat(selfhand[0], 'element'),ui.displayCardFormat(selfhand[0], 'value'),ui.displayCardFormat(selfhand[0], 'bg'))
    ui.displayCard(180,500, ui.displayCardFormat(selfhand[1], 'color'),ui.displayCardFormat(selfhand[1], 'element'),ui.displayCardFormat(selfhand[1], 'value'),ui.displayCardFormat(selfhand[1], 'bg'))
    ui.displayCard(310,500, ui.displayCardFormat(selfhand[2], 'color'),ui.displayCardFormat(selfhand[2], 'element'),ui.displayCardFormat(selfhand[2], 'value'),ui.displayCardFormat(selfhand[2], 'bg'))
    ui.displayCard(440,500, ui.displayCardFormat(selfhand[3], 'color'),ui.displayCardFormat(selfhand[3], 'element'),ui.displayCardFormat(selfhand[3], 'value'),ui.displayCardFormat(selfhand[3], 'bg'))
    ui.displayCard(570,500, ui.displayCardFormat(selfhand[4], 'color'),ui.displayCardFormat(selfhand[4], 'element'),ui.displayCardFormat(selfhand[4], 'value'),ui.displayCardFormat(selfhand[4], 'bg'))
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        if utils.isHovered(50,175,500,700,pygame.mouse.get_pos()):
          Card.useCard(0,'self')
        if utils.isHovered(180,305,500,700,pygame.mouse.get_pos()):
          Card.useCard(1,'self')
        if utils.isHovered(310,435,500,700,pygame.mouse.get_pos()):
          Card.useCard(2,'self')
        if utils.isHovered(440,565,500,700,pygame.mouse.get_pos()):
          Card.useCard(3,'self')
        if utils.isHovered(570,695,500,700,pygame.mouse.get_pos()):
          Card.useCard(4,'self')
    pygame.display.update()

  def startgame(activegame):
    win.fill(Colors.WHITE)
    mouse = pygame.mouse.get_pressed()
    if activegame == False:
        pygame.draw.rect(win, Colors.GREEN, Box)
        if utils.isHovered(10,50,500,600, pygame.mouse.get_pos()) and mouse[0]:
            return True
    pygame.display.update()
    return False

class deal:
  def dealNewHandToSelf():
    for index in range(5):
        deckindex = random.randint(0, len(deck)-1)
        selfhand.append(deck[deckindex])
        deck.pop(deckindex)
    return selfhand

  def dealNewHandToEnemy():
    for index in range(5):
        deckindex = random.randint(0, len(deck)-1)
        enemyhand.append(deck[deckindex])
        deck.pop(deckindex)
    return enemyhand
  
  def dealOneCardToSelf():
    deckindex = random.randint(0, len(deck)-1)
    selfhand.append( deck[deckindex])
    deck.pop(deckindex)
    return selfhand

  def dealOneCardToEnemy():
    deckindex = random.randint(0, len(deck)-1)
    enemyhand.append(deck[deckindex])
    deck.pop(deckindex)
    return enemyhand

Box = pygame.Rect(10,500,50,100)
number_2 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'number_2.png')),(30,30))
number_3 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'number_3.png')),(30,30))
number_4 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'number_4.png')),(30,30))
number_5 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'number_5.png')),(30,30))
number_6 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'number_6.png')),(30,30))
number_7 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'number_7.png')),(30,30))
number_8 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'number_8.png')),(30,30))
number_9 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'number_9.png')),(30,30))
number_10 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'number_10.png')),(30,30))
number_11 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'number_11.png')),(30,30))
number_12 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'number_12.png')),(30,30))
card_border_red = pygame.image.load(os.path.join('Assets', 'card_border_red.png'))
card_border_blue = pygame.image.load(os.path.join('Assets', 'card_border_blue.png'))
card_border_yellow = pygame.image.load(os.path.join('Assets', 'card_border_yellow.png'))
card_border_green = pygame.image.load(os.path.join('Assets', 'card_border_green.png'))
card_border_orange = pygame.image.load(os.path.join('Assets', 'card_border_orange.png'))
card_border_purple = pygame.image.load(os.path.join('Assets', 'card_border_purple.png'))
card_bg_fire = pygame.image.load(os.path.join('Assets', 'card_bg_fire.png'))
card_bg_snow = pygame.image.load(os.path.join('Assets', 'card_bg_snow.png'))
card_bg_water = pygame.image.load(os.path.join('Assets', 'card_bg_water.png'))
element_fire = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'fire.png')), (30, 30))
element_water = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'water.png')), (30, 30))
element_snow = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'snow.png')), (30, 30))

Colors = Colors()
Settings = Settings()

def main():
    runtime = True
    clock = pygame.time.Clock()
    activegame = False
    utils.newGame()
    deal.dealNewHandToEnemy()
    deal.dealNewHandToSelf()
    while runtime:
        clock.tick(Settings.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runtime = False
        if activegame == False:
            activegame = ui.startgame(activegame)
        else:
            ui.draw()
        

    pygame.quit()

if __name__ == '__main__':
    main()