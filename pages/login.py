import flet as ft 
from flet_route import Params, Basket
from utils.style import *


# класс для входа в приложение
class LoginPage:

    email_input = ft.Container(
            content=ft.TextField(label='Укажите Email',
                                   bgcolor=secondaryBgColor,
                                   border=ft.InputBorder.NONE,
                                   filled=True,
                                   color=secondaryFontColor),
            border_radius=15
    )
    
    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = 'Страница авторизации'
        page.window.width = defaultWidthWindow
        page.window.height = defaultHeightWindow
        page.window.min_width = 800
        page.window.min_height = 400

        return ft.View(
        "/",
        controls=[
            self.email_input                
            ]
        )
