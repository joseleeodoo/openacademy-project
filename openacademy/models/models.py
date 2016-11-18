# -*- coding: utf-8 -*-


from odoo import models, fields, api

'''
This module is to create the Course model
'''

class Course(models.Model):
    '''
    This class creates model of Course
    '''
    _name = 'openacademy.course'

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
