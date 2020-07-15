def run(*kids):
    for kid in kids:
        print(f"{kid} runs like a goddamn machine!")

def swing(*kids):
    for kid in kids:
        print(f"Tarzan? No! That's {kid} swinging like a champ!")

def slide(*kids):
    for kid in kids:
        print(f"Here comes {kid}, sliding better than I've ever slided into any DM before.")

def hide_and_seek(*kids):
    for kid in kids:
        print(f"{kid} is hiding pretty well. I'm not sure I can find them.")

run("Pam", "Sam", "Andrea", "Will")
swing("Marybeth", "Ariel", "Kevin", "Courtney")
slide("Mike", "Jack", "Jennifer", "Earl")
hide_and_seek("Henry", "Heather", "Hayley", "Hugh")