import math

def main():
    print()
    list = [['#1 Picnic', 6.83, 10.16], ['#1 Tall', 7.78, 11.91], ['#2', 8.73, 11.59], ['2.5', 10.32, 11.91], ['#3 Cylinder', 10.79, 17.78], ['#5', 13.02, 14.29], ['#6Z', 5.40, 8.89], ['#8Z Short', 6.83, 7.62], ['#10', 15.72, 17.78], ['#211', 6.83, 12.38], ['#300', 7.62, 11.27], ['#303', 8.10, 11.11]]
    for i in range(len(list)):
        # for j in range(len(pineapple[i])):
        #     print(list[i][j])"
        can_radius = list[i][1]
        can_height = list[i][2]
        volume = compute_volume(can_radius, can_height)
        surface_area = compute_surface_area(can_radius, can_height)
        storage_efficiency = compute_volume(can_radius, can_height) / compute_surface_area(can_radius, can_height)
        print(f'{list[i][0]} {storage_efficiency:.2f}')
    print()

def compute_volume(radius, height):
    volume = (math.pi) * (radius ** 2) * (height)
    return volume

def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

main()