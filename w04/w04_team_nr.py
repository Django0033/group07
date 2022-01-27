import math

#storage_efficiency = volume / surface_area
#volume = pi(radius**2)height
#surface_area = 2piradius(radius + height)

def main():
    
    # with open("can_info.txt") as can_info:
    #     for line in can_info:
    #         clean_line = line.strip()
    #         parts = clean_line.split(",")

    #         name = parts[0]
    #         radius = parts[1]
    #         height = parts[2]
    #         cost = parts[3]
   
    number1a = compute_volume(6.83, 10.16)
    number1b = compute_surface_area(6.83, 10.16)
    print(f"1 Picnic:\t {number1a / number1b:.1f} ")

    number2a = compute_volume(7.78, 11.91)
    number2b = compute_surface_area(7.78, 11.91)
    print(f"1 Tall:\t {number2a / number2b:.1f}")

    number3a = compute_volume(8.73, 11.59)
    number3b = compute_surface_area(8.73, 11.59)
    print(f"2:\t {number3a / number3b:.1f}")

    number4a = compute_volume(10.32, 11.91)
    number4b = compute_surface_area(10.32, 11.91)
    print(f"2.5:\t {number4a / number4b:.1f}")

    number5a = compute_volume(10.79, 17.78)
    number5b = compute_surface_area(10.79, 17.78)
    print(f"3 Cylinder:\t {number5a / number5b:.1f}")
    
    number6a = compute_volume(13.02, 14.29)
    number6b = compute_surface_area(13.02, 14.29)
    print(f"5:\t {number6a / number6b:.1f}")

    number7a = compute_volume(5.40, 8.89)
    number7b = compute_surface_area(5.40, 8.89)
    print(f"6Z:\t {number7a / number7b:.1f}")

    number8a = compute_volume(6.83, 7.62)
    number8b = compute_surface_area(6.83, 7.62)
    print(f"8Z short:\t {number8a / number8b:.1f}")

    number9a = compute_volume(15.72, 17.78)
    number9b = compute_surface_area(15.72, 17.78)
    print(f"10:\t {number9a / number9b:.1f}")
    
    number10a = compute_volume(6.83, 12.38)
    number10b = compute_surface_area(6.83, 12.38)
    print(f"211:\t {number10a / number10b:.1f}")
    
    number11a = compute_volume(7.62, 11.27)
    number11b = compute_surface_area(7.62, 11.27)
    print(f"300:\t {number11a / number11b:.1f}")

    number12a = compute_volume(8.10, 11.11)
    number12b = compute_surface_area(8.10, 11.11)
    print(f"303:\t {number12a / number12b:.1f}")

    # print(f'{name} {storage_efficiency:.1f} ')


def compute_volume(radius, height):

    volume = math.pi * radius ** 2 * height
    return volume


def compute_surface_area(radius, height):
    
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area


main()