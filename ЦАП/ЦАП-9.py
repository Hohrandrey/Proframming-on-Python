import re

def main(input_str):
    pattern = r'<sect>\s*set\s*#(-?\d+)\s*==>\s*(\w+)\s*</sect>'
    matches = re.findall(pattern, input_str)
    return [(name, int(num)) for num, name in matches]