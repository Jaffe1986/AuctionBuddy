from SessionManager import *
from DataManager import *
import tkinter as tk
from tkinter import filedialog

def main_menu():
    root = tk.Tk()
    root.withdraw()

    while True:
        print('1: Create session')
        print('2: Add bid to session')
        print('3: Remove bid from session')
        print('4: Display all bids in current session')
        print('5: Show session winners')
        print('6: Save session')
        print("7: Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            """Handle session creation"""
            session = BidSession()
        elif choice == "2":
            seller_name = input("Seller Name: ")
            bidder_name = input("Bidder Name: ")
            amount = input("Amount: ")
            session.add_bid(seller_name, bidder_name, amount)
        elif choice == "3":
            session.remove_bid()
        elif choice == "4":
            session.display_bids()
        elif choice == "5":
            file = filedialog.askopenfilename(title="Select a file",filetypes=(("Word Documents", "*.docx"), ("All Files", "*.*")))
            data = DataManager(session.session_name)
            data.view_session_result(file)
        elif choice == "6":
            data = DataManager(session.session_name)
            data.save_bid_session(session.bids)
        elif choice == "7":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main_menu()
