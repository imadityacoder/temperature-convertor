from flet import (
    Page,
    app,
    Text,
    TextField,
    colors,
    Dropdown,
    dropdown,
    IconButton,
    KeyboardType,
    ThemeMode,
    icons,
    AppBar,
    Icon,
    Banner,
    ResponsiveRow,
    Padding,

)
from time import sleep


def main(page:Page):
    page.vertical_alignment = "top"
    page.horizontal_alignment = "center"
    page.window_height = 720
    page.window_width = 420
    page.theme_mode=ThemeMode.DARK
    page.padding = Padding(top=30,bottom=6,right=6,left=6)


    def openbn():
        page.banner.open=True
        page.update()

    page.banner=Banner(  
        bgcolor=colors.AMBER_100,
        leading=Icon(icons.WARNING_AMBER_ROUNDED, color=colors.AMBER, size=40),
        content=Text("This is now in updating!!!",color=colors.BLACK54),
        actions=[IconButton(icons.LABEL_IMPORTANT_ROUNDED)]
        )

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
        openbn()
        sleep(5)
        page.banner.open=False
        page.update()

    page.appbar=AppBar(
        leading=Icon(icons.DEVICE_THERMOSTAT_SHARP),
        leading_width=40,
        title=Text("Aditya's Temprature Converter",size=16),
        center_title=False,
        bgcolor=colors.OUTLINE_VARIANT,
        actions=[
            IconButton(
                icons.LIGHT_MODE_OUTLINED,
                on_click=lambda e:theme(e),
                tooltip="Theme Mode"
                ),
            IconButton(
                icons.SETTINGS_SHARP,
                on_click= lambda e:profile(e)
                ),
        ],
    )

    boxw = 260
    fsize = 26

    d1 = Dropdown(
            width=boxw,
            value="Celcius",
            options=[
                dropdown.Option("Celcius"),
                dropdown.Option("Farenheit"),
                dropdown.Option("Kelvin"),
            ],
        )
    
    
    d2=Dropdown(
            width=boxw,
            value="Farenheit",
            options=[
                dropdown.Option("Celcius"),
                dropdown.Option("Farenheit"),
                dropdown.Option("Kelvin"),
            ], 
            
            )
    
    box1= TextField(
        text_align="center",
        text_size= fsize,
        border_radius= 10,
        autofocus= True,
        on_change=lambda e:mainfunc(e),
        bgcolor=colors.GREEN_600,
        width=boxw,
        keyboard_type=KeyboardType.NUMBER,
        max_length=12,
        
        )

    box2= TextField(
        text_align="center",
        text_size= fsize,
        border_radius= 8,
        bgcolor=colors.BLUE_ACCENT_400,
        width=boxw,
        read_only=True,
        adaptive=True,
        max_length=18,
        
    )

    def mainfunc(e):
        inp1=box1.value

        try:
            if d1.value ==  d2.value:
                box2.value=int(inp1)
                page.update()

            elif box1.value == "":
                box2.value= ""
                page.update()
    
            elif d1.value =="Celcius" and d2.value == "Farenheit":
                
                box2.value=str((float(inp1)*9/5)+32)
                page.update()

            elif d1.value =="Celcius" and d2.value == "Kelvin":
                box2.value=str(float(inp1)+273.15)
                page.update()

            elif d1.value =="Farenheit" and d2.value == "Kelvin":
                box2.value=str(((float(inp1)-32)*5/9+273.15)//1)
                page.update()

            elif d1.value =="Farenheit" and d2.value == "Celcius":
                box2.value=str(((float(inp1)-32)*5/9)//1)
                page.update()

            elif d1.value =="Kelvin" and d2.value == "Celcius":
                box2.value=str(float(inp1)-273.15)
                page.update()
                
            elif d1.value =="Kelvin" and d2.value == "Farenheit":
                box2.value=str(((float(inp1)-273.15)*9/5+32)//1)
                page.update()

        except Exception:
            pass


    page.add(
        
        ResponsiveRow(
            controls=[
                d1,
                box1,
            ],
        ),
        ResponsiveRow(
            controls=[
                d2,
                box2,
            ],
           
        ),

    )
    page.update()

app(target=main)
