import sys 

from lib.tools import read_input

rows = read_input(sys.argv[1])


class MapEntry:
    def __init__(self, dest_start, source_start, range):
        self.dest_start = dest_start
        self.source_start = source_start
        self.range = range

    def translate(self, source):
        diff = source - self.source_start
        return self.dest_start + diff

    def in_range(self, source):
        if source < self.source_start:
            return False
        if source > self.source_start + self.range - 1:
            return False
        return True

class Map:
    def __init__(self):
        self.entries = []

    def add_map(self, map_entry):
        self.entries.append(map_entry)

    def translate(self, source):
        result = source
        for entry in self.entries:
            if entry.in_range(source):
                result = entry.translate(source)
                break
        return result


seeds = []
seed_to_soil = Map()
soil_to_fertilizer = Map()
fertilizer_to_water = Map()
water_to_light = Map()
light_to_temperature = Map()
temperature_to_humidity= Map()
humidity_to_location = Map()



for row in rows:
    row = row.strip()
    if row == '':
        continue
    parts = row.split(":")
    if parts[0] == "seeds":
        seeds = [int(x) for x in parts[1].lstrip().split(' ')]
        print(f"seeds: {seeds}")
    elif parts[0] == "seed-to-soil map":
        curmap = seed_to_soil
    elif parts[0] == "soil-to-fertilizer map":
        curmap = soil_to_fertilizer
    elif parts[0] == "fertilizer-to-water map":
        curmap = fertilizer_to_water
    elif parts[0] == "water-to-light map":
        curmap = water_to_light
    elif parts[0] == "light-to-temperature map":
        curmap = light_to_temperature
    elif parts[0] == "temperature-to-humidity map":
        curmap = temperature_to_humidity
    elif parts[0] == "humidity-to-location map":
        curmap = humidity_to_location
    else:
        curmap.add_map(MapEntry(*[int(x) for x in row.split(' ')]))


min_location = sys.maxsize
for seed in seeds:
    location = humidity_to_location.translate(
        temperature_to_humidity.translate(
            light_to_temperature.translate(
                water_to_light.translate(
                    fertilizer_to_water.translate(
                        soil_to_fertilizer.translate(
                             seed_to_soil.translate(
                                seed 
                             )
                        )
                    )
                )
            )
        )
    )
    if location < min_location:
        min_location = location
print(min_location)
