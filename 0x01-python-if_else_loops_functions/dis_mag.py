#!/usr/bin/python3
import dis
from test import magic_calculation

code = dis.Bytecode(magic_calculation)

dis.dis(magic_calculation)

