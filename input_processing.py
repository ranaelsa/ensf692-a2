# input_processing.py
# Rana Elsadig, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.

class Sensor:
    """A class used to create Sensor object.

        Attributes:
            light (str): String that represents the traffic light status
            pedestrian (str): String that represents the presence of a pedestrian
            vehicle (str): String that represents the presence of a vehicle

    """
    
    def __init__(self):
        self.light = "green"
        self.pedestrian = "no"
        self.vehicle = "no"

    # The below method updates the light, pedestrian, and vehicle status's based on the selected menu option.
    def update_status(self, menu, change): 
        """Updates the status of the sensor based on the provided menu option and change value. Prints an invalid message if change is not accepted.
        
        Args:
            menu (int): The menu option indicating which attribute to update.
            change (str): The new value to set for the selected attribute.

        Returns:
            None
        """

        # Light status change
        if menu == 1:
            if (change == "green" or change == "yellow" or change ==  "red"):
                self.light = change
            else:
                print("Invalid vision change.")
        # Pedestrian status change
        elif menu == 2:
            if (change == "yes" or change == "no"):
                self.pedestrian = change
            else:
                print("Invalid vision change.")
        # Vehicle status change
        elif menu == 3:
            if (change == "yes" or change == "no"):        
                self.vehicle = change
            else:
                print("Invalid vision change.")

# The sensor object is passed to this function to print the action message and current status.
def print_message(sensor):
    """Prints an action message and the current status of the sensor.

    Args:
        sensor (Sensor): The sensor object whose status is to be evaluated and printed.

    Returns:
        None
    """

    # If the light status is red, or a pedestrian or vehicle is present, the message is "STOP"
    if (sensor.light == "red" or sensor.pedestrian == "yes" or sensor.vehicle == "yes"):
        print("STOP")
    # If the light is green, and no pedestrian and vehicle are present, the message is "proceed"
    elif (sensor.light == "green" and sensor.pedestrian == "no" and sensor.vehicle == "no"):
        print("Proceed")
    # If the light is yellow, the message is "CAUTION"
    elif (sensor.light == "yellow" and sensor.pedestrian == "no" and sensor.vehicle == "no"):
        print("Caution")
    print("") 
    print("Light = " + sensor.light + " , Pedestrian: " + sensor.pedestrian + " , Vehicle: " + sensor.vehicle + " . ")

# The main function will initialize a Sensor object and continuosly promt the user for a change through a while block.
def main():
    """Main function to run the Car Vision Detector Processing Program.

    Initializes a Sensor object and prompts the user for changes in sensor input,
    updating the sensor status and printing appropriate messages based on user input.

    Returns:
        None
    """

    sensor = Sensor()
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    while(True):
        # A try except block is used to test for and handle errors in menu selection
        try: 
            print("")
            print("Are changes detected in the vision input?")
            menu = int(input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: "))
            # If the users input is not 0, 1, 2, or 3, a ValueError is raised.
            if (menu != 0 and menu != 1 and menu != 2 and menu != 3):
                raise ValueError("must enter 0, 1, 2, or 3")
        except ValueError:
            print("You must select either 1, 2, 3, or 0")
        else:
            # If 0 is selected, the program stops.
            if menu == 0:
                break
            # If 1, 2, or 3 is is selected the function calls on the sensors instance method to update the light, pedestrian, or vehicle status.
            # The print_message funcion is then called to print the action message and current status.
            else:
                change = input("What change has been identified?: ")
                sensor.update_status(menu, change)
                print("")
                print_message(sensor)

# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

