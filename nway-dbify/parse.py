# Copyright 2013 Mitchell Stanton-Cook Licensed under the
#     Educational Community License, Version 2.0 (the "License"); you may
#     not use this file except in compliance with the License. You may
#     obtain a copy of the License at
#
#      http://www.osedu.org/licenses/ECL-2.0
#
#     Unless required by applicable law or agreed to in writing,
#     software distributed under the License is distributed on an "AS IS"
#     BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#     or implied. See the License for the specific language governing
#     permissions and limitations under the License.


import sys

def parse_nway(file_path):
    """
    Reference, position, type, base (N), evidence (N), annotations (N)
    """
    with open(file_path) as fin:
        strains = get_strains(fin.readline())
        for line in fin:
            print len(line.split('\t'))

def get_strains(line):
    """
    Returns a list of strain IDs
    """
    number_of_strains = (len(line.split('\t')[4:])-1)/3
    return line.split('\t')[4:(4+number_of_strains)]
