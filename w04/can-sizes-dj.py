from math import pi


def main():
    can_name_lst = []
    can_radius_lst = []
    can_height_lst = []
    can_volume_lst = []
    can_surface_area_lst = []
    storage_efficiency_lst = []

    # Takes info from the can_info.txt and populates can name, radius and height
    # lists
    with open('can_info.txt') as f:
        for line in f:
            line = line.strip()
            line_parts = line.split(',')
            can_name_lst.append(line_parts[0].strip())
            can_radius_lst.append(float(line_parts[1].strip()))
            can_height_lst.append(float(line_parts[2].strip()))

    # Computes the volume and surface area of each can and stores them in the
    # volume and surface area lists
    for i in range(len(can_name_lst)):
        can_volume_lst.append(compute_volume_cilinder(
            can_radius_lst[i], can_height_lst[i]))
        can_surface_area_lst.append(compute_surface_area_cilinder(
            can_radius_lst[i], can_height_lst[i]))
        storage_efficiency_lst.append(
            can_volume_lst[i] / can_surface_area_lst[i])

    # Prints the headers for the table
    print('{:<12} {:<9} {:<9} {:<9} {:<12} {:<9}'.format(
        'Name', 'Radius', 'Height', 'Volume', 'Surface Area', 'Storage Efficiency'))

    # Prints the table
    for i in range(len(can_name_lst)):
        print('{:<12} {:<9.2f} {:<9.2f} {:<9.2f} {:<12.2f} {:<9.2f}'.format(
            can_name_lst[i], can_radius_lst[i], can_height_lst[i], can_volume_lst[i], can_surface_area_lst[i], storage_efficiency_lst[i]))


def compute_volume_cilinder(radius, height):
    '''
    Computes the volume of a cilinder

    Parameters:
        radius (float): radius of the cilinder
        height (float): height of the cilinder

    Returns:
        volume (float): volume of the cilinder
    '''
    return pi * radius ** 2 * height


def compute_surface_area_cilinder(radius, height):
    '''
    Computes the surface area of a cilinder

    Parameters:
        radius (float): radius of the cilinder
        height (float): height of the cilinder

    Returns:
        surface_area (float): surface area of the cilinder
    '''
    return 2 * pi * radius * (radius + height)


main()
