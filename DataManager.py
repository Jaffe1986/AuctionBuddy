import csv
import os


class DataManager:
    """
    The DataManager class is part of a bidding system, responsible for handling the storage and management of bid
    session data. It ensures that bid information is systematically saved and organized within a specific
    directory structure, facilitating easy access and management of session data over time.

    Class Attributes:
    - sessions_folder (str): The name of the directory where all session data will be stored. Default is "Sessions".
    - session_name (str): The name of the current bid session. This is used to create uniquely named CSV files for each
     session.

    Methods:
    - __init__(self, session_name): Constructor that initializes the DataManager instance with a specific session name 
     and ensures the session directory exists.
    - get_session(self): Checks if the session directory exists; if not, it creates the directory. This method supports
      the organizational structure of the session data.
    - save_bid_session(self, bids): Takes a list of bids and saves them into a CSV file named after the session. Each
      bid is expected to be an object or dictionary with 'seller_name', 'bidder_name', and 'amount' attributes or keys.

    Usage:
    To use the DataManager, instantiate it with a specific session name. Then, call the save_bid_session method with the
    list of bid objects to save the session's data to a CSV file within the 'Sessions' directory. This allows for
    persistent storage and easy retrieval of bid session data, supporting the broader functionalities
    of the bidding system.

    Example:
        data_manager = DataManager("Session_2024_03_27")
        data_manager.save_bid_session(bids_list)
    Where 'bids_list' is a list of bids, with each bid containing 'seller_name', 'bidder_name', and 'amount'.

    Note:
    This class is designed with the assumption that it will be integrated into a larger bidding system. Developers
    should ensure that bid data passed to save_bid_session conforms to the expected structure.
    """

    def __init__(self, session_name):
        self.sessions_folder = "Sessions"
        self.get_session()
        self.session_name = session_name
    def get_session(self):
        if not os.path.exists(self.sessions_folder):
            os.makedirs(self.sessions_folder)
    def save_bid_session(self, bids):
        file_path = os.path.join(self.sessions_folder, f"{self.session_name}.csv")
        with open(file_path, mode='w', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["seller_name", "bidder_name", "amount"])
            for bid in bids:
                writer.writerow([bid.seller_name, bid.bidder_name, str(bid.amount)])



