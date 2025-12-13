def check_for_line():
    word = "learning"
    try:
        with open("practice.txt", "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, start=1):
                if word in line:
                    print(line_no)
                    return line_no
        return -1  # Word not found
    except FileNotFoundError:
        print("Error: 'practice.txt' not found.")
        return -1

# Run the function
check_for_line()
