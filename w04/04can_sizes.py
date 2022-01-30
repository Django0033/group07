import math

def main():
    #defines the storage efficency of 12 cans with difference volumes and surface areas
    
    can = "#1 Picnic"
    radius = 6.83
    height = 10.16
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage = volume / surface_area
    print(f"{can} {storage:.1f}")
    
    can = "#1 Tall"
    radius = 7.78
    height = 11.92
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage = volume / surface_area
    print(f"{can} {storage:.1f}")
    
    can = "#2"
    radius = 8.73
    height = 11.59
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage = volume / surface_area
    print(f"{can} {storage:.1f}")
    
    can = "#2.5"
    radius = 10.32
    height = 11.91
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage = volume / surface_area
    print(f"{can} {storage:.1f}")
    
    can = "#3 Cylinder"
    radius = 10.79
    height = 17.78
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage = volume / surface_area
    print(f"{can} {storage:.1f}")
    
    can = "#5"
    radius = 13.02
    height = 14.29
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage = volume / surface_area
    print(f"{can} {storage:.1f}")
    
    can = "#6Z"
    radius = 5.40
    height = 8.89
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage = volume / surface_area
    print(f"{can} {storage:.1f}")
    
    can = "#8Z short"
    radius = 6.83
    height = 7.62
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage = volume / surface_area
    print(f"{can} {storage:.1f}")
    
    can = "#10"
    radius = 15.72
    height = 17.78
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage = volume / surface_area
    print(f"{can} {storage:.1f}")
    
    can = "#211"
    radius = 6.83
    height = 12.38
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage = volume / surface_area
    print(f"{can} {storage:.1f}")
    
    can = "#300"
    radius = 7.62
    height = 11.27
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage = volume / surface_area
    print(f"{can} {storage:.1f}")
    
    can = "#303"
    radius = 8.10
    height = 11.11
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage = volume / surface_area
    print(f"{can} {storage:.1f}")
    
    
def compute_volume(radius, height):
    #compute the volume of a tin can
    
    volume = math.pi * (radius ** 2) * height
    return volume

def compute_surface_area(radius, height):
    #computes the surface area of a tin can
    
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area
        
main()