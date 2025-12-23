import os
import time
from module import Room
from bi import calculate_total_cost

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_ui():
    print("="*60)
    print("      AKWAABA HOTEL - BOOKING TERMINAL")
    print("      Luxury Eco-Resort (Ada Foah)")
    print("="*60)

def main():
    # Create rooms [101–105] for demo
    rooms = [Room(num) for num in range(101, 106)]
    bookings = []

    while True:
        clear()
        draw_ui()
        print("1. Book a Room")
        print("2. View Daily Summary Report")
        print("3. Check-out Guest")
        print("4. Exit System")
        print("-" * 60)

        choice = input("Select Command: ")

        if choice == '1':
            print("\n--- NEW BOOKING ENTRY ---")
            guest = input("Guest Name: ").title()
            nights = int(input("Number of Nights: "))
            base_price = float(input("Base Price per Night (GHS): "))

            # Find first available room
            assigned = None
            for room in rooms:
                if not room.is_occupied:
                    room.check_in(guest)
                    assigned = room
                    break

            if assigned:
                total_cost = calculate_total_cost(base_price * nights)
                bookings.append({"guest": guest, "room": assigned.room_number,
                                 "nights": nights, "cost": total_cost})
                print(f"\n>>> BOOKING SUCCESSFUL")
                print(f"Room {assigned.room_number} assigned to {guest}")
                print(f"Total Cost (incl. Levy & VAT): GHS {total_cost:,.2f}")
            else:
                print("SORRY: No rooms available.")

            input("\nPress Enter to continue...")

        elif choice == '2':
            clear()
            draw_ui()
            print(f"{'GUEST':<15} | {'ROOM':<6} | {'NIGHTS':<7} | {'TOTAL COST'}")
            print("-" * 60)

            total_revenue = 0
            for record in bookings:
                g = record['guest']
                r = record['room']
                n = record['nights']
                c = record['cost']
                print(f"{g:<15} | {r:<6} | {n:<7} | GHS {c:,.2f}")
                total_revenue += c

            print("-" * 60)
            print(f"TOTAL REVENUE COLLECTED: GHS {total_revenue:,.2f}")
            input("\nPress Enter to return to menu...")

        elif choice == '3':
            guest = input("Enter Guest Name to Check-out: ").title()
            found = False
            for room in rooms:
                if room.guest_name == guest:
                    print(room.check_out())
                    found = True
                    break
            if not found:
                print("Guest not found in current bookings.")
            input("\nPress Enter to continue...")

        elif choice == '4':
            print("System Locking... Goodbye.")
            break

if __name__ == "__main__":
    main()
