#!/usr/bin/env python3

from sqlalchemy import create_engine

from lib.test import Student

engine = create_engine('sqlite:///students.db')

if __name__ == '__main__':
    import ipdb; ipdb.set_trace()
