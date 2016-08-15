#!/usr/bin/env python3
import yaml
import sys


def read_hosts_from_yaml(filename):
    with open(filename, 'r') as yamlfile:
        return yaml.load(yamlfile)['hosts']


def generate_dns_line_from_record(record, value):
    try:
        ip = value.get('ip')
        cname = value.get('cname')
    except AttributeError:
        # Empty string is safer than printing None
        return ""
    if ip:
        target = "A {}".format(ip)
    elif cname:
        target = "CNAME {}.".format(cname)
    else:
        # Empty string is safer than printing None
        return ""
    return "{} {}".format(record, target)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} FILENAME".format(sys.argv[0]))
        sys.exit(1)
    filename = sys.argv[1]
    data = read_hosts_from_yaml(filename)
    for key, value in data.items():
        print(generate_dns_line_from_record(key, value))
