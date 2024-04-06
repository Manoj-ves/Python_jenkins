import os


def main():
    # Input first number
    num1 = float(get_input("Enter the first number: "))

    # Input second number
    num2 = float(get_input("Enter the second number: "))

    # Calculate the sum
    total = num1 + num2

    # Display the result
    print("The sum of", num1, "and", num2, "is:", total)

def get_input(prompt):
    # Check if running in Jenkins environment
    if 'JENKINS_URL' in os.environ:
        # Use default values or handle differently when running in Jenkins
        return 0
    else:
        # Ask for input interactively when not running in Jenkins
        return input(prompt)

if __name__ == "__main__":
    main()
