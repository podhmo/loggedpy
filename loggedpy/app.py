from loggedpy import (
    get_flavor,
    run,
)


def main():
    import argparse
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("filepath", nargs="?")
    parser.add_argument("-m", "--python-module")
    parser.add_argument("--flavor", default=":Flavor")
    args, extras = parser.parse_known_args()

    if args.filepath is None and args.python_module is None:
        return parser.print_help()
    flavor = get_flavor(args.flavor)

    run(flavor, filepath=args.filepath, python_module=args.python_module, args=extras)
