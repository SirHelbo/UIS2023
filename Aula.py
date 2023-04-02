import PySimpleGUI as sg


loginScreen = [
    [sg.Image("images/login_top.png", pad=(0, 0))],
    [sg.Button(key="login_overblik", image_filename="images/login_button.png", button_color="#18628f", pad=(0, 0), mouseover_colors=("white","#18628f"))],
    [sg.Image("images/login_bottom.png", pad=(0, 0))],
]


loadingScreen = [[sg.Image("images/loading.png", pad = (0,0), size = (500, 890))]]


beskeder = [[sg.Image("images/content/beskeder.png", pad=(0, 0))]]
dokumenter = [[sg.Image("images/content/dokumenter.png", pad=(0, 0))]]
ferie = [[sg.Image("images/content/ferie.png", pad=(0, 0))]]
galleri = [[sg.Image("images/content/galleri.png", pad=(0, 0))]]
kalender = [[sg.Image("images/content/kalender.png", pad=(0, 0))]]
foedselsdag = [[sg.Image("images/content/foedselsdag.png", pad=(0, 0))]]
invitationer = [[sg.Image("images/content/invitationer.png", pad=(0, 0))]]
vigtige = [[sg.Image("images/content/vigtige.png", pad=(0, 0))]]
kommeGaa = [[sg.Image("images/content/kommeGaa.png", pad=(0, 0))]]
henteansvarlige = [[sg.Image("images/content/henteansvarlige.png", pad=(0, 0))]]
tider = [[sg.Image("images/content/tider.png", pad=(0, 0))]]
aabningstider = [[sg.Image("images/content/aabningstider.png", pad=(0, 0))]]
kontakter = [[sg.Image("images/content/kontakter.png", pad=(0, 0))]]
overblik = [[sg.Image("images/content/overblik.png", pad=(0, 0))]]
sygdom = [[sg.Image("images/content/sygdom.png", pad=(0, 0))]]


content =  ["beskeder",
            "dokumenter",
            "ferie",
            "galleri",
            "kalender",
            "foedselsdag",
            "invitationer",
            "vigtige",
            "kommeGaa",
            "henteansvarlige",
            "tider",
            "aabningstider",
            "kontakter",
            "overblik",
            "sygdom"]


navMenu = [ [sg.Image("images/padding.png", pad=(0, 0))],
            *[ [sg.Button(key=f"navm-{menu}", image_filename=f"images/nav_menu/nav_{menu}.png", button_color=("white","#FFFFFF"), pad=(0, 0), mouseover_colors=("white", "white"))] for menu in content ] ]


topMenu = [[sg.Image("images/top_menu.png", visible=False, key="<top_menu>")]]


navBar = [[sg.Button(image_filename=f"images/{filename}_button.png", key=f"navb_{filename}", pad=(0, 0), border_width=0, button_color=("white","#f3f5f5"), mouseover_colors=("white","#f3f5f5"))
    for filename in ["overblik", "beskeder", "kalender", "navMenu"]]]


layout = [[
        topMenu],[
        sg.Column(loginScreen, visible=True, key="-loginScreen-", element_justification="center"),
        *[sg.Column(eval(name), visible=False, key=f"-{name}-", element_justification="center") for name in content + ["navMenu"]]],
        [navBar]]


window = sg.Window("Aula prototype", layout, size=(500, 890), margins=(0, 0), element_padding=(0,0))


currentWindow = "-overblik-"

while True:

    event, values = window.read(timeout=0)

    if event in (None, "Exit"):
        break

    # Leaving the login page is special, it actives the top and bottom menu bar
    if event == "login_overblik":
        window["-loginScreen-"].update(visible=False)
        window["<top_menu>"].update(visible=True)
        window["-overblik-"].update(visible=True) 

    # handle content swap requests
    if event[0:4] == "navb" or event[0:4] == "navm":

        # update header
        if (event[5:] == "navMenu"):
            window["<top_menu>"].update(visible=False)
        else:
            window["<top_menu>"].update(visible=True)


        window[currentWindow].update(visible=False)
        window[f"-{event[5:]}-"].update(visible=True)      
        currentWindow = f"-{event[5:]}-"

window.close()