import random

def secret_santa():
    with open("people.txt", "r") as file:
        people = file.readlines()
        people = [person.strip() for person in people]
    
    # Try up to 100 times to generate valid assignments
    for attempt in range(100):
        assignments = people.copy()
        random.shuffle(assignments)
        
        # Check if anyone is assigned to themselves
        valid = True
        for i in range(len(people)):
            if people[i] == assignments[i]:
                valid = False
                break
        
        if valid:
            # Write valid assignments to file
            with open("result.txt", "w") as file:
                for i in range(len(people)):
                    file.write(f"{people[i]} is buying for {assignments[i]}\n")
            return True
    
    raise Exception("Could not generate valid Secret Santa assignments after 100 attempts")

if __name__ == "__main__":
    secret_santa()
