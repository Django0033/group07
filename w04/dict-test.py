from math import pi
from tabulate import tabulate

def main():
    can_dict = {}

    # Turn each line into a dictionary inside can_dict
    with open('./can_info.txt') as f:
        for line in f:
            line = line.strip()
            line_parts = line.split(',')
            can_dict[line_parts[0]] = {
                'name': line_parts[0],
                'radius': float(line_parts[1]),
                'height': float(line_parts[2]),
                'cost': float(line_parts[3])}

    # Computes the volume, surface area and storage efficiency for each can and
    # stores them in the respective dictionary
    for i in can_dict:
        can_dict[i]['volume'] = round(
            cilinder_volume(can_dict[i]['radius'], can_dict[i]['height']), 2)
        can_dict[i]['surface_area'] = round(
            compute_surface_area(can_dict[i]['radius'], can_dict[i]['height']) , 2)
        can_dict[i]['storage efficiency'] = round(
            can_dict[i]['volume'] / can_dict[i]['surface_area'] , 2)
    
    # Prints the table
    print(tabulate(can_dict.values(), headers='keys', tablefmt='psql'))


def cilinder_volume(radius, height):
    '''
    Computes the volume of a cilinder

    Parameters:
        radius (float): The radius of the cilinder
        height (float): The height of the cilinder

    Returns:
        float: The volume of the cilinder
    '''
    return pi * radius ** 2 * height


def compute_surface_area(radius, height):
    '''
    Computes the surface area of a cilinder

    Parameters:
        radius (float): The radius of the cilinder
        height (float): The height of the cilinder

    Returns:
        float: The surface area of the cilinder
    '''
    return 2 * pi * radius * (radius + height)


main()

# test
