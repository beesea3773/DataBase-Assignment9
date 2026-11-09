class Person:
    """Represents a person in the social network."""

    def __init__(self, name):
        # Save the person's name and start with no friends.
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        # Add the friend if they are not already in the list.
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    """Stores people and their friendships."""

    def __init__(self):
        # Store each person using their name as the key.
        self.people = {}

    def add_person(self, name):
        # Make sure the person is not already in the network.
        if name not in self.people:
            self.people[name] = Person(name)
        else:
            print(f"{name} is already in the network.")

    def add_friendship(self, person1_name, person2_name):
        # Check that both people exist.
        if person1_name not in self.people or person2_name not in self.people:
            print("Friendship not created. One or both people do not exist!")
            return

        # Do not let someone become their own friend.
        if person1_name == person2_name:
            print("A person cannot be friends with themselves.")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        # Add the friendship in both directions.
        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        # Print each person and their friends.
        for person in self.people.values():
            friend_names = [friend.name for friend in person.friends]
            print(f"{person.name} is friends with: {', '.join(friend_names)}")


# Test the social network.
if __name__ == "__main__":
    network = SocialNetwork()

    # Add six people.
    network.add_person("Alex")
    network.add_person("Jordan")
    network.add_person("Morgan")
    network.add_person("Taylor")
    network.add_person("Casey")
    network.add_person("Riley")

    # Create eight friendships.
    network.add_friendship("Alex", "Jordan")
    network.add_friendship("Alex", "Morgan")
    network.add_friendship("Jordan", "Taylor")
    network.add_friendship("Morgan", "Casey")
    network.add_friendship("Taylor", "Riley")
    network.add_friendship("Casey", "Riley")
    network.add_friendship("Morgan", "Riley")
    network.add_friendship("Alex", "Taylor")

    # Test a person who does not exist.
    network.add_friendship("Jordan", "Johnny")

    # Test adding a duplicate person.
    network.add_person("Alex")

    # Print the finished network.
    network.print_network()



# Design Memo
# For this assignment, I created a social network using a graph
# data structure. I used a Person class to store each person's name and their list of friends. I also created a SocialNetwork
# class that stores everyone in a dictionary and allows people to be added, connected, and displayed.
# I chose a graph because social networks have people who can connect to multiple other people. Each person represents a
# node, and each friendship represents an edge. Since friendships work both ways, I made sure that adding a friendship updates
# both people's friend lists.
# A regular list would not work as well because it would be
# harder to organize and manage all the connections between people. A tree would also have problems because trees follow
# a parent-and-child structure. In a social network, people can have connections in many different directions, and there
# is no single person at the top. One advantage of my program is that using a dictionary makes
# it fast to find someone by their name. However, checking whether someone is already in a friend's list can take longer as the network grows because the program may need to search
# through the list. Printing the entire network also takes more time when there are more people and friendships.
#I tested the program with six people and eight friendships. I also tested adding a duplicate person and trying to connect
# someone who does not exist. Both situations were handled without crashing the program.
