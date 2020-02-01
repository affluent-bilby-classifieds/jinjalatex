#!/usr/bin/python3
import jinja2
import os
import MySQLdb


connection = MySQLdb.connect("localhost","test","password")
cursor = connection.cursor()


# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")
# Fetch a single row using fetchone() method.
data = cursor.fetchone()[0]
cursor.close()
connection.close()

from jinja2 import Template
latex_jinja_env = jinja2.Environment(
	block_start_string = '\BLOCK{',
	block_end_string = '}',
	variable_start_string = '\VAR{',
	variable_end_string = '}',
	comment_start_string = '\#{',
	comment_end_string = '}',
	line_statement_prefix = '%%',
	line_comment_prefix = '%#',
	trim_blocks = True,
	autoescape = False,
	loader = jinja2.FileSystemLoader(os.path.abspath('.'))
)

template = latex_jinja_env.get_template('test2.template')

print(template.render(section1='Long Form', section2='Short Form', section3='tcolorbox', section4="SQL query : %s " % data, section5='SQL query inside tcolorbox', section6='QR code', section7='pst-barcode Micro QR code',section8='attempt to render child template',my_string='Wheeeee!', my_list=[0,1,2,3,4,5], data1=data, section9='Another tcolorbox example with SQL query.', section10='SQL, tcolorbox, microQR code', section11='Screenshot of example classified ad'))





