from cmu_112_graphics import*
from Card_Catalog import*
import random
def appStarted(app):
    app.loadScreen = True
    app.boardColor = "blue"
    app.buttonColor = "white"
    app.startMenu = False
    app.margin = 50
    #source: https://www.facebook.com/SuperHeroSquadOnline/
    app.logo = app.loadImage('logodownload.jpg')
    app.startGame = False
    app.instructions = False
    #DECK MENU
    app.deckMenu = False
    app.deckCatalog = loadClasses()
    app.currentCard = 0
    app.card = app.deckCatalog[app.currentCard]
    app.cardImage = app.loadImage(app.card.getImage())
    ##okay button/remove button
    app.okayX = app.width/16
    app.okayY = app.height/24
    ##PERSONAL DECK
    app.myDeck = False
    app.personalDeck = dict()
    app.preLoad = {0:3, 1:2, 3:2, 5:2, 6:2, 7:2, 8:3, 10:3, 12:3, 30:3,
                    31:3, 32:3, 33:3, 34:2, 35:2, 36:2}
    # app.preLoad = {0:1, 1:2, 3:2, 5:2}
    app.preLoadDeck = dict()
    for key in app.preLoad:
        app.preLoadDeck[app.deckCatalog[key]] = app.preLoad[key]
    app.margin2 = 10
    app.numRows, app.numCols = 8, 5
    app.gridWidth = (app.width/2 + 10) - 2*app.margin2
    app.gridHeight = app.height - 2*app.margin2
    #GAME
    app.level = 1
    
def drawBoard(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = app.boardColor)

def drawLogo(app, canvas):
    if app.startMenu:
        logo2 = app.scaleImage(app.logo, 3/4)
        canvas.create_image(app.width//2, app.height//6, 
                        image = ImageTk.PhotoImage(logo2))
        return
    elif app.loadScreen:
        canvas.create_image(app.width//2, app.height//3, 
                        image = ImageTk.PhotoImage(app.logo))

def startText(app, canvas):
    if app.loadScreen:
        canvas.create_text(app.width//2, 3*(app.height//4), 
                        text = "Press the spacebar to start!", fill = "white",
                        font = "Cambria 25 bold")

def drawMenu(app, canvas):
    if app.startMenu:
        #DECK BUTTON
        canvas.create_rectangle(app.width//2 - 90, app.height - app.margin,
                                app.width//2 + 90, app.height - app.margin*3, 
                                fill = app.buttonColor, outline = "black",
                                width = 3)
        canvas.create_text(app.width//2, app.height - app.margin*2,
                            text = "Deck", font = "Arial 18")
        #INSTRUCTIONS BUTTON
        canvas.create_rectangle(app.width//2 - 90, app.height - app.margin*4,
                                app.width//2 + 90, app.height - app.margin*6, 
                                fill = app.buttonColor, outline = "black",
                                width = 3)
        canvas.create_text(app.width//2, app.height - app.margin*5,
                            text = "Instructions", font = "Arial 18")
        #START BUTTON
        canvas.create_rectangle(app.width//2 - 90, app.height - app.margin*7,
                                app.width//2 + 90, app.height - app.margin*9, 
                                fill = app.buttonColor, outline = "black",
                                width = 3)
        canvas.create_text(app.width//2, app.height - app.margin*8,
                            text = "Start", font = "Arial 18")
        #ICON BUTTON
        canvas.create_rectangle(app.width - app.width/7, 2, app.width - 2,
                                app.height/9, fill = app.buttonColor, 
                                outline = "black", width = 2)
        canvas.create_text(app.width - app.width/14, app.height/9 + 10, 
                            text = "Icon", fill = "white",
                            font = "Arial 14 bold")
def keyPressed(app, event):
    if app.loadScreen and event.key == "Space":
        app.startMenu = True
        app.loadScreen = False
        return
    elif app.deckMenu:
        if event.key == "Left" and app.currentCard > 0:
            app.currentCard -= 1
            updateImage(app)
        elif event.key == "Left":
            app.currentCard = len(app.deckCatalog) - 1
            updateImage(app)
        elif event.key == "Right" and app.currentCard < \
            (len(app.deckCatalog) - 1):
            app.currentCard += 1
            updateImage(app)
        elif event.key == "Right":
            app.currentCard = 0
            updateImage(app)
        elif event.key == "d":
            app.personalDeck = app.preLoadDeck
        return

def mousePressed(app, event):
    if app.deckMenu:
        if 17*app.okayY <= event.y <= 19*app.okayY:
            #add button
            if app.okayX <= event.x <= app.okayX + 80:
                add = app.personalDeck.get(app.deckCatalog[app.currentCard], 0)
                if add < 3:
                    app.personalDeck[app.card] = add + 1
            elif 7*app.okayX - 80 <= event.x <= 7*app.okayX:
                if app.card in app.personalDeck:
                    app.personalDeck[app.card] -= 1
                    if app.personalDeck[app.card] == 0:
                        app.personalDeck.pop(app.card)
        #button to enter my deck
        if (14*app.okayX - 80) <= event.x <=  app.width:
            if 2*(app.height//3) <= event.y <= 18*app.okayY:
                app.myDeck = True
                []
                app.deckMenu = False
    #back button 
    if  11*(app.height/12) <= event.y <= app.height and\
            14*app.okayX - 80 <= event.x <= app.width:
            if app.deckMenu:
                app.startMenu = True
                app.deckMenu = False
            elif app.myDeck:
                app.deckMenu = True
                app.myDeck = False
    elif app.startMenu == False:
        return
    elif app.width//2 - 90 <= event.x <= app.width//2 + 90:
        if app.height - app.margin*3 <= event.y <= app.height - app.margin:
            app.deckMenu = True
            app.startMenu = False
        elif app.height - app.margin*6 <= event.y <= app.height - app.margin*4:
            app.instructions = True
            app.startMenu = False
        elif app.height - app.margin*9 <= event.y <= app.height - app.margin*7:
            app.startGame = True
            app.startMenu = False
            startGame(app)
        return

def mouseMoved(app, event):
    if app.myDeck == False:
        return
    (x, y) = (event.x, event.y)

#DECK MENU
def updateImage(app): 
    app.card = app.deckCatalog[app.currentCard]
    app.cardImage = app.loadImage(app.card.getImage())
def drawCard(app, canvas):
    if app.deckMenu == False:
        return
    scaleFactor = 4/3
    card = app.scaleImage(app.cardImage, scaleFactor)
    canvas.create_image(app.width//4 + 5, app.height//3 - 10, 
                        image=ImageTk.PhotoImage(card))

def drawCardButtons(app, canvas):
    if app.deckMenu == False:
        return
    canvas.create_rectangle(0, 2*(app.height//3), app.width, app.height, 
                            fill = "pink", outline = "black", width = 3)
    canvas.create_text(app.width//2, 10*(app.height/12) + 20, 
            text = "Use the left and right arrows to look through the cards!",
            fill = "black", font = "Arial 15")   
    canvas.create_text(app.width//2, 10*(app.height/12) + 40, 
            text = "Press d to use preload deck",
            fill = "black", font = "Arial 15")   
    #ADD BUTTON
    canvas.create_rectangle(app.okayX, 17*app.okayY, app.okayX + 80,
                                19*app.okayY, fill = "green")
    canvas.create_text(app.okayX + 40, 18*app.okayY, text = "Add",
                        fill = "black", font = "Arial 15 bold")
    #REMOVE BUTTON
    canvas.create_rectangle(7*app.okayX - 80, 17*app.okayY,
                            7*app.okayX, 19*app.okayY, fill = "red")
    canvas.create_text(7*app.okayX - 40, 18*app.okayY, text = "Remove",
                            fill = "black", font = "Arial 14 bold")
    #GO TO MY DECK   
    canvas.create_rectangle(14*app.okayX - 80, 2*(app.height//3), app.width,
                            18*app.okayY, fill = "white", outline = "black",
                            width = 2)
    canvas.create_text(15*app.okayX - 40, 17*app.okayY, text = "MY DECK",
                        fill = "black", font = "Arial 15 bold")  
    #STATUS INFORMATION
    canvas.create_text((app.width/2 - 3*(app.width/8)) + 10, 
                        2*(app.height//3) - 20,
                        text = "Status:", fill = "white", 
                        font = "Arial 15 bold")
    if app.card in app.personalDeck:
        canvas.create_text(3*(app.width/8) - 15, 2*(app.height//3) - 20,
                        text = "Added" + "( x" +\
                    f'{app.personalDeck[app.card]}' +\
                        ")", 
                        fill = "white", 
                        font = "Arial 14 bold")
    else:
        canvas.create_text(3*(app.width/8) - 15, 2*(app.height//3) - 20,
                        text = "Not added", fill = "white", 
                        font = "Arial 14 bold")

def backButton(app, canvas):
    canvas.create_rectangle(14*app.okayX - 80, 11*(app.height/12), app.width,
                            app.height, fill = "blue", outline = "black",
                            width = 2)
    canvas.create_text(15*app.okayX - 40, 23*(app.height/24), text = "Go Back",
                        fill = "white", font = "Arial 15 bold")

def drawCardDescribe(app, canvas):
    canvas.create_rectangle(app.width/2 + 10, 0, app.width, app.height,
                                fill = "green", outline = "black", width = 3)
    canvas.create_text(app.width/2 + 60, 20, text = "Name:", fill = "black",
                        font = "Arial 14 bold")
    #fix to center text
    canvas.create_text(3*(app.width/4) + 10, 40, 
                        text = f'{app.card.getName()}',
                        fill = "black",
                        font = "Arial 14")
    canvas.create_text(app.width/2 + 60, 70, text = "Level:", fill = "black",
                        font = "Arial 14 bold")
    canvas.create_text(3*(app.width/4) + 10, 100, 
                        text = f'{app.card.getLevel()}',
                        fill = "black",
                        font = "Arial 14")
    canvas.create_text(app.width/2 + 90, 130, text = "Attack Points:", 
                        fill = "black", font = "Arial 14 bold")
    canvas.create_text(3*(app.width/4) + 10, 160, 
                        text = f'{app.card.getAttack()}',
                        fill = "black",
                        font = "Arial 14")
    canvas.create_text(app.width/2 + 60, 190, text = "Type:", 
                        fill = "black", font = "Arial 14 bold")
    canvas.create_text(3*(app.width/4) + 10, 220, 
                        text = f'{app.card.getType()}',
                        fill = "black",
                        font = "Arial 14")
    canvas.create_text(app.width/2 + 60, 250, text = "Blocks:", 
                        fill = "black", font = "Arial 14 bold")
    canvas.create_text(3*(app.width/4) + 10, 280, 
                    text = f'{app.card.getBlocks()}',
                        fill = "black",
                        font = "Arial 14")

#PERSONAL DECK
def drawMyDeck(app, canvas):
    if app.myDeck == False:
        return
    drawGrid(app, canvas)
    deck = []
    for key in app.personalDeck:
        for i in range(app.personalDeck[key]):
            deck += [key]
    for i in range(len(deck)):
        r = i//app.numCols
        c = i%app.numCols
        (x0, y0, x1, y1) = getCellBounds(app, r, c)
        canvas.create_text(x0 + (app.gridWidth/app.numCols)/2, 
                                y0 + (app.gridHeight/app.numRows)/2,
                        text = f'{i + 1}', fill = "white",
                        font = "Arial 20 bold")
    # for r in range(app.numRows):
    #     for c in range(app.numCols):
    #         if len(deck) >= (r+1)*(c+1):
    #             # scaleFactor = 1/4
    #             # app.card = deck[r*c]
    #             # card = app.scaleImage(app.cardImage, scaleFactor)
    #             (x0, y0, x1, y1) = getCellBounds(app, r, c)
    #             canvas.create_text(x0 + (app.gridWidth/app.numCols)/2, 
    #                             y0 + (app.gridHeight/app.numRows)/2,
    #                     text = f'{(r+1)*(c+1)}', fill = "white",
    #                     font = "Arial 20 bold")
                
def getCellBounds(app, r, c):
    xScale = ((app.width/2 + 10 -(app.margin2*2))/app.numCols)
    yScale = ((app.height-(app.margin2*2))/app.numRows)
    x0 = app.margin2 + xScale*c
    x1 = app.margin2 + xScale*(c+1)
    y0 = app.margin2 + yScale*r
    y1 = app.margin2 + yScale*(r+1)
    return (x0, y0, x1, y1)

def getCell(app, x, y):
    cellWidth = app.gridWidth / app.numCols
    cellHeight = app.gridHeight / app.numRows
    row = int((y - app.margin2) / cellHeight)
    col = int((x - app.margin2) / cellWidth)
    return (row, col)

def drawCell(app, canvas, r, c):
    (x0, y0, x1, y1) = getCellBounds(app, r, c)
    canvas.create_rectangle(x0, y0, x1, y1, 
                             outline = 'purple', width = 3)

def drawGrid(app, canvas):
    for r in range(app.numRows):
        for c in range(app.numCols):
            drawCell(app , canvas, r, c)

#START GAME
def shuffle(deck):
    answer = []
    tempDeck = copy.copy(deck)
    while len(answer) < len(deck):
        answer += [tempDeck.pop(random.randint(0, len(tempDeck)-1))]
    return answer 

#reference: playPig() from Audrey Chen's hw2 of 15112
def startGame(app):
    print("THE GAME IS STARTING")
    deck = []
    for key in app.personalDeck:
        for i in range(app.personalDeck[key]):
            deck += [key]
    deck1 = shuffle(deck)
    deck2 = shuffle(deck)
    hand1, hand2 = [], []
    for i in range(4):
        num = random.randint(1,len(deck1))
        a = deck1.pop(num - 1)
        hand1 += [a]
    for i in range(4):
        num = random.randint(1,len(deck2))
        a = deck2.pop(num - 1)
        hand2 += [a]
    currentPlayer = 0
    while len(deck1) > 0 and len(deck2) > 0:
        #update decks and hands too
        app.level += random.randint(0, 1)
        result = playTurn(app, currentPlayer, deck1, deck2, hand1, hand2)
        if result != None:
            damage, deck1, deck2, hand1, hand2 = result
            print('Wow! You did ' + f'{damage} points of damage!')
        else:
            print("Passed!")
        print("Next player's turn")
        print("------------------")   
        currentPlayer = (currentPlayer + 1) % 2
    print(f'Player {(currentPlayer+1)%2 + 1} is the winner! Skill issue')

def playTurn(app, player, deck1, deck2, hand1, hand2):
    deck, hand = deck1, hand1
    oppDeck, oppHand = deck2, hand2
    if bool(player):
        deck, hand = deck2, hand2
        oppDeck, oppHand = deck1, hand1
    if len(hand) < 8:
        drawCard = deck.pop()
        hand += [drawCard]
    print(f"PLAYER {player + 1}:\n",hand)
    print("Current Level:" + f'{app.level}')
    print("Your deck:" + f'{len(deck)}' + '\nOpponent\'s deck:' +\
         f'{len(oppDeck)}')
    while True:
        action = input("Press P to pass, press number to play a card:")
        if action.isdigit() and int(action) <= len(hand):
            num = int(action)- 1
            card = copy.copy(hand[num])
            if card.level <= app.level:
                print("Playing ... " + f'{card.getName()}')
                damage,oppDeck, oppHand =\
                     calcDamage(player, card, oppDeck, oppHand)
                hand.pop(num)
                return (damage, deck, oppDeck, hand, oppHand)
            else:
                print("Illegal Move! Try again")
        elif action.isalpha() and action.lower() == "p":
            return None
        else:
            print("Illegal move! Try again")

def calcDamage(player, card, deck, hand):
    opponent = (player + 1) % 2
    print(f'PLAYER {opponent + 1} hand:\n',hand)
    while True:
        press = input(f'Player {opponent + 1}, press P to pass,' +\
        'or press a number to block:')
        damage = 0
        if press.isdigit() and int(press) <= len(hand):
            block = hand[int(press)-1].blocks
            if block in card.type:
                card.type.remove(block)
                hand.pop(int(press)-1)
            else:
                print("Illegal move")
                continue
            if card.type == []:
                return (damage, deck, hand)
            else:
                print("Discard another card")
                continue
        elif press.isalpha() and press.lower() == "p":
            damage = 0
            for i in range(card.attack):
                if len(deck) == 0 and len(hand) == 0:
                    break
                elif len(deck) == 0:
                    discard = hand.pop()
                else:
                    discard = deck.pop()
                damage += 1
                print("Discarding... " + f'{discard.name}')
                block = discard.blocks
                if block in card.type:
                    card.type.remove(block)
                if card.type == []:
                    print("Lucky block!")
                    break
            return (damage, deck, hand)
        else:
            print("Illegal move!")

def redrawAll(app, canvas):
    drawBoard(app, canvas)
    startText(app, canvas)
    drawLogo(app, canvas)
    drawMenu(app, canvas)
    drawCard(app, canvas)
    if app.myDeck or app.deckMenu:
        drawCardDescribe(app, canvas)
    drawCardButtons(app, canvas)
    if app.myDeck or app.deckMenu:
        backButton(app, canvas)
    drawMyDeck(app, canvas)
runApp(width = 600, height = 700)