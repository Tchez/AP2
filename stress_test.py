

import csv
import time
from faker import Faker
from functions import create_person, search_by_name, search_by_salary
import psutil

def generate_fake_data(num_records: int):
    """Generate and insert fake data into the CSV files."""
    fake = Faker()
    for _ in range(num_records):
        name = fake.name()
        salary = fake.random_int(min=20000, max=100000)
        create_person(name, salary)

def measure_insertion_time(num_records: int) -> float:
    """Measure the time taken to insert num_records into the CSV files."""
    start_time = time.time()
    generate_fake_data(num_records)
    end_time = time.time()
    return end_time - start_time

def measure_search_time() -> (float, float):
    """Measure the time taken to search for a name and a salary."""
    # Using a common name and salary for search measurements
    search_name = "James Smith"
    search_salary = 50000.0

    # Measure search by name
    start_time_name = time.time()
    search_by_name(search_name)
    end_time_name = time.time()

    # Measure search by salary
    start_time_salary = time.time()
    search_by_salary(search_salary)
    end_time_salary = time.time()

    return end_time_name - start_time_name, end_time_salary - start_time_salary

def get_resource_usage() -> dict:
    """Get the current resource usage (CPU, RAM, and Disk)."""
    cpu_percent = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().used / (1024 ** 3)  # Convert bytes to GB
    disk_usage = psutil.disk_usage('/').used / (1024 ** 3)  # Convert bytes to GB
    
    return {
        "CPU (%)": cpu_percent,
        "RAM (GB)": ram_usage,
        "Disk (GB)": disk_usage
    }

def run_stress_test():
    data_sizes = {
        "Small": 300,
        "Medium": 600,
        "Large": 1200
    }

    report = []

    for label, size in data_sizes.items():
        print(f"Running stress test for {label} data size ({size} records)...")
        
        insertion_time = measure_insertion_time(size)
        search_name_time, search_salary_time = measure_search_time()
        resources = get_resource_usage()

        report.append({
            "Data Size": label,
            "Insertion Time (s)": insertion_time,
            "Search by Name Time (s)": search_name_time,
            "Search by Salary Time (s)": search_salary_time,
            **resources
        })

    return report

if __name__ == "__main__":
    test_report = run_stress_test()
    
# Print the results in a formatted table
headers = ["Data Size", "Insertion Time (s)", "Search by Name Time (s)", "Search by Salary Time (s)", "CPU (%)", "RAM (GB)", "Disk (GB)"]
print("|".join([header.ljust(25) for header in headers]))
print("-" * (25 * len(headers) + len(headers) - 1))

for entry in test_report:
    row = [str(entry[header]).ljust(25) for header in headers]
    print("|".join(row))

