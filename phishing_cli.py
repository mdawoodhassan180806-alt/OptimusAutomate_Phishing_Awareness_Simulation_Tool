from phishing_data import EMAIL_EXAMPLES, QUIZ_QUESTIONS

def show_examples():
    print("\n=== PHISHING EMAIL EXAMPLES ===\n")

    for i, item in enumerate(EMAIL_EXAMPLES, start=1):
        print(f"\nExample {i}: {item['title']}")
        print("-" * 50)
        print(item["email"])

        print("\nRed Flags:")

        for tactic in item["tactics"]:
            print(f"  - {tactic}")

        print("\n")


def run_quiz():
    print("\n=== PHISHING QUIZ ===\n")

    score = 0

    for q in QUIZ_QUESTIONS:
        answer = input(
            f"{q['question']}\n(phishing/legitimate): "
        ).strip().lower()

        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. Correct answer: {q['answer']}\n")

    print(f"Final Score: {score}/{len(QUIZ_QUESTIONS)}")


def main():
    while True:
        print("\n=== Phishing Awareness Tool ===")
        print("1. View Examples")
        print("2. Take Quiz")
        print("3. Exit")

        choice = input("Select: ")

        if choice == "1":
            show_examples()

        elif choice == "2":
            run_quiz()

        elif choice == "3":
            print("Goodbye.")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
