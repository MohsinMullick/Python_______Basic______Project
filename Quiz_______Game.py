import random# this line just user interesting because some people memorize question and answer
import time
import threading
# Create list variable and then create dict for each question
questions = [
    {
        "question": "Who invented Python programming language?",
        "options": ["a) Guido van Rossum", "b) James Gosling", "c) Dennis Ritchie", "d) Bjarne Stroustrup"],
        "answer": "a",
        "full": "a) Guido van Rossum"
    },
    {
        "question": "Who co-founded Google?",
        "options": ["a) Bill Gates", "b) Larry Page and Sergey Brin", "c) Mark Zuckerberg", "d) Jeff Bezos"],
        "answer": "b",
        "full": "b) Larry Page and Sergey Brin"
    },
    {
        "question": "Who founded Meta (formerly Facebook)?",
        "options": ["a) Jack Dorsey", "b) Mark Zuckerberg", "c) Elon Musk", "d) Sundar Pichai"],
        "answer": "b",
        "full": "b) Mark Zuckerberg"
    },
    {
        "question": "Who co-created Instagram?",
        "options": ["a) Kevin Systrom and Mike Krieger", "b) Evan Spiegel", "c) Pavel Durov", "d) Brian Acton"],
        "answer": "a",
        "full": "a) Kevin Systrom and Mike Krieger"
    },
    {
        "question": "Who were the original founders of Twitter (now X)?",
        "options": ["a) Elon Musk", "b) Jack Dorsey, Biz Stone, Evan Williams, Noah Glass", "c) Mark Zuckerberg",
                    "d) Larry Page"],
        "answer": "b",
        "full": "b) Jack Dorsey, Biz Stone, Evan Williams, Noah Glass"
    },
    {
        "question": "Who founded xAI and created Grok?",
        "options": ["a) OpenAI", "b) Elon Musk", "c) Google", "d) Anthropic"],
        "answer": "b",
        "full": "b) Elon Musk"
    },
    {
        "question": "DeepSeek AI was founded by whom?",
        "options": ["a) Liang Wenfeng", "b) Sam Altman", "c) Elon Musk", "d) Satya Nadella"],
        "answer": "a",
        "full": "a) Liang Wenfeng"
    },
    {
        "question": "Who developed ChatGPT?",
        "options": ["a) Google", "b) OpenAI", "c) xAI", "d) Microsoft"],
        "answer": "b",
        "full": "b) OpenAI"
    },
    {
        "question": "Who co-founded GitHub?",
        "options": ["a) Chris Wanstrath, PJ Hyett, and Tom Preston-Werner", "b) Linus Torvalds", "c) Elon Musk",
                    "d) Bill Gates"],
        "answer": "a",
        "full": "a) Chris Wanstrath, PJ Hyett, and Tom Preston-Werner"
    },
    {
        "question": "Who co-founded YouTube?",
        "options": ["a) Steve Chen, Chad Hurley, and Jawed Karim", "b) Mark Zuckerberg", "c) Larry Page",
                    "d) Reed Hastings"],
        "answer": "a",
        "full": "a) Steve Chen, Chad Hurley, and Jawed Karim"
    },
    {
        "question": "Who founded Amazon?",
        "options": ["a) Jeff Bezos", "b) Bill Gates", "c) Elon Musk", "d) Tim Berners-Lee"],
        "answer": "a",
        "full": "a) Jeff Bezos"
    },
    {
        "question": "Who invented the World Wide Web?",
        "options": ["a) Tim Berners-Lee", "b) Alan Turing", "c) Vint Cerf", "d) Bill Gates"],
        "answer": "a",
        "full": "a) Tim Berners-Lee"
    },
    {
        "question": "Who is the current CEO of Apple?",
        "options": ["a) Steve Jobs", "b) Tim Cook", "c) Satya Nadella", "d) Sundar Pichai"],
        "answer": "b",
        "full": "b) Tim Cook"
    },
    {
        "question": "Who co-founded Microsoft?",
        "options": ["a) Bill Gates and Paul Allen", "b) Steve Ballmer", "c) Larry Ellison", "d) Mark Zuckerberg"],
        "answer": "a",
        "full": "a) Bill Gates and Paul Allen"
    },
    {
        "question": "Who created the Linux kernel?",
        "options": ["a) Richard Stallman", "b) Linus Torvalds", "c) Guido van Rossum", "d) Dennis Ritchie"],
        "answer": "b",
        "full": "b) Linus Torvalds"
    },
    {
        "question": "Who invented Java programming language?",
        "options": ["a) James Gosling", "b) Bjarne Stroustrup", "c) Anders Hejlsberg", "d) Brendan Eich"],
        "answer": "a",
        "full": "a) James Gosling"
    },
    {
        "question": "Who created JavaScript?",
        "options": ["a) Brendan Eich", "b) Tim Berners-Lee", "c) Yukihiro Matsumoto", "d) Rasmus Lerdorf"],
        "answer": "a",
        "full": "a) Brendan Eich"
    },
    {
        "question": "Who founded Tesla (originally)?",
        "options": ["a) Elon Musk", "b) Martin Eberhard and Marc Tarpenning", "c) Both a and b", "d) JB Straubel"],
        "answer": "c",
        "full": "c) Both a and b"
    },
    {
        "question": "Who invented the C programming language?",
        "options": ["a) Ken Thompson", "b) Dennis Ritchie", "c) Brian Kernighan", "d) Both b and c"],
        "answer": "d",
        "full": "d) Both b and c"
    },
    {
        "question": "Who founded SpaceX?",
        "options": ["a) Gwynne Shotwell", "b) Elon Musk", "c) Tom Mueller", "d) Jeff Bezos"],
        "answer": "b",
        "full": "b) Elon Musk"
    },
]
random.shuffle(questions)# choice the random question from questions variable

print("Welcome to Ultimate Tech Founders Quiz!!")
player_name = input("First, Enter your name: ").strip().capitalize()
if not player_name:
    player_name = "Player"

print(f"\nHello, {player_name}! There are {len(questions)} questions.")
print("You will have 20 seconds for each question. Answer with a, b, c, or d.\n")

score = 0
total_answer = 0
time_limit = 20


def input_with_timeout(prompt, timeout):
    user_answer = [None]

    def get_input():
        try:
            user_answer[0] = input(prompt).strip().lower()
        except:
            pass

    thread = threading.Thread(target=get_input)
    thread.daemon = True
    thread.start()
    thread.join(timeout)

    return user_answer[0]


for i, q in enumerate(questions, 1):
    print(f"Question {i}: {q['question']}")
    for opt in q["options"]:
        print("  " + opt)

    print(f"\n⏰ You have {time_limit} seconds!")

    user_answer = input_with_timeout("\nYour answer (a/b/c/d): ", time_limit)

    total_answer += 1# total answer count until you don't get wrong answer

    if user_answer is None:
        print("⏰ Time's up!")
        print(f"The correct answer was: {q['full']}")
        print(f"\nThank you, {player_name}! ")
        print("Please try again next time. ")
        print(f"Your final score: {score} out of {total_answer}")
        break

    elif user_answer not in ['a', 'b', 'c', 'd']:
        print("Invalid input! Only a, b, c, or d allowed.")
        print(f"The correct answer was: {q['full']}")
        print(f"\nThank you, {player_name}! ")
        print("Please try again next time. ")
        print(f"Your final score: {score} out of {total_answer}")
        break

    elif user_answer == q["answer"]:#correct answer
        print("Correct!\n")
        score += 1

        if i < len(questions):
            while True:
                ready = input("Are you ready for the next question? (yes/no): ").strip().lower()
                if ready == 'yes':
                    print("\n" + "-" * 50 + "\n")
                    break
                elif ready == "no":
                    print(f"\nThank you for playing, {player_name}! Your score: {score} out of {total_answer}")
                    exit()
                else:
                    print("Please type 'yes' or 'no'.")

    else:
        print(f"Wrong! The correct answer was: {q['full']}")
        print(f"\nThank you, {player_name}! ")
        print("Please try again next time. ")
        print(f"Your final score: {score} out of {total_answer}")
        break

else:
    print(f"\nCongratulations, {player_name}! You completed the quiz under time pressure!")
    print(f"Your final score: {score} out of {total_answer}")