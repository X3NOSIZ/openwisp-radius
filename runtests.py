#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, "tests")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

if __name__ == "__main__":
    from django3.core.management import execute_from_command_line
    args = sys.argv
    args.insert(1, "test")
    args.insert(2, "openwisp_radius")
    execute_from_command_line(args)
