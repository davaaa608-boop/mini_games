import random
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 1. Санасан тоог таах тоглоомын төлөв
secret_number = random.randint(1, 100)
attempts = 0

@app.route('/')
def index():
    return render_template('index.html')

# 1. Санасан тоог таах
@app.route('/guess_number', methods=['GET', 'POST'])
def guess_number():
    global secret_number, attempts
    message = ""
    if request.method == 'POST':
        try:
            guess = int(request.form['guess'])
            attempts += 1
            if guess < secret_number:
                message = "📉 Хэт бага байна! Илүү өндөр тоо оруулна уу."
            elif guess > secret_number:
                message = "📈 Хэт өндөр байна! Илүү бага тоо оруулна уу."
            else:
                message = f"🎉 Баяр хүргэе! Та {attempts} оролдлогоор зөв таалаа!"
                secret_number = random.randint(1, 100)
                attempts = 0
        except ValueError:
            message = "⚠️ Зөвхөн бүхэл тоо оруулна уу!"
    return render_template('guess_number.html', message=message)

# 2. Хайч, Чулуу, Даавуу
@app.route('/rps', methods=['GET', 'POST'])
def rps():
    result = ""
    user_choice = ""
    computer_choice = ""
    if request.method == 'POST':
        user_choice = request.form['choice']
        choices = ['чулуу', 'хайч', 'даавуу']
        computer_choice = random.choice(choices)
        
        if user_choice == computer_choice:
            result = "🤝 Тэнцлээ!"
        elif (user_choice == 'чулуу' and computer_choice == 'хайч') or \
             (user_choice == 'хайч' and computer_choice == 'даавуу') or \
             (user_choice == 'даавуу' and computer_choice == 'чулуу'):
            result = "🏆 Та яллаа!"
        else:
            result = "💻 Компьютер яллаа!"
            
    return render_template('rps.html', result=result, user_choice=user_choice, computer_choice=computer_choice)

# 3. Зураг таах (Эможи санах/таах бяцхан тоглоом)
@app.route('/memory')
def memory():
    return render_template('memory.html')

# 4. Фибоначчигийн таавар
@app.route('/fibonacci', methods=['GET', 'POST'])
def fibonacci():
    message = ""
    if request.method == 'POST':
        try:
            user_ans = int(request.form['answer'])
            if user_ans == 21:
                message = "🎉 Зөв! Фибоначчийн дараалал өмнөх хоёр тооны нийлбэрээр үргэлжилдэг (8 + 13 = 21)."
            else:
                message = "❌ Буруу байна. Дахин оролдоод үз дээ! (Өмнөх тоонууд: 1, 1, 2, 3, 5, 8, 13)"
        except ValueError:
            message = "⚠️ Тоо оруулна уу!"
    return render_template('fibonacci.html', message=message)

# 5. Төөрдөг байшин (HTML5 Canvas дээр ажиллах мини тоглоом)
@app.route('/maze')
def maze():
    return render_template('maze.html')

if __name__ == '__main__':
    app.run(debug=True)