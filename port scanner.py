import socket

def scan_ports(target, start_port, end_port):
    print(f"\nScanning target: {target}")
    for port in range(start_port, end_port + 1):
        print(f"Checking port {port}...")  # Debugging line
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.1)  # Set timeout to 100ms for faster scanning
            result = s.connect_ex((target, port))
            if result == 0:  # Port is open
                print(f"Port {port}: Open")
            else:
                print(f"Port {port}: Closed")

if __name__ == "__main__":
    while True:
        try:
            # Input values from user
            target = input("\nEnter target IP (or type 'exit' to quit): ").strip()
            if target.lower() == 'exit':
                print("Exiting the scanner. Goodbye!")
                break

            start_port = int(input("Enter start port: "))
            end_port = int(input("Enter end port: "))

            # Validate port range
            if start_port < 0 or end_port > 65535 or start_port > end_port:
                print("Error: Invalid port range. Please enter valid ports between 0-65535.")
                continue

            # Run the port scanning
            scan_ports(target, start_port, end_port)

        except ValueError:
            print("Error: Ports must be integers within the range 0-65535.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
