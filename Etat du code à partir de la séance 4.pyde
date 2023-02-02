state = 0

def setup():
    size(1440, 1024)
    
    f = loadFont("RustyHooks-Regular-48.vlw")
    textFont(f)
    
def draw():
    login()
    print(mouseX, mouseY)

def gameState():
    if state == 0:
        login()    

def login():
    background(91, 196, 255)
    textAlign(CENTER)
    textSize(128)
    fill(0)
    text("Calcul App", 720, 160)
    fill(148, 216, 255)
    rect(370, 247, 700, 600, 20)
    textAlign(CENTER)
    textSize(24)
    fill(0)
    text("Identifiez vous pour pouvoir jouer !", 720, 285)
    textAlign(CENTER)
    textSize(16)
    text("Nom d'utilisateur", 470, 358)
    fill(183, 224, 248)
    rect(395, 380, 617, 83)
    fill(0)
    text("Mot de Passe", 455, 504)
    fill(183, 224, 248)
    rect(395, 526, 617, 83)
