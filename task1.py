import random

class QuizGame:
    def _init_(self, questions, difficulty_levels):
        self.questions = questions
        self.difficulty_levels = difficulty_levels
        self.score = 0

    def display_question(self, question, options):
        print(question)
        random.shuffle(options)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        user_input = input("Enter the number of your answer: ")
        return int(user_input) - 1

    def play_quiz(self):
        for question, options in self.questions:
            print("\n" + "-" * 50)
            user_answer = self.display_question(question, options)
            correct_answer = options.index(max(options))
            if user_answer == correct_answer:
                print("Correct! Good job!")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was: {options[correct_answer]}")

        print("\n" + "-" * 50)
        print(f"Quiz completed! Your final score is: {self.score}/{len(self.questions)}")

if _name_ == "_main_":
    # Define your questions and answers
    questions_and_answers = [
        ("What is the capital of France?", ["Paris", "Berlin", "Madrid"]),
        ("Which planet is known as the Red Planet?", ["Venus", "Mars", "Jupiter"]),
        ("What is the largest mammal in the world?", ["Elephant", "Blue Whale", "Giraffe"]),
        ("Who is the current President of the United States?", ["Donald Trump", "Joe Biden", "Barack Obama"]),
        ("In which year did World War II end?", ["1943", "1945", "1950"]),
        ("What is the currency of Japan?", ["Yuan", "Euro", "Yen"]),
        ("Who wrote 'Romeo and Juliet'?", ["Charles Dickens", "William Shakespeare", "Jane Austen"]),
        ("What is the capital of India?", ["Delhi", "Mumbai", "Kolkata"]),
        ("Who is known as the 'Father of the Nation' in India?", ["Jawaharlal Nehru", "Subhas Chandra Bose", "Mahatma Gandhi"]),
        ("What is the largest ocean on Earth?", ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean"]),
        ("What is the main ingredient in guacamole?", ["Tomato", "Avocado", "Onion"]),
        ("How many continents are there in the world?", ["5", "6", "7"]),
        ("Who painted the Mona Lisa?", ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso"]),
        ("What is the capital of Australia?", ["Sydney", "Melbourne", "Canberra"]),
        ("Which animal is known as the 'King of the Jungle'?", ["Elephant", "Lion", "Giraffe"]),
        ("What is the largest planet in our solar system?", ["Earth", "Jupiter", "Saturn"]),
        ("What is the currency of the United Kingdom?", ["Euro", "Pound Sterling", "Dollar"]),
        # Add more questions as needed
    ]

    # Define difficulty levels
    difficulty_levels = {
        'easy': 4,
        'medium': 6,
        'hard': 8,
    }

    # Choose difficulty level
    chosen_difficulty = input("Choose difficulty level (easy, medium, hard): ").lower()

    # Select questions based on difficulty level
    selected_questions = random.sample(questions_and_answers, difficulty_levels[chosen_difficulty])

    # Create and play the quiz
    quiz = QuizGame(selected_questions, difficulty_levels)
    quiz.play_quiz()