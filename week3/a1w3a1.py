import sys


def job_offer_template():
    name = input("First name:")
    if not (name.istitle() and name.isalpha() and 2 <= len(name) <= 10):
        print("Input error")
        return

    last_name = input("Last Name:")
    if not (last_name.istitle() and last_name.isalpha() and 2 <= len(last_name) <= 10):
        print("Input error")
        return

    job_title = input("Job title:")
    if not (len(job_title) >= 10):
        print("Input error")
        return

    annual_salary = input("Annual salary:")
    try:
        salary = float(annual_salary.replace(",", ""))
        if not (20000.00 <= salary <= 80000.00):
            print("Input error")
            return
    except ValueError:
        print("Input error")
        return

    starting_date = input("Starting date (YYYY-MM-DD):")
    parts = starting_date.split("-")
    if len(parts) != 3 or parts[0] not in ["2021", "2022"] or not parts[1].isdigit() or not parts[2].isdigit():
        print("Input error")
        return
    if not (1 <= int(parts[1]) <= 12 and 1 <= int(parts[2]) <= 31):
        print("Input error")
        return

    print(f"Dear {name} {last_name}, After careful evaluation of your application for the position of {job_title}, we are glad to offer you the job. Your salary will be {annual_salary} euro annually. Your start date will be on {starting_date}. Please do not hesitate to contact us with any questions. Sincerely, HR department of XYZ")


def rejection_template():
    name2 = input("First name:")
    if not (name2.istitle() and name2.isalpha() and 2 <= len(name2) <= 10):
        print("Input error")
        return

    last_name2 = input("Last Name:")
    if not (last_name2.istitle() and last_name2.isalpha() and 2 <= len(last_name2) <= 10):
        print("Input error")
        return

    job_title2 = input("Job title:")
    if not (len(job_title2) >= 10 and job_title2.isalpha()):
        print("Input error")
        return

    feedback = input("Feedback? 'Yes' or 'No':")
    if feedback not in ["Yes", "No"]:
        print("Input error")
        return

    if feedback == "Yes":
        feedback_info = input("Enter your feedback: ")
        print(f"Dear {name2} {last_name2}, after careful evaluation of your application for the position of {job_title2}, we have decided to proceed with another candidate. Here is our feedback: {feedback_info}. We wish you the best in finding your future desired career. Please do not hesitate to contact us with any questions. Sincerely, HR department of XYZ")
    else:
        print(f"Dear {name2} {last_name2}, after careful evaluation of your application for the position of {job_title2}, at this moment we have decided to proceed with another candidate. We wish you the best in finding your future desired career. Please do not hesitate to contact us with any questions. Sincerely, HR department of XYZ")


response = input("More letters? 'Yes' or 'No':")
if response == "No":
    sys.exit()

which = input("Job offer or Rejection: ")
if which == "Job offer":
    job_offer_template()
elif which == "Rejection":
    rejection_template()
