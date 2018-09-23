from loggedpy import (
    get_driver,
    run,
)


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", nargs="?")
    parser.add_argument("-m", "--python-module")
    parser.add_argument("--loggedpy-driver", default=":Driver")
    args, extras = parser.parse_known_args()

    if args.filepath is None and args.python_module is None:
        return parser.print_help()
    driver = get_driver(args.loggedpy_driver)

    run(driver, filepath=args.filepath, python_module=args.python_module, args=extras)
