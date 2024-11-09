#!/usr/bin/env python
# coding: utf-8

# In[18]:


# Define questions and answers
questions = {
    "What is the capital of France?": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
    "Which planet is known as the Red Planet?": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
    "Who wrote 'To Kill a Mockingbird'?": ["A. Harper Lee", "B. J.K. Rowling", "C. Mark Twain", "D. Ernest Hemingway"]
}

answers = {
    "What is the capital of France?": "A",
    "Which planet is known as the Red Planet?": "B",
    "Who wrote 'To Kill a Mockingbird'?": "A"
}

# Function to display questions
def display_question(questions, option):
    print(questions)
    for option in questions[question]:
        print(option)

# Function to get user answer
def get_user_answer():
    answer = input("Enter your answer (A, B, C, D): ").upper()
    while answer not in ["A", "B", "C", "D"]:
        print("Invalid option. Please try again.")
        answer = input("Enter your answer (A, B, C, D): ").upper()
    return answer

# Function to check answer
def check_answer(question, user_answer):
    correct_answer = answers[question]
    return user_answer == correct_answer

# Main quiz function
def quiz():
    score = 0
    for question in questions:
        display_question(question)
        user_answer = get_user_answer()
        if check_answer(question, user_answer):
            print("Correct!\n")
            score += 1
        else:
            print("Wrong answer.\n")
    
    total_questions = len(questions)
    pass_mark = total_questions // 2
    if score >= pass_mark:
        print(f"Congratulations! You passed with a score of {score}/{total_questions}.")
    else:
        print(f"Sorry, you failed with a score of {score}/{total_questions}.")


# In[5]:





# In[17]:





# In[ ]:




