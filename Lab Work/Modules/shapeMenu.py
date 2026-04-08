import shapes

while True:
    # main menu
    print("\nSelect a shape:")
    print("1. Cube")
    print("2. Cuboid")
    print("3. Cylinder")
    print("4. Cone")
    print("5. Sphere")
    print("6. Hemisphere")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    if choice == 7:
        print("Exiting...")
        break

    # operation menu
    print("\nChoose operation:")
    print("1. Curved Surface Area")
    print("2. Total Surface Area")
    print("3. Volume")

    op = int(input("Enter operation: "))

    # ---- Cube ----
    if choice == 1:
        a = float(input("Enter side: "))
        if op == 1:
            print("CSA =", shapes.cube_csa(a))
        elif op == 2:
            print("TSA =", shapes.cube_tsa(a))
        elif op == 3:
            print("Volume =", shapes.cube_volume(a))

    # ---- Cuboid ----
    elif choice == 2:
        l = float(input("Length: "))
        b = float(input("Breadth: "))
        h = float(input("Height: "))
        if op == 1:
            print("CSA =", shapes.cuboid_csa(l, b, h))
        elif op == 2:
            print("TSA =", shapes.cuboid_tsa(l, b, h))
        elif op == 3:
            print("Volume =", shapes.cuboid_volume(l, b, h))

    # ---- Cylinder ----
    elif choice == 3:
        r = float(input("Radius: "))
        h = float(input("Height: "))
        if op == 1:
            print("CSA =", shapes.cylinder_csa(r, h))
        elif op == 2:
            print("TSA =", shapes.cylinder_tsa(r, h))
        elif op == 3:
            print("Volume =", shapes.cylinder_volume(r, h))

    # ---- Cone ----
    elif choice == 4:
        r = float(input("Radius: "))
        if op == 3:
            h = float(input("Height: "))
            print("Volume =", shapes.cone_volume(r, h))
        else:
            l = float(input("Slant height: "))
            if op == 1:
                print("CSA =", shapes.cone_csa(r, l))
            elif op == 2:
                print("TSA =", shapes.cone_tsa(r, l))

    # ---- Sphere ----
    elif choice == 5:
        r = float(input("Radius: "))
        if op == 1:
            print("CSA =", shapes.sphere_csa(r))
        elif op == 2:
            print("TSA =", shapes.sphere_tsa(r))
        elif op == 3:
            print("Volume =", shapes.sphere_volume(r))

    # ---- Hemisphere ----
    elif choice == 6:
        r = float(input("Radius: "))
        if op == 1:
            print("CSA =", shapes.hemisphere_csa(r))
        elif op == 2:
            print("TSA =", shapes.hemisphere_tsa(r))
        elif op == 3:
            print("Volume =", shapes.hemisphere_volume(r))

    else:
        print("Invalid choice")