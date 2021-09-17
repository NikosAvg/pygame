import pygame,sys,random

class Main:
    def __init__(self):
        self.state = "intro"
        #initialize the x,y,z and user_text at the start and update them if the user wins
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
        self.z = self.x * self.y
        self.user_text = ""

    def state_manager(self):
        if self.state == "intro":
            self.intro()
        if self.state == "main_game":
            self.main_game(self.x,self.y,self.z,self.user_text)
        if self.state == "Winning":
            self.win()
        if self.state == "Loss":
            self.loss()
    #Added to states just for the looks
    def loss(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = "main_game"
                # delete the text if the user loses
                self.user_text = ""
        screen.fill("grey")
        self.button("Try Again!","light blue","dark blue",200,200,100,250)
        self.just_text("Press SPACEBAR to try again",300,40)


    def win(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = "main_game"
                #update x,y,z, user_text if the user wins
                self.x = random.randint(0,99)
                self.y = random.randint(0,99)
                self.z = self.x * self.y
                self.user_text = ""
            screen.fill("grey")
            #   button(self,text,top_colour,bot_colour,pos_x,pos_y,but_height,but_width):
            self.button("You Win","light blue","dark blue",200,200,100,250)
            #   just_text(self,text,pos_x,pos_y)
            self.just_text("Press SPACEBAR to play again",300,40)

    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = "main_game"

        screen.fill("grey")
        #   button(self,text,top_colour,bot_colour,pos_x,pos_y,but_height,but_width):
        self.button("Welcome","light blue","dark blue",200,200,100,250)
        #   just_text(self,text,pos_x,pos_y)
        self.just_text("Press SPACEBAR to continue",300,40)

    def check_answ(self,ans,z):
        if ans==z:
            return True
        return False

    def main_game(self,x,y,z, user_text):
        allowed_keys = [pygame.K_0,pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,pygame.K_5,pygame.K_6,pygame.K_7,pygame.K_8,pygame.K_9]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = "intro"
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                self.user_text = self.user_text[:-1]
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                ans = self.check_answ(int(self.user_text),z)
                if ans==True:
                    self.state = "Winning"
                else:
                    screen.fill("grey")
                    self.state = "Loss"
            #added allowed_keys just to make it harder for the user to make mistakes by putting letters as an answer
            if event.type == pygame.KEYDOWN and event.key in allowed_keys:
                self.user_text += event.unicode
                



            screen.fill("light blue")
            self.just_text("MAIN GAME",280,200)
            self.just_text(f"{x} x {y} == {user_text}",300,300)


    def button(self,text,top_colour,bot_colour,pos_x,pos_y,but_height,but_width):

        #   top rect
        self.top_rect = pygame.Rect(pos_x,pos_y,but_width,but_height)
        self.top_rect_colour = top_colour

        #   bot rect
        self.bot_rect = pygame.Rect(pos_x,pos_y + 6, but_width,but_height) # pos[1] always +6
        self.bot_rect_colour = bot_colour

        #   text
        self.text_surface = font.render(text,False,"black")
        self.text_rect = self.text_surface.get_rect(center = self.top_rect.center)




        #   draw the rects
        pygame.draw.rect(screen,self.bot_rect_colour,self.bot_rect,border_radius = 12)
        pygame.draw.rect(screen,self.top_rect_colour,self.top_rect,border_radius = 12)
        screen.blit(self.text_surface,self.text_rect)

    def just_text(self,text,pos_x,pos_y):
        #   text
        self.text_surface = font.render(text,False,"black")
        self.text_rect = self.text_surface.get_rect(center =(pos_x,pos_y))
        screen.blit(self.text_surface,self.text_rect)



pygame.init()
clock = pygame.time.Clock()

width, height = 600,600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Multiplication game")

font = pygame.font.Font("font2/Pixeltype.ttf",50)

main = Main()

while True:
    main.state_manager()
    pygame.display.update()
    clock.tick(60)
