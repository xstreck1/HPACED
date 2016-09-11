# Highest Peak Aligment for Capilary Electrophoresis Data
# Dr. Adam Streck 2016
# adam.streck@gmail.com

import os
import argparse


def read_data(datafile):
    result = []
    line_no = 1
    for line in datafile:
        line_data = [float(x) for x in str.split(line)]
        if len(line_data) != 2:
            raise Exception("invalid number of objects on the line " + str(line_no) + " expecting 2 values, got " + line + " instead")
        result.append(line_data)
        line_no += 1
    return result


def write_data(datafile, data):
    for line in data:
        if line[0] < 0:
            continue
        else:
            datafile.write(str(line[0]) + "\t" + str(line[1]) + "\n")


def find_highest_peak(data, delay):
    highest = [0, 0]
    for line in data:
        if line[0] <= delay:
            continue
        elif line[1] > highest[1]:
            highest = line
    return highest


def shift_time_by(data, shift):
    for line in data:
        line[0] += shift

if __name__ == "__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     description="Used to align the timeline of datafiles "
                                                 "based on the highest peak found after a certain timepoint.")
    parser.add_argument("template", help="the name of the file found in the location based on which the files are aligned")
    parser.add_argument("--timepoint", type=float, default=0.0, help="ignores the data up till the timepoint (inclusive)")
    parser.add_argument("--location", default=".", help="a path in the filesystem to where the data are stores")
    parser.add_argument("--output", default="./HPACED_OUT", help="a path relative to the location where the results are to be stored")
    parser.add_argument("--extension", help="if set, only the files with the extension (e.g. .xy) are considered, if not, all files found in the location are tested")

    args = parser.parse_args()

    if not os.path.exists(args.location):
        raise Exception(args.location + " is not a directory")

    template_path = args.template
    if not os.path.exists(template_path):
        template_path = os.path.join(args.location, template_path)
        if not os.path.exists(template_path):
            raise Exception("did not find the template in " + template_path + " or " + args.template)

    output_dir_path = os.path.join(args.location, args.output)
    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path)

    files = [f for f in os.listdir(args.location) if
             os.path.isfile(os.path.join(args.location, f)) and (not args.extension or f.endswith(args.extension))]

    with open(template_path, "r") as file:
        template_peak = find_highest_peak(read_data(file), args.timepoint)
        print("the template file at " + template_path + " has the peak of" +
              str(template_peak[1]) + " at the time " + str(template_peak[0]))

    for f in files:
        with open(os.path.join(args.location, f), "r") as file:
            content = read_data(file)
            file_peak = find_highest_peak(content, args.timepoint)
            print("file " + f + " has the peak of " + str(file_peak[1]) + " shifted by " + str(file_peak[0] - template_peak[0]))
            shift_time_by(content, template_peak[0] - file_peak[0])

        with open(os.path.join(output_dir_path, f), "w+") as file:
            write_data(file, content)

