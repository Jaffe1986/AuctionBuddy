from datetime import date
from decimal import Decimal, ROUND_HALF_UP


class BidSession:
    """    A class to manage a session of bids, facilitating the addition, removal, and display of bids.

    Attributes:
        session_name (date): The name of the session, defaulting to today's date.
        bids (list): A list to store instances of Bid objects.

    Methods:
        run_session(): Initiates the bid session with a command-line interface to manage bids.
        display_bids(): Prints all bids in the session to the console.
        add_bid(seller_name, bidder_name, amount): Adds a new bid to the session.
        remove_bid(): Removes a bid from the session based on user selection.

    The run_session method provides a basic command-line interface (CLI) for interacting with the bid session,
    including options to add, remove, and display bids, as well as to exit the session. This method is primarily for
    testing purposes and can be replaced by a graphical user interface (GUI) in a production environment.

    The inner Bid class defines the structure of a bid, including the seller's name, the bidder's name, and the bid amount.

    Example:
        >>> session = BidSession()
        >>> session.add_bid("jamie", "tammy", 1.25)
        >>> session.run_session()
    """

    def __init__(self):
        self.session_name = date.today()
        self.bids = []

    # This is a test session menu that can be customized to test class objects outside the main body
    def run_session(self):
        while True:
            print("1: Add a bid")
            print("2 Remove a Bid")
            print("3: Display Bids")
            print("4: Exit")
            choice = input("Enter your choice. ")
            if choice == "1":
                seller_name = input("Sellers name: ")
                bidder_name = input("Bidders Name: ")
                amount = input("Amount: ")
                self.add_bid(seller_name, bidder_name, amount)
            elif choice == "2":
                self.remove_bid()
            elif choice == "3":
                self.display_bids()
            elif choice == "4":
                break

    def display_bids(self):
        for bid in self.bids:
            print(f"{bid.bidder_name}, {bid.amount}, {bid.seller_name}")

    def add_bid(self, seller_name, bidder_name, amount):
        # ensure the bid amount is in dollar format
        bid_amount = Decimal(amount).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        self.bids.append(self.Bid(seller_name, bidder_name, bid_amount))

    def remove_bid(self):
        if not self.bids:
            print("No Bids")
            return
        for index, bid in enumerate(self.bids, start=1):
            print(f"{index}: {bid.seller_name}, {bid.bidder_name}, ${bid.amount}")
        try:
            selection = int(input("Enter number of bid you want to remove: ")) - 1
            if 0 <= selection < len(self.bids):
                removed_bid = self.bids.pop(selection)
                print(f"{removed_bid.bidder_name}, {removed_bid.seller_name}, {removed_bid.amount} removed")

        except ValueError:
            print("Please enter a number")

    class Bid:
        def __init__(self, seller_name, bidder_name, amount):
            self.seller_name = seller_name
            self.bidder_name = bidder_name
            self.amount = amount


session = BidSession()
# session.add_bid("jamie", "tammy", 1.25)
