import subprocess
import sys


def run_lint_check():
    """Runs flake8 on all Python files in the current directory and its
    subdirectories."""
    command = ["flake8", "."]
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0 and result.stdout:
            print("Linting issues found:\n")
            print(result.stdout)
            return True, result.stdout
        elif result.returncode == 0:
            print("No linting issues found.")
            return False, ""
        else:
            # Handle cases where there's an error but no stdout
            print("An error occurred during linting.")
            return True, ""  # Indicate issues to prompt the fix option
    except FileNotFoundError:
        print(
            "Error: flake8 is not installed. Please install it using "
            "'pip install flake8'."
        )
        sys.exit(1)


def apply_autopep8(linting_output):
    """Attempts to fix linting issues using autopep8."""
    files_to_format = set()
    for line in linting_output.splitlines():
        parts = line.split(":")
        if len(parts) >= 2:
            filepath = parts[0].strip()
            if filepath.endswith(".py"):
                files_to_format.add(filepath)

    if not files_to_format:
        print("No files identified for auto-formatting.")
        return

    print("\nAttempting to auto-format the following files:")
    for f in files_to_format:
        print(f"- {f}")

    command = ["autopep8", "--in-place"] + list(files_to_format)
    try:
        subprocess.run(command, check=True)
        print("\nAuto-formatting complete. Please review the changes.")
    except subprocess.CalledProcessError as e:
        print(f"Error running autopep8: {e}")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")
    except FileNotFoundError:
        print(
            "Error: autopep8 is not installed. Please install it using "
            "'pip install autopep8' if you want to auto-fix."
        )


if __name__ == "__main__":
    issues_found, linting_output = run_lint_check()

    if issues_found:
        while True:
            answer = (
                input(
                    "Would you like to attempt to automatically fix these "
                    "issues? (Y/N): "
                )
                .strip()
                .upper()
            )
            if answer == "Y":
                apply_autopep8(linting_output)
                break
            elif answer == "N":
                print("Skipping auto-fix.")
                break
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")
