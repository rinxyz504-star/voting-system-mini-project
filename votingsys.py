voted_users=set()
voted={}
def vote(user_id, candidate):
    if user_id in voted_users:
        print(f"FRAUD ALERT: User {user_id} has already voted.")
        return
    voted_users.add(user_id)
    if candidate in voted:
        voted[candidate] += 1
    else:
        voted[candidate] = 1
    print(f"Vote recorded for {candidate} by user {user_id}")

def show_results():
    if len(voted) == 0:
        print("No votes have been cast yet.")
        return False
    for candidate, votes in voted.items():
        print(f"{candidate}: {votes} votes")

while True:
    print("cast a vote: 1")
    print("show results: 2")
    print("Exit: 3")
    candidate = input("Enter your name: ")
    user_id = input("Enter your user ID: ")
    choice = input("Enter your choice: ")
    if choice=="1":
        vote(user_id, candidate)
    elif choice=="2":
        show_results()
    elif choice=="3":
        print("Exiting the program.")
        break
    
    
