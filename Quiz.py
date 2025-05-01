# Simple Quiz Game using dictionaries

# List of questions stored as dictionaries
quiz_questions = [
    {
        "question": "What is the capital of Nepal?",
        "options": ["A. Kathmandu", "B. Pokhara", "C. Lalitpur", "D. Bhaktapur"],
        "answer": "A"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["A. Python", "B. Java", "C. JavaScript", "D. C++"],
        "answer": "C"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Process Unit", "B. Central Processing Unit", "C. Computer Processing Unit", "D. Central Programming Unit"],
        "answer": "B"
    },
    {
        "question": "HTML is used to?",
        "options": ["A. Style web pages", "B. Structure content", "C. Program apps", "D. Connect to server"],
        "answer": "B"
    }
]

# Score counter
score = 0

# Quiz loop
for i, q in enumerate(quiz_questions):
    print(f"\nQ{i+1}: {q['question']}")
    for option in q['options']:
        print(option)
    user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()
    
    if user_answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer: {q['answer']}")

# Final Score & Feedback
print(f"\nYour final score is {score} out of {len(quiz_questions)}.")

if score == len(quiz_questions):
    print("🎉 Excellent! You're a quiz master!")
elif score >= len(quiz_questions) // 2:
    print("👍 Good job! Keep practicing.")
else:
    print("📘 Keep learning! You'll get better with time.")
