import random
import time

li = ["The quick brown fox jumps so high.",
      "Coding daily improves your logic well.",
      "Learning Python makes you think smart.",
      "She loves reading books at the park.",
      "Practice typing fast to boost your speed.",
      "A bright rainbow appeared after rain.",
      "Always stay curious and keep exploring.",
      "The little cat sleeps under the warm sun.",
      "Hard work and patience lead to success.",
      "Playing chess helps to sharpen your mind."]

def type_spd():
    sentence = random.choice(li)
    print("The following sentence has to be typed after the countdown.")
    print(sentence)
    time.sleep(5)  # Shorter countdown for better experience
    print("\nType the given sentence below:")
    
    init_time = time.time()
    user_input = input().strip().lower()  # Strip spaces and convert to lowercase
    diff_time = time.time() - init_time
    
    # Display result whether correct or incorrect input
    if user_input == sentence.lower():  # Compare lowercased versions for accuracy
        wpm = len(user_input.split()) / (diff_time / 60)  # Calculate WPM
        print(f"Your time taken is {int(diff_time)} seconds.")
        print(f"Your typing speed is {wpm:.2f} words per minute.")
    else:
        print("You have typed some mistakes or forgot about the full stop.")
        print("Please try again!!")
    
    # Ask if the user wants to try again or quit after result
    again = input("Do you want to try again? (yes/no): ").strip().lower()
    if again == "yes":
        type_spd()  # Recursively call the function to retry
    else:
        print("Thanks for playing!")  # End the program with a message

# Start the typing test
type_spd()
