# ============================================================
#  SIMPLE CALCULATOR
#  Concepts: functions, conditionals, input validation
# ============================================================
# A function is a reusable block of code that performs a task.
# We define one function per operation to keep code organized.


# ── BASIC OPERATIONS ────────────────────────────────────────

def add(a, b):
    """Addition: combines two numbers."""
    return a + b

def subtract(a, b):
    """Subtraction: finds the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Multiplication: repeated addition of a number."""
    return a * b

def divide(a, b):
    # Conditional: before dividing, check if b is zero.
    # Dividing by zero is mathematically undefined, so we guard against it.
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b


# ── EXTENSION OPERATIONS ────────────────────────────────────

def power(a, b):
    """Power (a ** b): raises 'a' to the exponent 'b'.
    Example: 2 ** 3 = 8
    """
    return a ** b

def modulus(a, b):
    """Modulus (a % b): returns the remainder after dividing a by b.
    Example: 10 % 3 = 1  (because 10 = 3*3 + 1)
    """
    if b == 0:
        return "Error: Cannot take modulus with zero!"
    return a % b


# ── CORE CALCULATOR FUNCTION ────────────────────────────────

def calculate(a, b, operator):
    """
    Main dispatcher function.
    Takes two numbers and an operator string, then calls
    the matching operation function using a dictionary lookup.

    Using a dict (operator → function) instead of a long
    if/elif chain is cleaner and easier to extend.
    """

    # Map each operator symbol to its corresponding function.
    operations = {
        "+":  add,
        "-":  subtract,
        "*":  multiply,
        "/":  divide,
        "**": power,   # extension: power
        "%":  modulus, # extension: modulus
    }

    # Check whether the operator the user typed is supported.
    # dict.get() returns None if the key doesn't exist — safer than direct access.
    operation_func = operations.get(operator)

    if operation_func is None:
        # Conditional: operator not found → return a helpful error.
        return f"Error: Unknown operator '{operator}'. Supported: {list(operations.keys())}"

    # Call whichever function was selected and return its result.
    return operation_func(a, b)


# ── INPUT HELPER ────────────────────────────────────────────

def get_number(prompt):
    """
    Repeatedly ask the user for a number until they type a valid one.
    This is input validation — preventing crashes from bad data.

    'while True' creates an infinite loop; 'break' exits it on success.
    'try/except' catches errors so the program doesn't crash.
    """
    while True:
        try:
            # float() converts a string like "3.5" to the number 3.5
            return float(input(prompt))
        except ValueError:
            # ValueError is raised when float() can't parse the string.
            print("  ⚠  Invalid number. Please enter a numeric value (e.g. 5, -2, 3.14).\n")


# ── MAIN PROGRAM ────────────────────────────────────────────

def main():
    """
    Entry point of the program.
    Runs a loop so the user can perform multiple calculations.
    """
    print("=" * 45)
    print("        SIMPLE CALCULATOR")
    print("  Operators: +  -  *  /  **  %")
    print("  Type 'q' at any prompt to quit.")
    print("=" * 45)

    while True:
        print()  # blank line for readability

        # ── Get first number ──────────────────────────────
        raw = input("Enter first number : ").strip()
        if raw.lower() == "q":
            break
        try:
            num1 = float(raw)
        except ValueError:
            print("  ⚠  Invalid number. Try again.")
            continue  # 'continue' skips the rest of the loop body and restarts

        # ── Get operator ──────────────────────────────────
        operator = input("Enter operator (+, -, *, /, **, %): ").strip()
        if operator.lower() == "q":
            break

        # ── Get second number ─────────────────────────────
        raw = input("Enter second number: ").strip()
        if raw.lower() == "q":
            break
        try:
            num2 = float(raw)
        except ValueError:
            print("  ⚠  Invalid number. Try again.")
            continue

        # ── Calculate & Display ───────────────────────────
        result = calculate(num1, num2, operator)

        # If the result is a number, format it nicely.
        # isinstance() checks the type of a variable at runtime.
        if isinstance(result, (int, float)):
            # Remove unnecessary trailing zeros (e.g. 4.0 → 4)
            formatted = int(result) if result == int(result) else result
            print(f"\n  ✔  {num1} {operator} {num2} = {formatted}")
        else:
            # Result is an error string
            print(f"\n  {result}")

    print("\nGoodbye! 👋")


# ── RUN ─────────────────────────────────────────────────────
# This block ensures main() only runs when this file is executed
# directly — not when it's imported as a module by another file.
if __name__ == "__main__":
    main()
