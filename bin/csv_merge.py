#!/usr/bin/env python3
#    Merge CSV files
#    Copyright (C) 2018  Neptune Nyx Nishedcob
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import json
import csv
import sys


def main():
    parser = argparse.ArgumentParser(description='''
    NUX-BIN:csv_merge.py  Copyright (C) 2018  Neptune Nyx Nishedcob
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions.

    Combine CSV files.
    ''')
    parser.add_argument('-u', '--unique', action='store_true', help='Enforce uniqueness in merged CSV')
    parser.add_argument('input.csv', nargs='+', help='CSV file(s) to merge')
    parser.add_argument('output.csv', action='store', help='Merged CSV Output')
    args = parser.parse_args()

    data = []

    args = vars(args)

    for input_file in args.get('input.csv', []):
        with open(input_file) as input_fp:
            csv_reader = csv.DictReader(input_fp)
            data += [row for row in csv_reader]

    if args.get('unique', False):
        data = list(
            map(
                lambda row: json.loads(row),
                {
                    json.dumps(row)
                    for row in data
                }
            )
        )

    columns = {
        key
        for row in data
            for key, _ in row.items()
    }

    data = [
        {
            key: row.get(key, '')
            for key in columns
        }
        for row in data
    ]

    with open(args.get('output.csv', sys.stdout), 'w') as output_fp:
        csv_writer = csv.DictWriter(output_fp, fieldnames=list(columns))

        csv_writer.writeheader()

        list(
            map(
                lambda row: csv_writer.writerow(row),
                data
            )
        )


if __name__ == '__main__':
    main()
