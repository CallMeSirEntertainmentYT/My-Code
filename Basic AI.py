import random
import datetime
import time

def calculate():
    calculation = input("Please enter the calculation: ")
    try:
        result = eval(calculation)
        print(f"The result is {result}")
    except:
        print("I'm sorry, I couldn't perform the calculation.")

def game():
    number = random.randint(1, 10)
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == number:
        print("Congratulations! You guessed correctly.")
    else:
        print(f"Sorry, the correct number was {number}.")

def tell_joke():
    jokes = ["Why don't scientists trust atoms? Because they make up everything!",
             "Why did the scarecrow win an award? Because he was outstanding in his field!",
             "Why don't some fish play piano? Because you can't tuna fish!",
             "Why did the bicycle fall over? Because it was two-tired!",
             "Why do we tell actors to 'break a leg'? Because every play has a cast!",
             "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
             "Why don't skeletons fight each other? They don't have the guts!",
             "What do you call fake spaghetti? An impasta!",
             "Why couldn't the leopard play hide and seek? Because he was always spotted!",
             "What do you call a snowman with a six-pack? An abdominal snowman!",
             "What did the fish say to the sushi? Wassah b!"]
    print(random.choice(jokes))

def trivia_game():
    questions = {"What is the capital of France?": "Paris",
                 "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
                 "What is the square root of 16?": "4",
                 "Who painted the Mona Lisa?": "Leonardo da Vinci",
                 "What is the chemical symbol for Hydrogen?": "H"}
    question = random.choice(list(questions.keys()))
    answer = input(question + " ")
    if answer.lower() == questions[question].lower():
        print("Correct!")
    else:
        print(f"Sorry, the correct answer was {questions[question]}.")

def tell_time():
    now = datetime.datetime.now()
    print(f"The current date and time is {now.strftime('%Y-%m-%d %H:%M:%S')} (UTC)")

power_level = 100
first_time = True
while True:
    if first_time:
        print("Hello! How can I assist you today? (Type 'exit' to quit)")
        first_time = False
    else:
        print("What else can I assist you with today? (Type 'exit' to quit)")
    user_input = input().lower()

    if user_input == 'exit':
        break
    elif "calculate" in user_input:
        calculate()
    elif "joke" in user_input:
        tell_joke()
    elif "quote" in user_input:
        print("Here's a quote for you: 'The only way to do great work is to love what you do.' - Steve Jobs")
    elif "game" in user_input:
        game()
    elif "time" in user_input:
        tell_time()
    elif "trivia" in user_input:
        trivia_game()
    else:
        power_level -= random.randint(1, 10)
        if power_level > 0:
            print("I'm sorry, but I can't do that. Remember that I am only a simple AI. Maybe try rephrasing?")
        if power_level <= 0:
            print("I'm running low on power. Please wait while I recharge. Estimated time: 30 seconds.")
            time.sleep(30)
            power_level = 100
        else:
            print(f"Current power level: {power_level}%")
