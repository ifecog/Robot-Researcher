from robotics import Robot

SCIENTISTS = ["Albert Einstein", "Isaac Newton", "Pierre Curie", "Charles Darwin"]

robot = Robot("Quandrinaut")


def introduce_yourself():
    """
    Introduce the robot and display the steps to take.
    """
    robot.say_hello()
    robot.steps_to_take()
    print()
   
    
def main():
    """
    The main function of the program.
    """
    introduce_yourself()

    # Open Wikipedia and retrieve information for each scientist
    for scientist in SCIENTISTS:
        robot.open_webpage("https://en.wikipedia.org")
        scientist_info = robot.get_scientist_info(scientist)
        
        # Display scientist information to the user
        print("Scientist: ", scientist)
        print("Birth Date: ", scientist_info[0])
        print("Death Date: ", scientist_info[1])
        print("Age: ", scientist_info[2])
        print("First Paragraph: ", scientist_info[3])
        print("Notable Award: ", scientist_info[4])
        print("\n")
    
    # Complete display by robot and farewell bidding.
    robot.say_goodbye()


if __name__ == "__main__":
    main()
