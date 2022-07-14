from QUESTION import Question


question_prompts = [
    "What colour are apples?\n(a) Red\n(b) Blue\n(c) Green\n(d) Orange\nEnter answer: ",
    "What colour are bananas?\n(a) Purple\n(b) Yellow\n(c) Green\n(d) Orange\nEnter answer: ",
    "What colour are Strawberries?\n(a) Golden\n(b) Blue\n(c) Pink\n(d) Grey\nEnter answer: "
]


questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
]


def run_test(questions):
    score = 0
    for question in questions:
        ans = input(question.prompt)
        if ans == question.ans:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)




















