from tkinter import*
import json
window=Tk()
window.title("Добавление продуктов")
window.geometry("500x850")
products=[]
def load_data():
    global products
    try:
        with open('products.json',"r",encoding='utf-8') as file:
            products=json.load(file)
            update_lb()
    except FileNotFoundError:
        products=[]
def save():
    try:
        with open('product.json',"w",encoding='utf-8') as file:
            json.dump(products,file,ensure_ascii=False,indent=2)
    except FileNotFoundError:
        return
def add_item():
    name=name_entry.get()
    count=count_entry.get()
    price=price_entry.get()
    if name and count and price:
        summa=int(count)*int(price)
        item=f'{name}|{count}|{price}|Итого:{summa} руб.'
        name_entry.delete(0,END)
        count_entry.delete(0,END)
        price_entry.delete(0,END)
        products.append(item)
        update_lb()
        save()
def delete_item():
    selected_index=lb.curselection()
    if selected_index:
        index=selected_index[0]
        # Чтобы правильно удалить при включенном фильтре:
        item_text=lb.get(index)
        products.remove(item_text)
        update_lb()
        save()
def update_lb():
    lb.delete(0,END)
    for item in products:
        lb.insert(END,item)
def applyVH_filter():
    limit=filter_entry.get()
    if not limit:
        update_lb
        return
    lb.delete(0,END)
    for item in products:
        try:
            parts=item.split("|")
            item_price=int(parts[2])
            if item_price>=int(limit):
                lb.insert(END,item)
        except:
            continue
def apply_filter():
    limit=filter_entry.get()
    if not limit:
        update_lb
        return
    lb.delete(0,END)
    for item in products:
        try:
            parts=item.split("|")
            item_price=int(parts[2])
            if item_price<=int(limit):
                lb.insert(END,item)
        except:
            continue
        
Label(text="Добавление продуктов", font="Arial 20").pack(pady=5)
Label(text="Название", font="Arial 20").pack(pady=5)
name_entry=Entry(font="Arial 20")
name_entry.pack(pady=2)

Label(text="Количество", font="Arial 20").pack(pady=5)
count_entry=Entry(font="Arial 20")
count_entry.pack(pady=2)

Label(text="Цена", font="Arial 20").pack(pady=5)
price_entry=Entry(font="Arial 20")
price_entry.pack(pady=2)
Button(text="Добавить",font="Arial 18", bg="lightgreen", fg="white", command=add_item).pack(pady=2)
Button(text="Удалить выбранное",font="Arial 18", bg="red", fg="white", command=delete_item).pack(pady=2)

# ===========Фильтр:Интерфейс===
Label(text="Фильтр(по цене)",font="Arial 15", fg="blue").pack(pady=10)
filter_entry=Entry(font="Aria 18", bg="#f0f0f0")
filter_entry.pack(pady=2)
Button(text="ВЫШЕ", font="Arial 15", command=applyVH_filter).pack(pady=5)
Button(text="НИЖЕ", font="Arial 15", command=apply_filter).pack(pady=5)
Button(text="ВСЕ ЗАПИСИ", font="Arial 15", command=update_lb).pack(pady=5)

lb=Listbox(font="Arial 18", width=100)
lb.pack()
load_data()
window.mainloop()


