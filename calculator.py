class Calculator:
    
    OPERATORS = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else None,
        '**':lambda x, y: x ** y,
        '%': lambda x, y: x % y if y != 0 else None
    }

    @staticmethod
    def get_number_input(prompt):
        """Get numerical input from user with error handling."""
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Error: Please enter a valid number.")

    @classmethod
    def get_operator(cls):
        """Get operator input from user with validation."""
        while True:
            operator = input("Enter the operator (+, -, *, /, **, %): ").strip()
            if operator in cls.OPERATORS:
                return operator
            print(f"Error: Please enter a valid operator from {', '.join(cls.OPERATORS.keys())}")

    @staticmethod
    def display_instructions():
        """Display calculator instructions."""
        print("\n=== Calculator Instructions ===")
        print("Available operations:")
        print("  + : Addition")
        print("  - : Subtraction")
        print("  * : Multiplication")
        print("  / : Division")
        print("  ** : Exponentiation")
        print("  % : Modulus (Remainder)")
        print("========================\n")

    @classmethod
    def calculate(cls, num1, num2, operator):
        """Perform calculation and handle edge cases."""
        if operator in ['/', '%'] and num2 == 0:
            return None, "Error: Division by zero!"
        
        try:
            result = cls.OPERATORS[operator](num1, num2)
            return result, None
        except Exception as e:
            return None, f"Error: {str(e)}"

    def run(self):
        """Main calculator loop."""
        print("Welcome to Inathi's Advanced Calculator!")
        
        while True:
            self.display_instructions()
            num1 = self.get_number_input("Enter the first number: ")
            num2 = self.get_number_input("Enter the second number: ")
            operator = self.get_operator()
            
            result, error = self.calculate(num1, num2, operator)
            
            if error:
                print(error)
            else:
                print(f"\nResult: {num1} {operator} {num2} = {result}")
    
                if result.is_integer():
                    print(f"(Integer result: {int(result)})")


            if not input("\nContinue? (y/n): ").lower().startswith('y'):
                print("Thank you for using the calculator. Goodbye!")
                break


def main():
    """Entry point of the calculator program."""
    try:
        calculator = Calculator()
        calculator.run()
    except KeyboardInterrupt:
        print("\nCalculator terminated by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()