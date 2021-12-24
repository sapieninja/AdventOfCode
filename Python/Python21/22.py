import aoc_utils

lines = aoc_utils.readlines()
regions = []


def sizeof(region):
    xmin, xmax, ymin, ymax, zmin, zmax = region
    return (1 + xmax - xmin) * (1 + ymax - ymin) * (1 + zmax - zmin)


def intersection(cubea, cubeb):
    xmin, xmax, ymin, ymax, zmin, zmax = cubea
    xmin2, xmax2, ymin2, ymax2, zmin2, zmax2 = cubeb
    newxmin, newxmax, newymin, newymax, newzmin, newzmax = 0, 0, 0, 0, 0, 0
    if (
        xmin > xmax2
        or ymin > ymax2
        or zmin > zmax2
        or xmin2 > xmax
        or ymin2 > ymax
        or zmin2 > zmax
    ):
        return False
    else:
        newxmin = max(xmin, xmin2)
        newymin = max(ymin, ymin2)
        newzmin = max(zmin, zmin2)
        newxmax = min(xmax, xmax2)
        newymax = min(ymax, ymax2)
        newzmax = min(zmax, zmax2)
    return newxmin, newxmax, newymin, newymax, newzmin, newzmax


for line in lines:
    line = line.split()
    status = line[0]
    line = line[1].split(",")
    for part in range(len(line)):
        line[part] = line[part][2:].split("..")
    xmin = int(line[0][0])
    xmax = int(line[0][1])
    ymin = int(line[1][0])
    ymax = int(line[1][1])
    zmin = int(line[2][0])
    zmax = int(line[2][1])
    for i in range(len(regions)):
        intersect = intersection(
            (xmin, xmax, ymin, ymax, zmin, zmax), regions[i][1]
        )
        if intersect == False:
            continue
        else:
            if regions[i][0] == "on":
                regions.append(["off", intersect])
            if regions[i][0] == "off":
                regions.append(["on", intersect])
    if status == "on":
        regions.append([status, (xmin, xmax, ymin, ymax, zmin, zmax)])

nocubes = 0
for region in regions:
    if region[0] == "on":
        nocubes += sizeof(region[1])
    if region[0] == "off":
        nocubes -= sizeof(region[1])
print(nocubes)
