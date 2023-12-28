import sys
from typing import List

from lib.tools import read_input

rows = read_input(sys.argv[1])


class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __repr__(self):
        return f"Range: {self.start} - {self.end}"

    def __lt__(self,other):
        return self.start < other.start


class MapEntry:
    def __init__(self, dest_start, source_start, range):
        self.dest_start = dest_start
        self.source_start = source_start
        self.range = range
        self.dest_end = dest_start + range -1
        self.source_end = source_start + range - 1

    def translate(self, source):
        diff = source - self.source_start
        return self.dest_start + diff

    def in_range(self, source):
        if source < self.source_start:
            return False
        if source > self.source_start + self.range - 1:
            return False
        return True

    def __lt__(self, other):
        return self.source_start < other.source_start
    
    def __repr__(self):
        return f"MapEntry: <{self.dest_start} - {self.dest_end}> <{self.source_start} - {self.source_end}>"


class Map:
    def __init__(self, name):
        self.entries = []
        self.name = name

    def add_map(self, map_entry):
        self.entries.append(map_entry)

    def translate(self, source):
        result = source
        for entry in self.entries:
            if entry.in_range(source):
                result = entry.translate(source)
                break
        return result

    def ranges(self, range: Range) -> List[Range]:
        result = []
        cur = range.start
        entries = sorted(self.entries)
        cur_entry = 0
        while cur < range.end and cur_entry < len(entries):
            print(f"{cur} -- {range.end}")
            entry = entries[cur_entry]

            # case 1: cur is < the start of the entry
            if range.end < entry.source_start:
                #case1a: range.end < the start of the entry
                if range.end < entry.source_start:
                    end = range.end
                #case1b: range.end >= the start of the entry
                else:
                    end = entry.source_start-1
                result.append(Range(cur, end))
                cur = end + 1
            #case 2: cur is in the range of the entry
            elif  entry.in_range(cur):
                # case 2a: range.end <= the end of the entry
                if entry.in_range(range.end):
                    end = range.end
                else:
                    end = entry.source_end
                    cur_entry +=1 
                result.append(Range(entry.translate(cur), entry.translate(end)))
                cur = end +1
            #case 3: cur is > the end of the entry 
            else:
                cur_entry +=1
        # case 3 - nothing is found
        if cur == range.start:
            result.append(Range(cur, range.end))
        return result
            
    def xrange(self):
                # case 2b: range.end > 
            
            if cur < entry.source_start:
                end = entry.source_start - 1
                
            # case 2: cur is >= the start and  <= the end
                # case 2a: range.end <= the end of the entry
                # case 2b: range.end > the end of the entry
              
            if cur  < entry.source_start + entry.range:
                cur_entry += 1
            elif entry.in_range(cur):
                start = cur
                end = cur + entry.range if cur + entry.range <= range.end else range.end
                result.append(Range(entry.translate(start), entry.translate(end)))
                print(
                    f"Adding range: {cur}, {end} -> {entry.translate(start)},  {entry.translate(end)}"
                )
                cur = end
                cur_entry += 1
            else:
                end = (
                    entry.source_end - 1
                    if entry.source_end - 1 <= range.end
                    else range.end
                )
                print(f"Adding self-range: {cur}, {end}")
                result.append(Range(cur, end))
                cur = end + 1
            return result


def print_entries(entries):
    for entry in entries:
        print(entry.dest_start, entry.source_start)


seeds = []
seeds2 = []
seed_to_soil = Map("seed-to-soil")
soil_to_fertilizer = Map("soil-to-fertilizer")
fertilizer_to_water = Map("fertlizer-to-water")
water_to_light = Map("water-to-light")
light_to_temperature = Map("light-to-temperature")
temperature_to_humidity = Map("temperature-to-humidity")
humidity_to_location = Map("humidity-to-location")


seed_range = []
for row in rows:
    row = row.strip()
    if row == "":
        continue
    parts = row.split(":")
    if parts[0] == "seeds":
        seeds = [int(x) for x in parts[1].lstrip().split(" ")]
        print(len(seeds))
        for i in range(0, len(seeds), 2):
            start = seeds[i]
            end = seeds[i + 1]
            seed_range.append(Range(start, start + end - 1))
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
        curmap.add_map(MapEntry(*[int(x) for x in row.split(" ")]))


min_location = sys.maxsize
for seed in seeds:
    location = humidity_to_location.translate(
        temperature_to_humidity.translate(
            light_to_temperature.translate(
                water_to_light.translate(
                    fertilizer_to_water.translate(
                        soil_to_fertilizer.translate(seed_to_soil.translate(seed))
                    )
                )
            )
        )
    )
    if location < min_location:
        min_location = location
print(min_location)


def get_ranges(ranges: List[Range], map: Map) -> List[Range]:
    new_ranges = []
    for range_i in ranges:
        new_ranges.extend(map.ranges(range_i))
    return new_ranges



cur_ranges = sorted(seed_range)
for map in [
    seed_to_soil,
    soil_to_fertilizer,
    fertilizer_to_water,
    water_to_light,
    light_to_temperature,
    temperature_to_humidity,
    humidity_to_location,
]:

    print(f"--------------- {map.name}-----------------")
    new_ranges = sorted(get_ranges(cur_ranges, map))
    breakpoint()
    cur_ranges = new_ranges


print(cur_ranges[0].start)

