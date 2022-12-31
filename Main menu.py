from cmu_112_graphics import*
from Card_Catalog import*
import random, time

#creates variables to be used for every function that has app as an input
def appStarted(app):
    #General variables
    app.boardColor = "RoyalBlue1"
    app.color = "snow"
    app.margin = 50
    #source for shso.png: https://www.facebook.com/SuperHeroSquadOnline/
    app.logo = app.loadImage('shso.png')
    app.flipLogo = app.logo.transpose(Image.FLIP_LEFT_RIGHT)

    #Variables for load screen
    app.loadScreen = True

    #Variables for start menu
    app.startMenu = False
    
    #Variables for instructions screen
    app.instructions = False
    instruct = ["instruct1.png", "instruct2.png", "instruct3.png", 
                "instruct4.png",
                "instruct5.png", "instruct6.png", "instruct7.png", 
                "instruct8.png", "instruct9.png", "instruct10.png",
                "instruct12.png"]
    app.instructPages = []
    for page in instruct:
        image = app.loadImage(page)
        app.instructPages += [app.scaleImage(image, 1/3)]
    app.num = 0

    #Variables for deck screen
    app.deckMenu = False
    app.deckCatalog = loadClasses()

    #Variables for personal deck screen
    app.myDeck = False
    app.numRows, app.numCols = 8, 5
    app.gridWidth = 11*app.width/20 - 2*(app.margin/5)
    app.gridHeight = app.height - 2*(app.margin/5)

    #Variables for cards and personal deck
    app.currentCard = 0
    app.card = app.deckCatalog[app.currentCard]
    app.cardImage = app.loadImage(app.card.getImage())
    app.personalDeck = dict()
    preLoad = {0:3, 1:3, 2:3, 3:3, 4:3, 5:3, 6:3, 7:3, 8:3, 9:3,
                10:3, 11:3, 12:3, 13:1}
    app.preLoadDeck = dict()
    for key in preLoad:
        app.preLoadDeck[app.deckCatalog[key]] = preLoad[key]
    
    #Variable for game options menu
    app.optionsMenu = False

    #Varibles for game
    app.level = 1
    app.startGame = False
    app.deckImages = []
    app.deck = []
    app.hand1, app.hand2 = [], []
    app.deck1, app.deck2 = [], []
    app.currentPlayer = 0
    app.aiEasy = False
    app.aiTurn = False
    app.passed = False
    app.endTurn = False
    app.aiCard = []
    #app.discard contains the image link for current player discard with
    app.yourDiscard = []
    app.oppDiscard = []
    app.luckyBlock = False
    app.blocked = False

#fills the background of the screen with the board color
def drawBoard(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = app.boardColor)

#creates the logo image, the size is determined by the current screen
def drawLogo(app, canvas):
    if app.startMenu:
        logo1 = app.scaleImage(app.logo, 2/5)
        canvas.create_image(app.width//2, app.height//6, 
                        image = ImageTk.PhotoImage(logo1))
    elif app.loadScreen:
        logo2 = app.scaleImage(app.logo, 5/8)
        canvas.create_image(app.width//2, app.height//3, 
                        image = ImageTk.PhotoImage(logo2))
    return

#provides instruction for the user on how to go to the main menu
def startText(app, canvas):
    canvas.create_text(app.width//2, 2*(app.height//3), 
                        text = "Press the spacebar to start!", fill = "white",
                        font = "Cambria 25 bold")

#creates the buttons for the main menu
def drawMenu(app, canvas):
    #DECK BUTTON
    canvas.create_rectangle(app.width//2 - 90, app.height - app.margin,
                            app.width//2 + 90, app.height - app.margin*3, 
                            fill = app.color, outline = "black", width = 3)
    canvas.create_text(app.width//2, app.height - app.margin*2,
                        text = "Deck", font = "Arial 18")
    #INSTRUCTIONS BUTTON
    canvas.create_rectangle(app.width//2 - 90, app.height - app.margin*4,
                            app.width//2 + 90, app.height - app.margin*6, 
                            fill = app.color, outline = "black", width = 3)
    canvas.create_text(app.width//2, app.height - app.margin*5,
                            text = "Instructions", font = "Arial 18")
    #START BUTTON
    canvas.create_rectangle(app.width//2 - 90, app.height - app.margin*7,
                            app.width//2 + 90, app.height - app.margin*9, 
                            fill = app.color, outline = "black", width = 3)
    canvas.create_text(app.width//2, app.height - app.margin*8,
                        text = "Start", font = "Arial 18")

#Back button to navigate to the previous screen
def backButton(app, canvas):
    canvas.create_rectangle(12*app.width/15, 11*(app.height/12), app.width,
                            app.height, fill = app.color, outline = "black",
                            width = 2)
    canvas.create_text(27*app.width/30, 23*(app.height/24), text = "Go Back",
                        fill = app.boardColor, font = "Arial 15 bold")

#-------User commands-------#
#Key commands to interact with certain screens
def keyPressed(app, event):
    #Key command to enter main menu
    if app.loadScreen and event.key == "Space":
        app.startMenu = True
        app.loadScreen = False
        return
    #Key commands for looking through card catalog
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
            app.personalDeck = copy.copy(app.preLoadDeck)
    #Key commands to navigate through instructions screen
    elif app.instructions:
        if event.key == "Left":
            if app.num > 0:
                app.num -= 1
                return
        elif event.key == "Right":
            if app.num < 10:
                app.num += 1
                return
        return

#Mouse click commands to interact with certain screens
def mousePressed(app, event):
    #button actions for deck menu
    if app.deckMenu:
        if 9*app.height/20 <= event.y <= 11*app.height/20:
            #add button action
            if 23*app.width/40 <= event.x <= 30*app.width/40:
                add = app.personalDeck.get(app.deckCatalog[app.currentCard], 0)
                if add < 3:
                    app.personalDeck[app.card] = add + 1
            #remove button action
            elif 32*app.width/40 <= event.x <= 39*app.width/40:
                if app.card in app.personalDeck:
                    app.personalDeck[app.card] -= 1
                    if app.personalDeck[app.card] == 0:
                        app.personalDeck.pop(app.card)
        #button to enter my deck
        if 32*app.width/40 <= event.x <=  app.width:
            if 13*app.height/20 <= event.y <= 15*app.height/20:
                app.myDeck = True
                app.deckMenu = False
                updateDeck(app)
    #back button actions
    if app.deckMenu or app.myDeck or app.instructions:
        if 11*(app.height/12) <= event.y <= app.height and\
            12*app.width/15 <= event.x <= app.width:
                if app.deckMenu:
                    app.startMenu = True
                    app.deckMenu = False
                elif app.myDeck:
                    app.deckMenu = True
                    app.myDeck = False
                elif app.insturctions:
                    app.deckMenu = True
                    app.instructions = False
    #button actions for start menu
    elif app.startMenu:
        if app.width//2 - 90 <= event.x <= app.width//2 + 90:
            #Deck button action
            if app.height - app.margin*3 <= event.y <= app.height - app.margin:
                app.deckMenu = True
                app.startMenu = False
            #Instructions button action
            elif app.height - app.margin*6 <= event.y \
                <= app.height - app.margin*4:
                app.instructions = True
                app.startMenu = False
            #Start button action
            elif app.height - app.margin*9 <= event.y \
                <= app.height - app.margin*7:
                app.optionsMenu = True
                app.startMenu = False
                updateDeck(app)
    #button actions for options menu
    elif app.optionsMenu:
        if 11*(app.height/12) <= event.y <= app.height and\
           12*app.width/15 <= event.x <= app.width:
                app.startMenu = True
                app.optionsMenu = False
                return
        width = (app.height - app.margin*4)/3
        if app.width//2 - 180 <= event.x <= app.width//2 + 180:
            if len(app.deck) != 40:
                return
            #enter TWO-Player mode
            elif (app.height - (app.margin*3 + width*2)) >= event.y >=\
                (app.height - (app.margin*3 + width*3)):
                app.startGame = True
                app.optionsMenu = False
                app.cardImage, app.card = [], []
                startGame(app)
            #enter AI-Easy mode
            elif app.height - (app.margin*2 + width) >= event.y >=\
                app.height - (app.margin*2 + width*2):
                app.startGame = True
                app.optionsMenu = False
                app.cardImage, app.card = [], []
                app.aiEasy = True
                startGame(app)
            #enter AI-Hard mode
            elif app.height - app.margin >= event.y >=\
                app.height - (app.margin + width):
                print("Coming Soon")
    elif app.startGame:  
        #Quit Game
        if 12*app.width/15 <= event.x <= app.width and\
             11*app.height/12 <= event.y <= app.height:
            app.startGame = False
            app.startMenu = True
            app.yourDiscard, app.oppDiscard = [], []
            app.card = app.deckCatalog[app.currentCard]
            app.cardImage = app.loadImage(app.card.getImage())
            app.level = 1
            app.endTurn = False
            app.aiEasy = False
            app.aiCard = []
            app.aiTurn = False
            app.luckyBlock = False
            app.passed = False
            app.currentPlayer = 0
            return
        #at end of turn
        elif app.endTurn and event.x != 0 and event.y != 0:
            time.sleep(0.5)
            app.luckyBlock = False
            app.blocked = False
            app.endTurn = False
            app.passed = False
            #Two Player
            if app.aiEasy == False:
                app.currentPlayer = (app.currentPlayer + 1) % 2
                (app.yourDiscard, app.oppDiscard) =\
                     (app.oppDiscard, app.yourDiscard)
                startTurn(app)
                return
            else:
                #previously your turn
                if app.aiTurn == False:
                    app.aiTurn = True
                    startTurn(app)
                    playAIGame(app)
                    return
                else:
                    app.aiTurn = False
                    startTurn(app)
                    return
        elif app.startGame:
            cardHeight = 120
            image = app.deckImages[0]
            imageWidth, imageHeight = image.size
            scaleFactor = cardHeight/imageHeight
            cardWidth = imageWidth * scaleFactor
            hand = app.hand1
            if app.currentPlayer == 1:
                hand = app.hand2
            #Passing
            if 70 + cardWidth <= event.x <= 140 + cardWidth and\
                app.height - 140 - cardHeight <= event.y\
                    <= app.height - 100 - cardHeight:
                    if app.aiTurn:
                        card = app.aiCard[0]
                        copyCard = Card(card.name, card.level, card.attack, 
                                            copy.copy(card.type), card.blocks,
                                             card.img)
                        damage = recurseDamage(app, copyCard, copyCard.attack, 
                                                app.hand1, app.deck1)
                        app.endTurn = True
                        app.aiCard = []
                        return
                    app.passed = True
                    app.endTurn = True
            #Selecting a Card to play
            elif app.height - 50 - cardHeight <= event.y <= app.height - 50:
                for i in range(len(hand)):
                    if 60 + 5*i + (i+1)*cardWidth <= event.x <=\
                        60 + 5*i + (i+2)*cardWidth:
                        app.card = hand[i][0]
                        app.cardImage = hand[i][1]
                        if app.aiTurn == False:
                            playGame(app)
                        elif app.aiCard != []:
                            result = aiYourResponse(app)
                            if result != None:
                                discard = app.hand1.pop(i)
                                app.yourDiscard = discard[1]
                            if result != "Again" and result != None:
                                app.blocked = True
                                app.endTurn = True
                                app.aiCard = []
                            else:
                                app.card, app.cardImage = [], []
                        break
    return 

def mouseMoved(app, event):
    x, y = event.x, event.y
    if app.myDeck:
        answer = reverseGetCellBounds(app, x, y)
        if answer == None:
            return
        else:
            (r, c) = answer
        for i in range(len(app.deck)):
            if r == i//app.numCols and c == i%app.numCols:
                app.currentCard = i
                updateImage(app)
    elif app.startGame:
        if len(app.hand1) == 0 or len(app.hand2) == 0:
            return
        cardHeight = 120
        image = app.deckImages[0]
        imageWidth, imageHeight = image.size
        scaleFactor = cardHeight/imageHeight
        cardWidth = imageWidth * scaleFactor
        hand = app.hand1
        if bool(app.currentPlayer):
            hand = app.hand2
        if app.height - 50 - cardHeight <= event.y <= app.height - 50:
            for i in range(len(hand)):
                if 60 + 5*i + (i+1)*cardWidth <= event.x <=\
                    60 + 5*i + (i+2)*cardWidth:
                    app.cardImage = hand[i][1]
                    break
        else:
            app.cardImage = []
    return

#Instructions Menu:
def drawInstruct(app, canvas):
    if app.instructions:
        page = app.instructPages[app.num]
        canvas.create_image(app.width/2, app.height/2, 
                        image=ImageTk.PhotoImage(page))
        canvas.create_text(app.width/2, app.height/8, text = 
                            "use left and right arrow keys!",
                            font = "Arial 15 bold")
        return

#-----DECK MENU------#
#Changes current card and corresponding current image for app variables
def updateImage(app): 
    if app.myDeck:
        app.card = app.deck[app.currentCard]
        return
    app.card = app.deckCatalog[app.currentCard]
    app.cardImage = app.loadImage(app.card.getImage())

#Create a list with each card object and its translated image
def updateDeck(app):
    app.deck = []
    app.deckImages = []
    for key in app.personalDeck:
        for i in range(app.personalDeck[key]):
            app.deck += [key]
            app.deckImages += [app.loadImage(key.img)]

#Creates image of the current card
def drawCard(app, canvas):
    scaleFactor = 9/6
    card = app.scaleImage(app.cardImage, scaleFactor)
    canvas.create_image(11*app.width/40, 5*app.height/16, 
                        image=ImageTk.PhotoImage(card))
    cardStatus(app, canvas)

#writes out status of card's placement in deck
def cardStatus(app, canvas):
    #STATUS INFORMATION
    canvas.create_text(6*app.width/40, 20*app.height/32,
                        text = "Status:", anchor = 'nw', fill = "white", 
                        font = "Arial 14 bold")
    if app.card in app.personalDeck:
        canvas.create_text(11*app.width/40, 20*app.height/32, 
                            text = "Added" + "( x" +\
                            f'{app.personalDeck[app.card]}' + ")", 
                            anchor = 'nw', fill = "white", 
                            font = "Arial 14 bold")
    else:
        canvas.create_text(11*app.width/40, 20*app.height/32, 
                            text = "Not added",
                            anchor = 'nw', fill = "white",
                            font = "Arial 14 bold")
    #Deck length info
    deck = []
    for key in app.personalDeck:
        for i in range(app.personalDeck[key]):
            deck += [key]
    canvas.create_text(11*app.width/40, 22*app.height/32,
                        text = "Deck length: " + f'{len(deck)} / 40', 
                        font = "Arial 15 bold",
                        fill = "white")


#Provides you with all the card's information
def cardDescribe(app, canvas):
    margin = app.margin/2
    #background
    canvas.create_rectangle(11*app.width/20, 0, app.width, app.height,
                                fill = "SkyBlue1", 
                                outline = "black", width = 2)
    #card name
    canvas.create_text(23*app.width/40, margin, text = "Name:", anchor ='nw',
                        fill = "black",
                        font = "Arial 14 bold")
    canvas.create_text(27*app.width/40, margin, 
                        text = f'{app.card.getName()}', anchor = 'nw',
                        fill = "black",
                        font = "Arial 14")
    #card level
    canvas.create_text(23*app.width/40, 3*margin, text = "Level:", 
                        anchor = 'nw', fill = "black", font = "Arial 14 bold")
    canvas.create_text(27*app.width/40, 3*margin, 
                        text = f'{app.card.getLevel()}', anchor = 'nw',
                        fill = "black", font = "Arial 14")
    #card attack
    canvas.create_text(23*app.width/40, 5*margin, text = "Attack:",
                        anchor = 'nw', fill = "black", font = "Arial 14 bold")
    canvas.create_text(27*app.width/40, 5*margin, 
                        text = f'{app.card.getAttack()}', anchor = 'nw',
                        fill = "black", font = "Arial 14")
    #card type
    canvas.create_text(23*app.width/40, 7*margin, text = "Type:", anchor = 'nw',
                        fill = "black", font = "Arial 14 bold")
    canvas.create_text(27*app.width/40, 7*margin, 
                        text = f'{app.card.getType()}', anchor = 'nw',
                        fill = "black", font = "Arial 14")
    #card blocks
    canvas.create_text(23*app.width/40, 9*margin, text = "Blocks:", 
                        anchor = 'nw', fill = "black", font = "Arial 14 bold")
    canvas.create_text(27*app.width/40, 9*margin,
                        text = f'{app.card.getBlocks()}', anchor = 'nw',
                        fill = "black", font = "Arial 14")
    #Instructions for personal deck
    if app.myDeck:
        canvas.create_text(31*app.width/40, 12*margin, 
                            text = 'Scroll over each card', fill = "white",
                            font = "Arial 15 bold italic")
        canvas.create_text(31*app.width/40, 13*margin,
                            text = 'for information',
                            fill = "white",
                            font = "Arial 15 bold italic")

#Draws buttons on deck menu and text instructions
def drawDeckButtons(app, canvas):
    canvas.create_rectangle(0, 3*(app.height/4), app.width, app.height, 
                            fill = app.color, outline = "black", width = 3)
    #text instructions
    canvas.create_text(app.width//2, 13*(app.height/16), 
            text = "Use the left and right arrows to look through the cards!",
            fill = "black", font = "Cambria 15")   
    canvas.create_text(app.width//2, 14*(app.height/16), 
            text = "Press d to use the preload deck",
            fill = "black", font = "Cambria 15")   
    #ADD BUTTON
    canvas.create_rectangle(23*app.width/40, 9*app.height/20, 30*app.width/40,
                            11*app.height/20, fill = 'lime green', width = 2)
    canvas.create_text(53*app.width/80, app.height/2, text = "Add",
                        fill = app.color, font = "Arial 23 bold")
    #REMOVE BUTTON
    canvas.create_rectangle(32*app.width/40, 9*app.height/20, 39*app.width/40,
                            11*app.height/20, fill = 'red', width = 2)
    canvas.create_text(71*app.width/80, app.height/2, text = "Remove",
                            fill = app.color, font = "Arial 22 bold")
    #GO TO MY DECK   
    canvas.create_rectangle(32*app.width/40, 13*app.height/20, app.width,
                            15*app.height/20, fill = "white", outline = "black",
                            width = 2)
    canvas.create_text(36*app.width/40, 14*app.height/20, text = "MY DECK",
                        fill = "black", font = "Arial 15 bold")  

#-------PERSONAL DECK-------#
#Creating the grid display of the user's personal deck
def drawMyDeck(app, canvas):
    drawGrid(app, canvas)
    deck = []
    for key in app.personalDeck:
        for i in range(app.personalDeck[key]):
            deck += [key]
    for i in range(len(app.deckImages)):
        r = i//app.numCols
        c = i%app.numCols
        (x0, y0, x1, y1) = getCellBounds(app, r, c)
        image = app.deckImages[i]
        scaleFactor = 9/32
        card = app.scaleImage(image, scaleFactor)
        canvas.create_image(x0 + (app.gridWidth/app.numCols)/2,  
                            y0 + (app.gridHeight/app.numRows)/2, 
                            image = ImageTk.PhotoImage(card))

#Inscribing for each cell
def drawGrid(app, canvas):
    for r in range(app.numRows):
        for c in range(app.numCols):
            drawCell(app , canvas, r, c)

#Creating a rectangle for each cell
def drawCell(app, canvas, r, c):
    (x0, y0, x1, y1) = getCellBounds(app, r, c)
    canvas.create_rectangle(x0, y0, x1, y1, 
                             outline = 'black', width = 3)

#Defining boundaries for each cell
def getCellBounds(app, r, c):
    margin = app.margin/5
    xScale = (app.gridWidth/app.numCols)
    yScale = (app.gridHeight/app.numRows)
    x0 = margin + xScale*c
    x1 = margin + xScale*(c+1)
    y0 = margin + yScale*r
    y1 = margin + yScale*(r+1)
    return (x0, y0, x1, y1)

def reverseGetCellBounds(app, x, y):
    for r in range(app.numRows):
        for c in range(app.numCols):
            (x0, y0, x1, y1) = getCellBounds(app, r, c)
            if x0 <= x <= x1 and y0 <= y <= y1:
                return (r, c)
    return None

#OPTIONS MENU
def drawOptions(app, canvas):
    width = (app.height - app.margin*4)/3
    #AI Hard BUTTON
    canvas.create_rectangle(app.width//2 - 180, app.height - app.margin,
                            app.width//2 + 180, 
                            app.height - (app.margin + width), 
                            fill = app.color, outline = "black",
                            width = 3)
    canvas.create_text(app.width//2, app.height - app.margin - width*0.5, 
                        text = "AI Hard", font = "Arial 25 bold")
    #AI Easy BUTTON
    canvas.create_rectangle(app.width//2 - 180, 
                            app.height - (app.margin*2 + width),
                            app.width//2 + 180, 
                            app.height - (app.margin*2 + width*2), 
                            fill = app.color, outline = "black",
                            width = 3)
    canvas.create_text(app.width//2, app.height - app.margin*2 - width*1.5,
                            text = "AI Easy", font = "Arial 25 bold")
    #TWO-Player BUTTON
    canvas.create_rectangle(app.width//2 - 180, 
                            app.height - (app.margin*3 + width*2),
                            app.width//2 + 180, 
                            app.height - (app.margin*3 + width*3), 
                            fill = app.color, outline = "black",
                            width = 3)
    canvas.create_text(app.width//2, app.height - app.margin*3 - width*2.5,
                        text = "Two-Player", font = "Arial 25 bold")
    #Back button
    canvas.create_rectangle(12*app.width/15, 11*app.height/12, app.width,
                            app.height, fill = "snow", outline = "black",
                            width = 3)
    canvas.create_text(27*app.width/30, 23*app.height/24, text = "Go Back",
                        fill = "blue2", font = "Arial 15 bold")

#START GAME  
def shuffle(app):
    answer = []
    tempDeck = copy.copy(app.deck)
    images = copy.copy(app.deckImages)
    while len(answer) < len(app.deck):
        n = random.randint(0, len(tempDeck)-1)
        answer += [[tempDeck.pop(n), images.pop(n)]]
    return answer 

#reference: playPig() from Audrey Chen's hw2 of 15112
def startGame(app):
    app.deck1 = shuffle(app)
    app.deck2 = shuffle(app)
    app.hand1, app.hand2 = [], []
    for i in range(4):
        num = random.randint(1,len(app.deck1))
        a = app.deck1.pop(num - 1)
        app.hand1 += [a]
    for i in range(4):
        num = random.randint(1,len(app.deck2))
        a = app.deck2.pop(num - 1)
        app.hand2 += [a]
    startTurn(app)
    return

## GRAPHICS FOR GAME
def drawGameMat(app, canvas):
    hand, deck = app.hand1, app.deck1
    oppHand, oppDeck = app.hand2, app.deck2
    if app.currentPlayer == 1:
        hand, deck = app.hand2, app.deck2
        oppHand, oppDeck = app.hand1, app.deck1
    cardHeight = 120
    image = app.deckImages[0]
    imageWidth, imageHeight = image.size
    scaleFactor = cardHeight/imageHeight
    logo = app.scaleImage(app.logo, 1/7)
    cardWidth = imageWidth * scaleFactor
    #AI's Turn
    if app.aiTurn and app.endTurn == False and len(app.hand1) > 0\
        and len(app.hand2) > 0:
        canvas.create_text(app.width/2, 55 + cardHeight, text = "AI is playing",
                            fill = "MediumPurple1",
                            font = "Arial 20 bold")
    #Pass button
    canvas.create_rectangle(70 + cardWidth, app.height - 100 - cardHeight,
                            140 + cardWidth, app.height - 140 - cardHeight,
                            fill = "green", outline = "white", width = 2)
    canvas.create_text(105 + cardWidth, app.height - 120 - cardHeight, 
                        text = "Pass", fill = "white",
                        font = "Arial 15")
    #Your Deck
    canvas.create_rectangle(40, app.height - 50, 40 + cardWidth, 
                            app.height - 50 - cardHeight,
                            fill = "blue2", outline = "black", width = 3)
    canvas.create_text(40 + cardWidth/2, app.height - 50 - cardHeight/2,
                        text = f'{len(deck)}', fill = "white",
                        font = "Arial 25 bold")
    canvas.create_text(40 + cardWidth/2, app.height - 35, text = "Deck",
                        fill = "white", font = "Arial 15 bold")
    #your discard
    canvas.create_rectangle(40, app.height - 90 - cardHeight, 40 + cardWidth, 
                            app.height - 90 - 2*cardHeight,
                            fill = "grey18", outline = "black", width = 3)
    canvas.create_text(40 + cardWidth/2, app.height - 75 - cardHeight,
                        text = "Discard", fill = "white", 
                        font = "Arial 15 bold")
    if app.yourDiscard != []:
        discard = app.scaleImage(app.yourDiscard, scaleFactor)
        canvas.create_image(40 + cardWidth/2, app.height - 90 - 1.5*cardHeight,
                            image = ImageTk.PhotoImage(discard))
    #Player text
    canvas.create_text(60 + cardWidth, 
                        app.height - 60 - cardHeight, anchor ='sw',
                        text = f'Player {app.currentPlayer + 1}',
                        fill = "yellow",
                        font = "Arial 20 bold")
    if app.aiEasy:
        canvas.create_text(app.width - 40 - cardWidth/2,
                            70 + 2*cardHeight, text = "AI",
                            fill = "white",
                            font = "Arial 20 bold")
    #Hand
    for i in range(len(hand)):
        canvas.create_rectangle(60 + 5*i + (i+1)*cardWidth, app.height - 50, 
                                60 + 5*i + (i+2)*cardWidth, 
                                app.height - 50 - cardHeight,
                                fill = "blue2", outline = "black", width = 3)
        card = app.scaleImage(hand[i][1], scaleFactor)
        canvas.create_image(60 + 5*i + (i+1)*cardWidth + cardWidth/2, 
                            app.height - 50 - cardHeight/2,
                            image = ImageTk.PhotoImage(card))
    canvas.create_text(60 + cardWidth + (5*(len(hand)-2) +\
                         (len(hand))*cardWidth)/2, 
                        app.height - 35, text = "Hand", fill = "white",
                        font = "Arial 15 bold")
    if app.cardImage != [] and app.card == []:
        drawBig(app, canvas)
    if app.card != [] and app.cardImage != []:
        pushCard(app, canvas)
    #opponent deck
    flipLogo = app.scaleImage(app.flipLogo, 1/7)
    canvas.create_rectangle(app.width - 40, 30, app.width - 40 - cardWidth, 
                            30 + cardHeight,
                            fill = "blue2", outline = "black", width = 3)
    canvas.create_text(app.width - 40 - cardWidth/2, 
                        30 + cardHeight/2,
                        text = f'{len(oppDeck)}', fill = "white",
                        font = "Arial 25 bold")
    #opponent hand
    for i in range(len(oppHand)):
        canvas.create_rectangle(app.width - 60 - 5*i - (i+1)*cardWidth, 
                                30, 
                                app.width - 60 - 5*i - (i+2)*cardWidth,
                                30 + cardHeight,
                                fill = "blue2", outline = "black", width = 3)
        canvas.create_image(app.width - 60 - 5*i - ((i+1)*cardWidth) -\
                            cardWidth/2, 
                            30 + cardHeight/2, 
                            image = ImageTk.PhotoImage(flipLogo))
    #opponent discard
    canvas.create_rectangle(app.width - 40, 50 + cardHeight, 
                            app.width - 40 - cardWidth, 
                            50 + 2*cardHeight,
                            fill = "grey18", outline = "black", width = 3)
    if app.oppDiscard != []:
        discard = app.scaleImage(app.oppDiscard, scaleFactor)
        canvas.create_image(app.width - 40 - cardWidth/2, 
                            50 + 1.5*cardHeight,
                            image = ImageTk.PhotoImage(discard))
    #Current Level
    canvas.create_oval(app.width - 120, app.height - 160, app.width - 40, 
                        app.height - 80, fill = "yellow", outline = "black",
                        width = 3)
    canvas.create_text(app.width - 80, app.height - 120, 
                        text = f'{app.level}',
                        fill = "black", font = "Arial 25 bold")
    canvas.create_text(app.width - 80, app.height - 180,
                        text = "Level:", fill = "white",
                        font = "Arial 25")
    #Quit Button
    canvas.create_rectangle(12*app.width/15, 11*app.height/12, app.width,
                            app.height, fill = "red", outline = "white",
                            width = 2)
    canvas.create_text(27*app.width/30, 23*app.height/24, text = "Quit",
                        fill = "white", font = "Arial 18 bold")
    #End of Game
    if len(app.hand1) == 0 or len(app.hand2) == 0:
        winner = app.currentPlayer
        canvas.create_text(app.width/2, app.height/2,
                            text = "GAME OVER", fill = "snow",
                            font = "Arial 35 bold")
        if app.aiEasy and len(app.hand1) == 0:
            canvas.create_text(app.width/2, app.height/2 + 60,
                            text = 'AI wins!',
                            fill = "gold",
                            font = "Arial 25")
        else:
            canvas.create_text(app.width/2, app.height/2 + 60,
                            text = f'Player {winner + 1} wins!',
                            fill = "gold",
                            font = "Arial 25")
        return
    #Lucky Block/Passed
    if app.luckyBlock:
        canvas.create_text(app.width/2, app.height/2, text = "Lucky block!",
                            fill = "orange red",
                            font = "Arial 30 bold")
    elif app.passed:
        canvas.create_text(app.width/2, app.height/2, text = "Passed!",
                            fill = "green",
                            font = "Arial 30 bold")
    elif app.blocked:
        canvas.create_text(app.width/2, app.height/2, text = "Blocked!",
                            fill = "red",
                            font = "Arial 30 bold")
    if app.endTurn:
        canvas.create_text(app.width/2, app.height/2 + 40,
                        text = "Next player's turn! Click anywhere",
                        fill = "white",
                        font = "Arial 15")
    #AI push card
    if app.aiCard != []:
        pushAICard(app, canvas)
    return
#mouse over effect   
def drawBig(app, canvas):
    scaleFactor = 11/10
    image = app.scaleImage(app.cardImage, scaleFactor)
    canvas.create_image(150, 180, image = ImageTk.PhotoImage(image))

#selecting card effect
def pushCard(app, canvas):
    imageCard = app.cardImage
    if app.aiTurn:
        return
    canvas.create_image(app.width/2, app.height/2, 
                        image = ImageTk.PhotoImage(imageCard))

#displaying AI's chosen card
def pushAICard(app, canvas):
    imageCard = app.aiCard[1]
    canvas.create_image(app.width/2, app.height/2, 
                        image = ImageTk.PhotoImage(imageCard))

def startTurn(app):
    if len(app.hand1) > 0 and len(app.hand2) > 0:
        #update decks and hands too
        app.level += random.randint(0, 1)
        currentDeck, hand = app.deck1, app.hand1
        oppDeck, oppHand = app.deck2, app.hand2
        if bool(app.currentPlayer):
            currentDeck, hand = app.deck2, app.hand2
            oppDeck, oppHand = app.deck1, app.hand1
        if app.aiTurn:
            if len(oppDeck) > 0 and len(oppHand) < 5:
                drawCard = oppDeck.pop()
                oppHand += [drawCard]
            return
        elif len(hand) < 5 and len(currentDeck) > 0:
            drawCard = currentDeck.pop()
            hand += [drawCard]
    return

def playGame(app):
    if len(app.hand1) == 0 or len(app.hand2) == 0:
        return
    else: 
        if bool(app.currentPlayer):
            result = playTurn(app, app.hand2, app.deck2, app.hand1, app.deck1)
        else:
            result = playTurn(app, app.hand1, app.deck1, app.hand2, app.deck2)
        if result == "Blocked!":
            app.blocked = True
            app.endTurn = True
        elif result != None:
            damage = result
            print('Wow! You did ' + f'{damage} points of damage!')
            app.endTurn = True
    return

def playTurn(app, hand, deck, oppHand, oppDeck):
    if app.card.level <= app.level:
        card = Card(app.card.name, app.card.level, app.card.attack, 
                    copy.copy(app.card.type), app.card.blocks, app.card.img)
        for i in range(len(hand)):
            handItem = hand[i][0]
            if handItem.getName() == card.getName():
                hand.pop(i)
                if app.currentPlayer == 0:
                    app.hand1 = hand
                else:
                    app.hand2 = hand
                break
        if app.aiEasy:
            damage = aiEasyDamage(app, card, oppHand, oppDeck)
        else:
            damage = calcDamage(app, card, oppHand, oppDeck)
        app.yourDiscard = app.cardImage
        app.card = []
        app.cardImage = []
        return damage
    else:
        app.card = []
        app.cardImage = []
        return None

def printHand(app, hand):
    answer = ""
    for card in hand:
        answer += "\t" + repr(card[0])
    return answer

#for two player, getting input from opposite player
def calcDamage(app, card, oppHand, oppDeck):
    opponent = (app.currentPlayer + 1) % 2
    print(f'PLAYER {opponent + 1}\'s hand:\n', printHand(app, oppHand))
    while True:
        press = app.getUserInput(f'Player {opponent + 1}, press P to pass,' +\
        'or press a number to block:')
        damage = 0
        if press == None:
            print("Try again!")
        elif press.isdigit() and int(press) <= len(oppHand):
            block = oppHand[int(press)-1][0].blocks
            if block in card.type:
                card.type.remove(block)
                discard = oppHand.pop(int(press)-1)
                updateOppDiscard(app, discard[1])
            else:
                print("Illegal move")
                continue
            if card.type == []:
                print("Blocked!")
                return("Blocked!")
            else:
                print("Discard another card")
                continue
        elif press.isalpha() and press.lower() == "p":
            attack = card.attack
            damage = recurseDamage(app, card, attack, oppHand, oppDeck)
            return damage
        else:
            print("Illegal move!")

def updateOppDiscard(app, image):
    app.oppDiscard = image

#recursion
def recurseDamage(app, card, attack, oppHand, oppDeck):
    if attack == 0:
        return 0
    elif len(oppDeck) == 0 and len(oppHand) == 0:
        return 0
    else:
        time.sleep(0.5)
        if len(oppDeck) == 0:
            discard = oppHand.pop()
        else:
            discard = oppDeck.pop()
        print("Discarding... " + f'{discard[0].name}')
        if app.aiTurn:
            app.yourDiscard = discard[1]
        else:
            updateOppDiscard(app, discard[1])
        block = discard[0].blocks
        if block in card.type:
            card.type.remove(block)
        if card.type == []:
            app.luckyBlock = True
            if app.aiTurn:
                updateOppDiscard(app, app.aiCard[1])
            return 1
        else:
            return 1 + recurseDamage(app, card, attack - 1, oppHand, oppDeck)

#AI easy function
def aiEasyDamage(app, card, oppHand, oppDeck):
    attack = card.attack
    damage = 0
    if attack < 7:
        n = random.randint(1, 2)
        if n == 1:
            damage = recurseDamage(app, card, attack, oppHand, oppDeck)
            return damage
        #else try to block
    for oppCard in oppHand:
        if oppCard[0].blocks in card.type and len(card.type) == 1:
            updateOppDiscard(app, oppCard[1])
            oppHand.remove(oppCard)
            return ("Blocked!")
    damage = recurseDamage(app, card, attack, oppHand, oppDeck)
    return damage

def playAIGame(app):
    if len(app.hand1) == 0 or len(app.hand2) == 0:
        return
    else:
        if app.aiEasy:
            result = playAIEasy(app, app.hand2, app.deck2)
            if result != None:
                app.aiCard = result
                return
            else:
                app.passed = True
                app.endTurn = True
                return

def playAIEasy(app, hand, deck):
    possibleCards = []
    for card in hand:
        if card[0].level <= app.level:
            possibleCards += [card]
    if possibleCards == []:
        return None
    #to avoid playing the highest card
    if len(possibleCards) > 1:
        highestAttack = 0
        highestCard = possibleCards[0]
        for card in possibleCards:
            if card[0].attack > highestAttack:
                highestAttack = card[0].attack
                highestCard = card
        possibleCards.remove(highestCard)
    card = possibleCards[random.randint(0, (len(possibleCards)-1))]
    hand.remove(card)
    return card

def aiYourResponse(app):
    card = app.aiCard[0]
    copyCard = Card(card.name, card.level, card.attack, 
                    copy.copy(card.type), card.blocks, card.img)
    #block is legal
    if app.card.blocks in copyCard.type:
        copyCard.type.remove(app.card.blocks)
        app.yourDiscard = app.card
    #block is illegal, try again
    else:
        return None
    #block is successful
    if copyCard.type == []:
        updateOppDiscard(app, app.aiCard[1])
        return("Blocked")
    #can block again
    else:
        return("Again")

def redrawAll(app, canvas):
    drawBoard(app, canvas)
    drawLogo(app, canvas)
    if app.loadScreen:
        startText(app, canvas)
    if app.startMenu:
        drawMenu(app, canvas)
    drawInstruct(app, canvas)
    if app.deckMenu:
        drawCard(app, canvas)
    if app.myDeck or app.deckMenu:
        cardDescribe(app, canvas)
    if app.deckMenu:
        drawDeckButtons(app, canvas)
    if app.myDeck or app.deckMenu or app.instructions or app.optionsMenu:
        backButton(app, canvas)
    if app.myDeck:
        drawMyDeck(app, canvas)
    if app.optionsMenu:
        drawOptions(app, canvas)
    if app.startGame == True:
        drawGameMat(app, canvas)
  
runApp(width = 800, height = 700)