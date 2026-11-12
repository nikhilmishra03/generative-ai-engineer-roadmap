
import time
from functools import wraps


# STEP 1: Timing decorator
def timer_decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        start = time.perf_counter()

        result = func(*args, **kwargs)

        end = time.perf_counter()

        print(
            "Execution time:",
            round(end - start, 4),
            "seconds"
        )

        return result

    return wrapper


# STEP 2: Read records using a generator
def read_records(file_path):

    with open(file_path, "r") as file:

        for line in file:

            line = line.strip()

            if line:
                yield line


# STEP 3: Generate customer IDs

def read_customer_ids(file_path):

    for record in read_records(file_path):

        data = record.split(",")

        if len(data) != 3:
            continue

        customer_id = data[0].strip()
        customer_name = data[1].strip()
        location = data[2].strip()

        if not customer_id or not customer_name or not location:
            continue

        yield customer_id


# STEP 4: Process customer records
@timer_decorator
def process_customers(file_path):

    count = 0

    for record in read_records(file_path):

        data = record.split(",")

        if len(data) != 3:
            continue

        customer_id = data[0].strip()
        customer_name = data[1].strip()
        location = data[2].strip()

        if not customer_id or not customer_name or not location:
            continue

        print(
            customer_id,
            customer_name,
            location
        )

        count += 1

    return count

@timer_decorator
def calculate_total(a, b):
    return a + b


result = calculate_total(10, 20)

print("Returned result:", result)

# STEP 5: Execute application
if __name__ == "__main__":

    print("CUSTOMER RECORDS")
    #total = process_customers("missing_customers.txt")
    total = process_customers("Day-02-Decorators-Generators/customers.txt")

    print("\nTotal processed:", total)

    print("\nCUSTOMER IDS")

    for customer_id in read_customer_ids(
        "Day-02-Decorators-Generators/customers.txt"
    ):
        print(customer_id)
