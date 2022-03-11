# Import the csv module so that it can be used
# to read from the accidents.csv file.
import csv


# Column numbers from the accidents.csv file.
YEAR_COLUMN = 0
FATALITIES_COLUMN = 1
INJURIES_COLUMN = 2
CRASHES_COLUMN = 3
FATAL_CRASHES_COLUMN = 4
DISTRACT_COLUMN = 5
PHONE_COLUMN = 6
SPEED_COLUMN = 7
DUI_COLUMN = 8
FATIGUE_COLUMN = 9


def main():
    try:
        # Prompt the user for a filename and open that text file.
        filename = input("Name of file that contains NHTSA data: ")
        with open(filename, "rt") as text_file:
            while True:
                try:
                    # Prompt the user for a percentage.
                    perc_reduc = float(input(
                        "Percent reduction of texting while driving [0, 100]: "))
                    if perc_reduc < 0:
                        print('Percent reduction must be greater than 0.')
                        print('Please enter a valid number.')
                    elif perc_reduc > 100:
                        print('Percent reduction must be less than 100.')
                        print('Please enter a valid number.')
                    else:
                        print()
                        print(f"With a {perc_reduc}% reduction in using a cell",
                            "phone while driving, approximately this",
                            "number of injuries and deaths would have",
                            "been prevented in the USA.", sep="\n")
                        print()
                        print("Year, Injuries, Deaths")

                        # Use the csv module to create a reader
                        # object that will read from the opened file.
                        reader = csv.reader(text_file)

                        # The first line of the CSV file contains column headings
                        # and not a student's I-Number and name, so this statement
                        # skips the first line of the CSV file.
                        next(reader)

                        # Process each row in the CSV file.
                        for row in reader:
                            year = row[YEAR_COLUMN]

                            # Call the estimate_reduction function.
                            try:
                                injur, fatal = estimate_reduction(
                                        row, PHONE_COLUMN, perc_reduc)
                            except:
                                break


                            # Print the estimated reductions
                            # in injuries and fatalities.
                            print(year, injur, fatal, sep=", ")
                        break

                except ValueError:
                    print('The percentage must be a number between 0 and 100.')
                    print('Please enter a valid number.')

    except FileNotFoundError:
        print('The file {} does not exist.'.format(filename))
        print('Please run this program again and enter a valid filename.')

    except PermissionError:
        print('The file {} is not accessible.'.format(filename))
        print('Please run this program again and enter a valid filename.')
    

def estimate_reduction(row, behavior_key, perc_reduc):
    """Estimate and return the number of injuries and deaths that would
    not have occurred on U.S. roads and highways if drivers had reduced
    a dangerous behavior by a given percentage.

    Parameters
        row: a CSV row of data from the U.S. National Highway Traffic
            Safety Administration (NHTSA)
        behavior_key: heading from the CSV file for the dangerous
            behavior that drivers could reduce
        perc_reduc: percent that drivers could reduce a dangerous
            behavior
    Return: The number of injuries and deaths that may have been
        prevented
    """
    behavior = int(row[behavior_key])
    fatal_crashes = int(row[FATAL_CRASHES_COLUMN])

    try:
        ratio = perc_reduc / 100 * behavior / fatal_crashes
        fatalities = int(row[FATALITIES_COLUMN])
        injuries = int(row[INJURIES_COLUMN])

        reduc_fatal = int(round(fatalities * ratio, 0))
        reduc_injur = int(round(injuries * ratio, 0))
        return reduc_injur, reduc_fatal
    except ZeroDivisionError:
        with open('accidents.csv', 'rt') as accidents_csv:
            reader = csv.reader(accidents_csv)
            next(reader)
            row_number = 1
            for row in reader:
                if row[FATAL_CRASHES_COLUMN] == '0':
                    print('The fatal crashes column contains 0.')
                    print('Please enter a valid number.')
                    print('Row number:', row_number)
                    break
                row_number += 1



# If this file was executed like this:
# > python accidents.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
