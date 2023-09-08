from flet import (
    Page,
    app,
    TextButton,
    Text,
    TextField,
    colors,
    Container,
    Column,
    Row,
    Margin,
    BoxShadow,
    Dropdown,
    dropdown,
    IconButton,
    alignment,
    KeyboardType,
    TextAlign,
    ThemeMode,
    icons,
    AppBar,
    Icon,
    PopupMenuButton,
    PopupMenuItem,
)

def main(page:Page):
    page.title="Welcome to Aditya's Temrature-Converter"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.theme_mode = ThemeMode.DARK
    page.auto_scroll = False

    def theme(e):
        if page.theme_mode == ThemeMode.DARK:
            page.theme_mode=ThemeMode.LIGHT
            page.bgcolor= colors.LIGHT_GREEN_100
            page.update()
        else:
            page.theme_mode=ThemeMode.DARK   
            page.bgcolor=colors.BACKGROUND
            page.update()
            
    def profile(e):
        pass

    page.appbar=AppBar(
        leading=Icon(icons.CALCULATE_ROUNDED),
        leading_width=35,
        title=Text("Aditya's Temprature Converter"),
        center_title=False,
        bgcolor=colors.OUTLINE_VARIANT,
        actions=[
            IconButton(icons.LIGHT_MODE_OUTLINED,on_click=lambda e:theme(e)),
            IconButton(icons.WEB_OUTLINED),
            IconButton(
                icon=icons.MENU_SHARP,
                on_click=lambda e:profile(e),
                )
        ],
    )
    boxh = 120
    boxw = 260
    fsize = 40
    d1 = Container(
        content=Dropdown(
            width=boxw,
            value="Celcius",
            options=[
                dropdown.Option("Celcius"),
                dropdown.Option("Farenheit"),
                dropdown.Option("Kelvin"),
            ],
        ),
        
        )
    d2=Container(
        content=Dropdown(
            width=boxw,
            value="Farenheit",
            bgcolor=colors.BLUE_500,
            options=[
                dropdown.Option("Celcius"),
                dropdown.Option("Farenheit"),
                dropdown.Option("Kelvin"),
            ], 
            
            ))
    box1=Container(
        content = TextField(
        hint_text="0",
        text_align="center",
        text_size= fsize,
        border_radius= 10,
        keyboard_type=KeyboardType.NUMBER,
        tooltip="ENTER HERE",
        autofocus= True,
    ),
    bgcolor=colors.GREEN,
    height=boxh,
    width=boxw,
    border_radius=10,
    opacity=0.9,
    margin=Margin(top=5,bottom=0,left=4,right=4),
    shadow=BoxShadow(spread_radius=2,blur_radius=2,color=colors.BLUE_50,)

    )
    box2=Container(
        content = TextField(
        hint_text="12",
        text_align="center",
        text_size= fsize,
        keyboard_type=KeyboardType.NUMBER,
        border_radius= 8,
        read_only=True
    ),
    bgcolor=colors.BLUE_ACCENT_400,
    height=boxh,
    width=boxw,
    border_radius=10,
    opacity=0.9,
    margin=Margin(top=5,bottom=0,left=4,right=4),
    shadow=BoxShadow(spread_radius=2,blur_radius=2,color=colors.GREEN_50,)
    
    )  
    page.add(
        Row(
            [
                d1,
                d2
            ],
            alignment="center",
        ),
        Row(
            [
                box1,
                box2
            ],
            alignment="center",
        ),
    )
app(target=main)