
output_file = "dissipation-data-eta-0-5-eta-1-2-10-5-optimized-0.csv"
writer = open(output_file, 'w')

stuff_to_write_to_the_file = '''

Product, Price\n
Chicken, 2.60\n
Celery,  2.99\n
'''

writer.write(stuff_to_write_to_the_file)
writer.close()
