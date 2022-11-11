# Name: Joshua C. Akers

import random
topics = []
TOTAL_TOPICS = 5

def main():
    num_used_topics = 0
    for i in range(TOTAL_TOPICS):
        topics.append("A")

    generate_another_randnum = True
    continue_search = True

    while generate_another_randnum:
        continue_search = True

        while continue_search:
            randnum = random.randint(0, TOTAL_TOPICS-1)
            if topics[randnum] == "A":
                topics[randnum] = "U"
                num_used_topics += 1
                continue_search = False

        print("\nRandom Topic Number: " + str(randnum+1))
        print("List of topic availability by number:")
        for i in range(TOTAL_TOPICS):
            print("\t" + str(i+1) + ". " + topics[i])

        if num_used_topics == TOTAL_TOPICS:
            print("There are no more topics available at this time.")
            return()
        else:
            answer = input("Would you like another random number? Y/N: ")
            if answer.upper() == "n" or answer.upper() == "N":
                generate_another_randnum = False

main()
