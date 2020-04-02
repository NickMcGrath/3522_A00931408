"""
A simple program that calculates the area of a room using argparse.
"""
import argparse


def setup_commandline_request():
    parser = argparse.ArgumentParser()
    # length and the width
    # positional args - length and width
    parser.add_argument("length", type=float, help="The length of a room")
    parser.add_argument("width", type=float, help="The width of the room")
    parser.add_argument("-rn", "--room_name", type=str, help="The name of "
                                                             "the room")
    parser.add_argument("-m", "--metres", action="store_true",
                        help="Is the room measurements in metres? "
                             "default: False")
    parser.add_argument("name", type=str,
                        choices=["Penelope", "Lydia", "Elena", "Max"],
                        help="The name of the user. Can be one of Peneloper," \
                             "Lydia, Elena or Max")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--b", type=str,
                       help="The type of building that is room is present "
                            "in. Either building or house type must be "
                            "specified.")
    group.add_argument("--h", type=str,
                       help="The type of house the room is present in. "
                            "Either building or house type must be "
                            "specified.")

    # This parses all the arguments passed
    # through terminal/command line
    args = parser.parse_args()
    return args


def main():
    cmd_args = setup_commandline_request()
    print(cmd_args)
    area = cmd_args.length * cmd_args.width
    print(f"Hi {cmd_args.name}")
    if cmd_args.metres:
        unit = "square metres"
    else:
        unit = "square feet"
    if cmd_args.room_name:
        print(f"{cmd_args.room_name} Area: {area} {unit}")
    else:
        print(f"Area: {area} {unit}")


if __name__ == '__main__':
    main()
