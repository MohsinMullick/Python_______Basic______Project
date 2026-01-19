#Voting System Simulator
print("="*50)
print("     WELCOME TO  VOTING SYSTEM SIMULATOR  ")
print("="*50)
print("Vote for your favorite candidate!")
print("Type 'q' or 'quit' or 'exit' to stop voting and see the results")
print("="*50)

candidates={
    "1":{"name":"Mohsin","Votes":0},
     "2":{"name":"Mullik","Votes":0},
    "3":{"name":"Satu","Votes":0}
}
voted_users=set()
print("Candidates: ")
for cid,info in candidates.items():
    print(f"{cid}.{info["name"]}")
    print("="*50)

while True:
    voter_id=input("Enter your voter id (or 'q' to finish voting): ").strip().lower()
    if voter_id in ['q','quit','exit']:
        break
    if voter_id in voted_users:
        print("You have already voted! One voter=one vote.")
        continue

    voted_users.add(voter_id)
    print("Choice your candidate(enter number 1 to 3): ")
    vote=input("").strip()