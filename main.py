import subprocess
import sys

def run_scrapers():
    print("Running scrapers...")
    # Example: run each scraper script
    scrapers = [
        "extract/flipkart.py",
        "extract/amazon.py",
        # Add other scraper scripts here
    ]
    for scraper in scrapers:
        print(f"Running {scraper}...")
        subprocess.run([sys.executable, scraper], check=True)

def run_data_cleaning():
    print("Running data cleaning...")
    subprocess.run([sys.executable, "utils/cleaner.py"], check=True)

def run_db_inserts():
    print("Inserting data into database...")
    subprocess.run([sys.executable, "database/insert_data.py"], check=True)

def run_backend():
    print("Starting Flask API backend...")
    subprocess.run([sys.executable, "backend/app.py"], check=True)

def run_frontend():
    print("Starting Streamlit frontend...")
    subprocess.run(["streamlit", "run", "frontend/app.py"], check=True)

def main():
    print("E-commerce Data Pipeline CLI")
    print("1. Run scrapers")
    print("2. Run data cleaning")
    print("3. Insert data into DB")
    print("4. Start backend API")
    print("5. Start frontend preview")
    print("6. Run all steps")
    choice = input("Enter choice (1-6): ").strip()

    if choice == "1":
        run_scrapers()
    elif choice == "2":
        run_data_cleaning()
    elif choice == "3":
        run_db_inserts()
    elif choice == "4":
        run_backend()
    elif choice == "5":
        run_frontend()
    elif choice == "6":
        run_scrapers()
        run_data_cleaning()
        run_db_inserts()
        print("All steps completed. You can now start backend and frontend separately.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
