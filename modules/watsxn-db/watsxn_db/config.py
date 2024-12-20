# -*- coding: utf-8 -*-
#
# This file is part of the Watsxn DB Flask extension.
# (C) 2024 tom96da.com

""" watsxn_db.config module """

SQLALCHEMY_DATABASE_URI="postgresql://tom96da:dbpass@postgres:5432/tom96da_dev"

SQLALCHEMY_TRACK_MODIFICATIONS=False

SQLALCHEMY_ECHO=False

WATSXN_DB_PARAMS = {
    'dbname': 'postgres',
    'user': 'tom96da',
    'password': 'dbpass',
    'host': 'postgres',
    'port': '5432'
}
