from flet import (
    Page,
    app,
    Text,
    TextField,
    colors,
    Row,
    Dropdown,
    dropdown,
    IconButton,
    KeyboardType,
    ThemeMode,
    icons,
    AppBar,
    Icon,
    Banner,

)
from time import sleep

def main(page:Page):
    page.title="Welcome to Aditya's Temrature-Converter"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

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
        leading=Icon(icons.CALCULATE_ROUNDED),
        leading_width=35,
        title=Text("Aditya's Temprature Converter"),
        center_title=False,
        bgcolor=colors.OUTLINE_VARIANT,
        actions=[
            IconButton(icons.LIGHT_MODE_OUTLINED,on_click=lambda e:theme(e),tooltip="Theme Mode"),
            IconButton(icons.WEB_OUTLINED,on_click= lambda e:profile(e)),
            IconButton(
                icon=icons.MENU_SHARP,
                on_click=lambda e:profile(e),
                )
        ],
    )

    boxh = 200
    boxw = 260
    fsize = 40

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
            bgcolor=colors.BLUE_500,
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
        tooltip="ENTER HERE",
        autofocus= True,
        on_change=lambda e:mainfunc(e),
        bgcolor=colors.GREEN_600,
        height=boxh,
        width=boxw,
        opacity=0.9,
        max_length=8,
        )
    
    page.update()    

    box2= TextField(
        text_align="center",
        text_size= fsize,
        max_length=12,
        border_radius= 8,
        bgcolor=colors.BLUE_ACCENT_400,
        height=boxh,
        width=boxw,
        opacity=0.9,
        read_only=True
    )

    def mainfunc(e):
        inp1=box1.value

        try:
            if d1.value ==  d2.value:
                box2.value=inp1
                page.update()

            elif box1.value == "":
                box2.value=""
                page.update()    
    
            elif d1.value =="Celcius" and d2.value == "Farenheit":
                box2.value=str((float(inp1)*9/5)+32)
                page.update()

            elif d1.value =="Celcius" and d2.value == "Kelvin":
                box2.value=str(float(inp1)+273.15)
                page.update()

            elif d1.value =="Farenheit" and d2.value == "Kelvin":
                box2.value=str((float(inp1)-32)*5/9+273.15)
                page.update()

            elif d1.value =="Farenheit" and d2.value == "Celcius":
                box2.value=str((float(inp1)-32)*5/9)
                page.update()

            elif d1.value =="Kelvin" and d2.value == "Celcius":
                box2.value=str(float(inp1)-273.15)
                page.update()
                
            elif d1.value =="Kelvin" and d2.value == "Farenheit":
                box2.value=str((float(inp1)-273.15)*9/5+32)
                page.update()
        except Exception as e:
            print("error",e)


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

if __name__=="__main__":
    app(target=main)