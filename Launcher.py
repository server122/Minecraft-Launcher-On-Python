import flet as ft
from minecraft_launcher_lib.utils import get_minecraft_directory
from minecraft_launcher_lib.install import install_minecraft_version
from minecraft_launcher_lib.command import get_minecraft_command
from minecraft_launcher_lib.utils import get_version_list
import minecraft_launcher_lib
# Эти импорты не обязательны, вместо generate_username()[0] и str(uuid1()) можно оставить просто ''
from random_username.generate import generate_username
from uuid import uuid1

from subprocess import call
from sys import argv, exit

import flet as ft

version_id = get_version_list
nickname = ""
minecraft_directory = get_minecraft_directory().replace('minecraft', 'mjnlauncher')




def main(page: ft.Page):
    def Button_clicked(e): 
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()
        version_id = versionid.value  
        username = Nickname.value
        minecraft_directory = get_minecraft_directory().replace('minecraft', 'mjnlauncher')
        install_minecraft_version(versionid=version_id, minecraft_directory=minecraft_directory)
        options = {'username': username, 'uuid': str(uuid1()), 'token': ''}
        call(minecraft_launcher_lib.command.get_minecraft_command(version=version_id, minecraft_directory=minecraft_directory, options=options))
        
    
    def close_dlg(e):
        dlg_modal.open = False
        page.update()

    dlg_modal = ft.AlertDialog(
    modal=True,
    title=ft.Text("Wait"),
    content=ft.Text("Minecraft is installing / Starting, Please wait"),
    actions=[
        ft.TextButton("OK", on_click=close_dlg),
    ],
    actions_alignment=ft.MainAxisAlignment.END,
    on_dismiss=lambda e: print("Modal dialog dismissed!"),
)



    page.title = "SLauncher"
    Nickname = ft.TextField(label="NickName")

    versionid = ft.Dropdown(
        options=[ft.dropdown.Option(version['id']) for version in get_version_list()],
        
        width=200,
)
    Buttons = ft.FilledButton(text="Launch the game", on_click=Button_clicked)

    page.add(Nickname, versionid, Buttons)

    
ft.app(target=main)