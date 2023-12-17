'''CHANGELOG: 
1)Error Handling
2)More verbose comments
'''
import random
import csv

# Global variables
chapter_percentages = {}  # A dictionary to store chapter percentages
counter = 0  # A counter variable to keep track of the number of questions generated
custom_question_no = 0  # A variable to store the total number of questions to be generated

def directory_changer(csv_file_path):
    """
    Change directory and read chapter percentages from a CSV file.

    Parameters:
    - csv_file_path (str): The path to the CSV file.

    Raises:
    - FileNotFoundError: If the specified CSV file is not found.
    - ValueError: If there is an issue reading the CSV file or if the file format is incorrect.
    """
    global chapter_percentages

    try:
        with open(csv_file_path, 'r', encoding='utf-8-sig') as csv_file:
            reader = csv.DictReader(csv_file)

            # Check if the required columns are present
            if 'Chapter' not in reader.fieldnames or 'Percentage' not in reader.fieldnames:
                raise ValueError("-------------------------------------------------------------\n"
                                 "You have an incorrectly formatted CSV file.\n"
                                 "The CSV file should have the first line defining the format 'Chapter,Percentage'.\n"
                                 "An example CSV file would look like this:\n"
                                 "Chapter,Percentage\n"
                                 "Chapter_1,5\n"
                                 "Chapter_2,10\n"
                                 "-------------------------------------------------------------")

            chapter_percentages = {row['Chapter']: float(row['Percentage'].strip('%')) for row in reader}
    except FileNotFoundError:
        raise FileNotFoundError("Error: File not found.")
    except csv.Error as e:
        raise ValueError(f"Error reading CSV file: {e}")

def get_no_of_questions(chapter_name, custom_question_no):
    """
    Calculate the number of questions based on chapter percentages.

    Parameters:
    - chapter_name (str): The name of the chapter.
    - custom_question_no (int): The total number of questions to be generated.

    Returns:
    - int: The number of questions for the specified chapter.
    """
    if chapter_name in chapter_percentages:
        return int(chapter_percentages[chapter_name] * custom_question_no / 100)
    else:
        return 0

def get_question_nums(num_weighed, total_questions):
    """
    Generate unique question numbers based on weighted percentages.Useful when the question bank is easy to hard.Real Exams have a mix of
    easy and hard questions so this emsures that.

    Parameters:
    - num_weighed (int): The number of questions to be generated based on weighted percentages.
    - total_questions (int): The total number of questions available for the chapter.

    Returns:
    - list: A list of strings representing the unique random question numbers.
    """
    unique_question_nums = set()
    global counter
    counter = 0

    while len(unique_question_nums) < num_weighed:
        question_num = random.randint(1, total_questions)
        
        if question_num not in unique_question_nums:
            unique_question_nums.add(question_num)
            counter += 1

    sorted_question_nums = sorted(unique_question_nums)
    return [str(num) for num in sorted_question_nums]

def relative_weightage(chapters):
    """
    Calculate and display the relative weightage of chapters.

    Parameters:
    - chapters (int): The number of chapters for which relative weightage is to be calculated.

    Raises:
    - ValueError: If there is an issue with user input or calculations.
    """
    while True:
        name_list = []  # A list to store chapter names
        question_list = []  # A list to store the total number of questions available for each chapter
        total_weight = 0  # A variable to store the total weight of selected chapters
        output = ''  # A string to store the formatted output of chapter weightage
        try:
            for i in range(chapters):
                while True:
                    try:
                        chapter_name = input("Enter the name of the chapter or enter 'b' to go back: ")
                        if chapter_name == 'b':
                            main()
                        elif chapter_name in chapter_percentages:
                            break
                        else:
                            raise ValueError("Chapter not found. Enter a valid chapter name.")
                    except ValueError as e:
                        print(f"Error: {e}")
            
                num_questions = int(input(f"Enter the total number of questions available to you for {chapter_name}: "))
                total_weight = total_weight + chapter_percentages.get(chapter_name, 0)
                name_list.append(chapter_name)
                question_list.append(num_questions)

            for j in range(chapters):
                question_num_final_value = round(chapter_percentages.get(name_list[j], 0) / total_weight * custom_question_no)
                final = " ".join(get_question_nums(question_num_final_value, question_list[j]))
                output = f"{name_list[j]} {question_list[j]}\n {final}\n"
                print()
                print(output)
                print()
                print("or " + str(counter) + " questions")   
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid number.")
        except Exception as e:
            print(f"Error: {e}. Please try again.")
        
        repeat = input("Do you want to repeat the process for the same subject? (yes/no): ").lower()
        if repeat == 'no':
                main()
        elif repeat == 'yes':
                continue     

def main():
    """
    Main program to interact with the user and execute functionalities.

    Raises:
    - FileNotFoundError: If the specified CSV file is not found during directory change.
    - ValueError: If there is an issue with user input or calculations.
    """
    saved_paths = {
        'Jee adv Phy': r"C:\Users\Seaking!!!\Desktop\python projects\jee_adv_physics.csv",
        'Jee adv Math': r"C:\Users\Seaking!!!\Desktop\python projects\jee_adv_math.csv",
        'Jee adv Chem': r"C:\Users\Seaking!!!\Desktop\python projects\jee_adv_chem.csv",
        'Jee mains Math': r"C:\Users\Seaking!!!\Desktop\python projects\jee_mains_math.csv",
        'Jee mains Chem': r"C:\Users\Seaking!!!\Desktop\python projects\Jee_mains_chem.csv",
        # Add more saved paths as needed
    }

    while True:
        print("Choose an option:")
        print("1. Choose from saved paths")
        print("2. Add a new file path")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            print("Saved file paths:")
            for key, value in saved_paths.items():
                print(f"{key}: {value}")

            selected_path_key = input(r"Choose a saved path (enter the key) or enter 'b' to go back: ")
            if selected_path_key == 'b':
                continue

            csv_file_path = saved_paths.get(selected_path_key, None)

            if csv_file_path is None:
                print("Invalid choice. Try again.")
                continue
        elif choice == '2':
            while True:
                try:
                    csv_file_path = input("Enter the path to the CSV file or enter 'b' to go back: ").strip('"')
                    if csv_file_path == 'b':
                        main()
                    directory_changer(csv_file_path)  # Attempt to change directory to check if the file exists
                    break  # Break the loop if the file path is valid
                except FileNotFoundError:
                    print("Error: File not found. Make sure the file path is correct.")
                except Exception as e:
                    print(f"Error: {e}")
        elif choice == '3':
            print("Program terminated.")
            exit()
        else:
            print("Invalid choice. Try again.")
            continue

        break

    directory_changer(csv_file_path)
    print()
    print("Showing available Chapters\n")
    for key, value in chapter_percentages.items():
        print(f"{key}: {value}%")  # Corrected the printing issue
    print()

    while True:
        reps = input("Enter the number of chapters or enter 'b' to go back: ")

        if reps == 'b':
            main()
        elif reps.isdigit():
            reps = int(reps)
            break
        else:
            print("Invalid input. Enter a valid number.")

    output = ""

    global custom_question_no
    while True:
        custom_question_no_input = input("Enter how many total questions you want to practice or enter 'b' to go back:")
        if custom_question_no_input == 'b':
            main()
        elif custom_question_no_input.isdigit():
            custom_question_no = int(custom_question_no_input)
            break
        else:
            print("Invalid input. Enter a valid number.")

    if reps == len(chapter_percentages):
        for _ in range(reps):
            while True:
                try:
                    chapter_name = input("Enter the name of the chapter or enter 'b' to go back: ")
                    if chapter_name == 'b':
                        main()
                    elif chapter_name in chapter_percentages:
                        break
                    else:
                        raise ValueError("Chapter not found. Enter a valid chapter name.")
                except ValueError as e:
                    print(f"Error: {e}")

            num_questions = int(input(f"Enter the number of questions available for {chapter_name}: "))
            num_weighed = get_no_of_questions(chapter_name, custom_question_no)
            final_question_nums = " ".join(get_question_nums(num_weighed, num_questions))
            output += f"{chapter_name} {num_questions} {final_question_nums}\n"
        print(output)
    else:
        relative_weightage(reps)

    repeat_program = input("Do you want to repeat the program? (yes/no): ").lower()
    if repeat_program == 'yes':
        main()
    else:
        print("Program terminated.")

if __name__ == "__main__":
    main()
