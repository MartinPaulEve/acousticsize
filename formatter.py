import crayons


class Formatter:
    @staticmethod
    def print_res(method_name, output):
        print('[{0}] {1}'.format(crayons.red(method_name), output))

    @staticmethod
    def format_line(method_name, output):
        return '[{0}]: {1}'.format(crayons.red(method_name), output)
