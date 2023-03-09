from tkinter import Tk, ttk
from tkinter import *
from PIL import Image, ImageTk
import requests
import json

# colors

color1 = "white"
color2 = "black"
color0 = "red"
color3 = "sky-blue"
color4 = "orange"
color5 = "blue"

Window = Tk()
Window.geometry("350x350")
Window.title("FIAT CONVERTER")
Window.configure(bg=color1)
Window.resizable(height=FALSE, width=FALSE)

# Frames
top = Frame(Window, width=350, height=60, bg=color0)
top.grid(row=0, column=0)

main = Frame(Window, width=350, height=310, bg=color5)
main.grid(row=1, column=0)


def converting():
    global symbol
    url = "https://api.apilayer.com/currency_data/convert"

    currency2 = combo1.get()
    currency1 = combo2.get()
    amt = fiat_entry.get()
    querystring = {'to': currency1, "from": currency2, "amount": amt}

    if currency1 == 'USD':
        symbol = '$'
    elif currency1 == 'NGN':
        symbol = '₦'
    elif currency1 == 'EUR':
        symbol = '€'
    elif currency1 == 'CAD':
        symbol = 'CA $'
    elif currency1 == 'KWD':
        symbol = 'KD'

    payload = {}
    headers = {
        "apikey": "K6muiYcl3dbleYYlHgwgKrfDdrpxL4KX"
    }

    response = requests.request("GET", url, headers=headers, data=payload, params=querystring)

    status_code = response.status_code
    convert = response.text
    data = json.loads(convert)
    Converted = (data["result"])
    formatted = symbol + " {:,.2f}".format(Converted)

    result['text'] = formatted
    print(Converted, formatted)


# top  frame
icon = Image.open('images/2845677.png')
icon = icon.resize((40, 40))
icon = ImageTk.PhotoImage(icon)
app_name = Label(top, image=icon, compound=LEFT, text="FIAT CONVERTER", height=5, padx=35, pady=30, anchor=CENTER,
                 font=('Cooper black', 15, 'bold'), bg=color0, fg=color1)
app_name.place(x=0, y=0)

currency = ['CAD', 'USD', 'NGN', 'EUR', 'KWD']

# mainframe
result = Label(main, text=" ", width=16, height=2, pady=7, relief="flat", anchor=NW, font=('Ivy', 15, 'bold'),
               bg=color1, fg=color2)
result.place(x=65, y=20)

From = Label(main, text="From", width=8, height=1, pady=0, padx=0, relief="solid", anchor=CENTER,
             font=('Ivy', 10, 'bold'), bg=color1, fg=color2)
From.place(x=48, y=100)
combo1 = ttk.Combobox(main, width=8, justify=CENTER, font=('Ivy', 12, 'bold'))
combo1['values'] = currency
combo1.place(x=47, y=130)

To = Label(main, text="To", width=8, height=1, pady=0, padx=0, relief="solid", anchor=CENTER, font=('Ivy', 10, 'bold'),
           bg=color1, fg=color2)
To.place(x=200, y=99)
combo2 = ttk.Combobox(main, width=8, justify=CENTER, font=('Ivy', 12, 'bold'))
combo2['values'] = currency
combo2.place(x=200, y=130)

fiat_entry = Entry(main, width=27, justify='center', font='Ivy 12 bold', relief='solid')
fiat_entry.place(x=50, y=175)

fiat_converter = Button(main, text='CONVERT', width=19, height=1, padx=5, bg=color1, fg=color2,
                        font=('Cooper black', 12, 'bold'), command=converting)
fiat_converter.place(x=50, y=220)

Window.mainloop()
