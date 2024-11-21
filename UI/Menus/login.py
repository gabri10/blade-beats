import sys

from Config.window_config import *
from app import Game

from UI.Text import Text
from UI.TextField import TextField
from UI.Button import Button

from Backend.PlayerDAO import PlayerDAO


class Login:
    def __init__(self, camera):

        self.camera = camera
        self.title_text = Text(msg="Log In!", position=(WIDTH / 2, 100), color=WHITE, font_size=70, centered=True)

        self.start = 0

        self.name_text = Text(msg="Nickname: ", position=(WIDTH / 2, HEIGHT / 2 - 50), color=WHITE, font_size=30,
                              centered=True)
        self.name_input = TextField(x=WIDTH / 2 - 100, y=HEIGHT / 2, w=200, h=50, text='Augusto')

        self.confirm_button = Button(position=(WIDTH / 2, HEIGHT / 2 + 100), size=(200, 50), color=GRAY,
                                     hover_color=WHITE, on_click=self.confirm, text="Fazer login")

        self.error_message = Text(msg="", position=(WIDTH / 2, HEIGHT / 2 + 200), color=RED, font_size=20,
                                  centered=True)
        self.error = False

        self.playerDAO = PlayerDAO()
        self.authed_player = None

    def run(self):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load('audio/main_menu.mp3')
            pygame.mixer.music.play(loops=-1, start=0)
        self.start = pygame.time.get_ticks()

        while self.authed_player is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.confirm_button.rect.collidepoint(event.pos):
                            self.confirm_button.handle_click()
                self.name_input.handle_event(event)

            CLOCK.tick(FPS)
            self.camera.internal_surface.fill(BLACK)

            if pygame.time.get_ticks() - self.start > 900:
                self.title_text.draw(self.camera.internal_surface)
                self.name_text.draw(self.camera.internal_surface)
                self.name_input.draw(self.camera.internal_surface)
                self.confirm_button.draw(self.camera.internal_surface)
                self.error_message.draw(self.camera.internal_surface)

            self.name_input.update()
            Game.blit_screen(self.camera)
            pygame.display.flip()

        return self.authed_player

    def confirm(self):
        if self.name_input.text == '':
            self.error_message.msg = f"O seguinte erro ocorreu: Informe um nickname primeiro"
            self.error = True
        else:
            try:
                self.playerDAO.create_player(self.name_input.text)
            except ValueError:
                print(ValueError)
            try:
                self.authed_player = self.playerDAO.get_player_by_nickname(self.name_input.text)
            except ValueError as e:
                self.error = True
                self.error_message.msg = f"O seguinte erro ocorreu: {e}"
