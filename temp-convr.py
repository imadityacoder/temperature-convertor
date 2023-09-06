from flet import (
    Page,
    app,
    TextButton,
    Text,
    TextField,
    border,
    colors,
    Container,
    Column,
    Row,
    Padding,
    Margin,
    BoxShadow,
    Dropdown,
    dropdown,
    IconButton,
    FloatingActionButton,
    alignment,
    Alignment,
    MainAxisAlignment,
    CrossAxisAlignment,
    KeyboardType,
    TextAlign,
    NavigationBar
    
)

def main(page:Page):
    page.title="Welcome to Aditya's Temrature-Converter"
    # page.bgcolor=colors.DEEP_PURPLE_400
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.window_height=800
    page.window_width=800
    page.auto_scroll = False
    title=Text(
        value="Aditya's Temprature Converter",
        size=20,

        )
    d1 = Dropdown(
        width=200,
        value="Celcius",
        options=[
            dropdown.Option("Celcius"),
            dropdown.Option("Farenheit"),
            dropdown.Option("Kelvin"),
        ],
        )

    d2 =Dropdown(
        width=200,
        value="Farenheit",
        bgcolor=colors.GREEN_ACCENT_700,
        options=[
            dropdown.Option("Celcius"),
            dropdown.Option("Farenheit"),
            dropdown.Option("Kelvin"),
        ], 
        
        )
    box1=Container(
        content = TextField(
        hint_text="0",
        text_align="center",
        text_size= 20,
        border_radius= 8,
        keyboard_type=KeyboardType.NUMBER
    ),
    padding=10,
    bgcolor=colors.BLUE_ACCENT_400,
    height=100,
    width=200,
    border_radius=10

    )
    box2=Container(
        content = TextField(
        hint_text="0",
        text_align="center",
        text_size= 20,
        keyboard_type=KeyboardType.DATETIME,
        border_radius= 8,
    ),
    padding=10,
    bgcolor=colors.BLUE_ACCENT_400,
    height=100,
    width=200,
    border_radius=10,

    )    
    page.add(
        title,
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
        )
    )
app(target=main)