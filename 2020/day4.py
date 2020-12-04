day = 4

###############################
import re
from read_input import *

input_string = get_input_string(day).strip()
# input_string = read_file('test.txt').strip()


def count_valid(input_string, validate_func):
    return sum(
        validate_func({
            key: value for key, value in (
                field.split(':') for field in re.split(r' |\n', passport)
            )
        }) for passport in input_string.split('\n\n'))


# Part One
def rule1(fields):
    fields['cid'] = fields.get('cid', None)
    return len(fields) == 8


# Part Two
def rule2(fields):
    fields['cid'] = fields.get('cid', None)
    try:
        assert len(fields) == 8

        # Birth Year
        assert len(fields['byr']) == 4
        assert 1920 <= int(fields['byr']) <= 2002

        # Issue Year
        assert len(fields['iyr']) == 4
        assert 2010 <= int(fields['iyr']) <= 2020

        # Expiration Year
        assert len(fields['eyr']) == 4
        assert 2020 <= int(fields['eyr']) <= 2030

        # Height
        if  fields['hgt'][-2:] == 'cm':
            assert 150 <= int(fields['hgt'][:-2]) <= 193
        elif fields['hgt'][-2:] == 'in':
            assert 59 <= int(fields['hgt'][:-2]) <= 76
        else:
            raise AssertionError

        # Hair Clor
        assert re.fullmatch(r'#[0-9a-f]{6}', fields['hcl'])

        # Eye Color
        assert fields['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')

        # Passport ID
        assert re.fullmatch(r'\d{9}', fields['pid'])

    except AssertionError:
        return False
    except KeyError:
        return False
    return True


if __name__ == '__main__':
    print(count_valid(input_string, rule1))
    print(count_valid(input_string, rule2))
