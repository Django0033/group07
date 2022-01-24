from math import pi


def main():
    can_name_lst = []
    can_radius_lst = []
    can_height_lst = []
    can_cost_lst = []
    storage_efficiency_lst = []
    cost_efficiency_lst = []

    # Takes info from the can_info.txt and populates can name, radius and height
    # lists
    with open('can_info.txt') as f:
        for line in f:
            line = line.strip()
            line_parts = line.split(',')
            can_name_lst.append(line_parts[0].strip())
            can_radius_lst.append(float(line_parts[1].strip()))
            can_height_lst.append(float(line_parts[2].strip()))
            can_cost_lst.append(float(line_parts[3].strip()))

    # Computes the storage efficiency and cost efficiency for each can and appends it to the
    # storage_efficiency_lst and cost_efficiency_lst lists
    for i in range(len(can_name_lst)):
        storage_efficiency_lst.append(compute_storage_efficiency(
            can_radius_lst[i], can_height_lst[i]))
        cost_efficiency_lst.append(compute_cost_efficiency(
            can_radius_lst[i], can_height_lst[i], can_cost_lst[i]))

    # Gets the index of the best storage efficiency and cost efficiency
    best_storage_efficiency_index = storage_efficiency_lst.index(max(storage_efficiency_lst))
    best_cost_efficiency_index = cost_efficiency_lst.index(max(cost_efficiency_lst))

    # Prints the headers for the table
    print('\n{:<12} {:<9} {:<9} {:<18} {:<12}'.format(
        'Name', 'Radius', 'Height', 'Storage Efficiency', 'Cost Efficiency'))

    # Prints the table
    for i in range(len(can_name_lst)):
        print('{:<12} {:<9.2f} {:<9.2f} {:<18.2f} {:<12.2f}'.format(
            can_name_lst[i], can_radius_lst[i], can_height_lst[i], storage_efficiency_lst[i], cost_efficiency_lst[i]))
    
    # Prints the best storage efficiency and cost efficiency
    print('\n{} has the best storage efficiency with {:.2f}'.format(
        can_name_lst[best_storage_efficiency_index], max(storage_efficiency_lst)))
    print('{} has the best cost efficiency with {:.2f}'.format(
        can_name_lst[best_cost_efficiency_index], max(cost_efficiency_lst)))


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


def compute_storage_efficiency(radius, height):
    '''
    Computes the storage efficiency of a cilinder using the compute_volume_cilinder
    and compute_surface_area_cilinder functions

    Parameters:
        radius (float): radius of the cilinder
        height (float): height of the cilinder

    Returns:
        storage_efficiency (float): storage efficiency of the cilinder
    '''
    return compute_volume_cilinder(radius, height) / compute_surface_area_cilinder(radius, height)


def compute_cost_efficiency(radius, height, cost):
    '''
    Computes the cost efficiency of a cilinder using the compute_volume_cilinder

    Parameters:
        radius (float): radius of the cilinder
        height (float): height of the cilinder
        cost (float): cost of the cilinder

    Returns:
        cost_efficiency (float): cost efficiency of the cilinder
    '''
    return compute_volume_cilinder(radius, height) / cost


main()
