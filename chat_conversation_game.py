print("Heyy ! ")

a = input("How are you? (good or bad): ").strip().lower()

if a == "good" or a == "gud":
    print("Waao !! Nice bro ")

    b = input("Can we talk more or not? (yes or no): ").strip().lower()
    if b == "yes":
        c = input("So, what's your name?: ").strip()
        print(f"Nice to meet you, {c}")
        d = input("Where are you from?: ").strip()
        print(f"Oh Waoo!! {d}, that's really a nice place.")

        e = input("Wanna know about me? (yes or no): ").strip().lower()
        if e == "yes":
            print(f"Okay {c}!")
            print("My name is Arpit Sharma. I'm from Himachal Pradesh.")
            print("I don't even know what I'm doing but I'm still doing it.")
            print("For now it's enough. Bye bro, I will talk to you later.")
        elif e == "no":
            print("Haha !! Maybe you don't love to know about good new things.")

    elif b == "no":
        print("It's okay !! Enjoy your time.")

elif a == "bad":
    print("Oh! Take care of yourself. Don't worry, I will make your mood good.")
    f = input("Wanna play a game? (yes or no): ").strip().lower()
    if f == "yes":
        g = input("Okay! Guess anything. I will read your mind: ").strip()
        print("It's a difficult guess...")
        print("But I will surely read your mind...")
        print(f"Yeah! I got it. It's {g} 😄")
    elif f == "no":
        print("Okay, no problem. Take rest and feel better soon!")

else:
    print("Hmm, I didn't understand that. But hope you're doing okay!")




