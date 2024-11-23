import tkinter
import random
pered = ["У найближчому майбутньому наукові досягнення дозволять \nлюдям жити більше і здоровіше з новим медичним.",
"Відбудеться значне зростання популярності зелених технологій, \nщо зменшить вплив людства на навколишнє середовище.",
"Сфера штучного інтелекту продовжувати розвиватися, і багато \nпрофесій будуть автоматизовані, змінюючи",
"Люди будуть більше цікаві у подорожах до віддалених куточків\n планети, коли дозволять технічні інновації",
"Глобальні кліматичні зміни призведуть до нового поштовху до \nрозвитку відновлювальних джерел енергії та технологій для боротьби з...",
"Система освіти змінюється за рахунок інновацій у навчанні \nта новим підходам до онлайн-осві",
"У світі буде більше уваги приділяти психічному здоров'ю, \nщо допоможе зменшити соціальне",
"Міжнародна політика стане більш динамічною, з новими економічними\n та соціальними альянсами.",
"Люди знайдуть нові способи збереження приватності в цифровому\n світі, адже безпека даних стане пріоритетом.",
"У галузі розваг будуть з'являтися нові формати медіа, зокрема \nвіртуальні світи, що повністю змінюють сприйняття реального",]

def go():
    p = random.choice(pered)
    text.config(text = p)

window = tkinter.Tk()
window.title ("Нострадамус - передбачення для Вас! / Поліна Горбатенко")
window.geometry("600x250+100+100")

text = tkinter.Label(text = "натисни на кнопку для отримання передбачення на сьогодні", font = ("Tahoma",16))
text.place(x = 10, y = 20)

button = tkinter.Button(text = "Натисни", font = ("Tahoma", 16), command = go)
button.place(x = 240, y = 100)
window.mainloop()
