from instances import INSTANCES
from aws_manager import start_instance, stop_instance, get_status
from logger import log

def show_instances():
    print("\nAvailable Lightsail Instances:")
    for key, inst in INSTANCES.items():
        print(f"{key}. {inst['name']}")

def main_menu():
    print("\nAWS Lightsail WordPress Manager")
    print("1. Start Instance")
    print("2. Stop Instance")
    print("3. Check Status")
    print("4. Exit")

def main():
    while True:
        main_menu()
        choice = input("Choose an option: ")

        if choice == "4":
            print("Goodbye!")
            break

        show_instances()
        inst_choice = input("Select instance: ")

        if inst_choice not in INSTANCES:
            print("Invalid selection")
            continue

        inst = INSTANCES[inst_choice]

        if choice == "1":
            start_instance(inst["instance_name"], inst["region"])
            log(f"Started {inst['name']}")
            print("Instance starting...")

        elif choice == "2":
            stop_instance(inst["instance_name"], inst["region"])
            log(f"Stopped {inst['name']}")
            print("Instance stopping...")

        elif choice == "3":
            status = get_status(inst["instance_name"], inst["region"])
            print(f"Status: {status}")
            log(f"Checked status of {inst['name']}")

        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
