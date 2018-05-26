import pandas as pd
from chile import data_cleaner_rules

csv_file_name = '/Users/mcarreiro/Downloads/datos_ine.csv'

headers = ['Obs','year','nui','ciiu3','region','forpro','fabval','expval','va','emptot','rempag','vstk']

df = pd.read_csv(csv_file_name, skiprows=[0], names=headers)

keys = {'expval': data_cleaner_rules.natural_cleaners,
        'fabval': data_cleaner_rules.integer_cleaners,
        'emptot': data_cleaner_rules.natural_cleaners,
        }

df = df[df.apply(lambda x: all(checker(x[key]) for key, cleaners in keys.items() for checker in cleaners) and
                      False if x['emptot'] == 0 and x['fabval'] > 0 else True and
                      x['expval'] < x['fabval']
                 , axis=1)]


table = df.pivot_table(values=('expval', 'fabval', 'rempag'), index= 'nui', columns=['year'])


tf_starter = table[table.apply(lambda x: x['expval'][2001] == 0 and x['expval'][2006] != 0, axis=1)]
tf_stopper = table[table.apply(lambda x: x['expval'][2001] != 0 and x['expval'][2006] == 0, axis=1)]
tf_cont_exporter = table[table.apply(lambda x: x['expval'][2001] != 0 and x['expval'][2006] != 0, axis=1)]
tf_cont_non_exporter = table[table.apply(lambda x: x['expval'][2001] == 0 and x['expval'][2006] == 0, axis=1)]


#By year
print(tf_starter['fabval'].mean())
print(tf_starter['rempag'].mean())

print(tf_starter['fabval'].median())
print(tf_starter['rempag'].median())

print(tf_stopper['fabval'].mean())
print(tf_stopper['rempag'].mean())

print(tf_stopper['fabval'].median())
print(tf_stopper['rempag'].median())

print(tf_cont_exporter['fabval'].mean())
print(tf_cont_exporter['rempag'].mean())

print(tf_cont_exporter['fabval'].median())
print(tf_cont_exporter['rempag'].median())

print(tf_cont_non_exporter['fabval'].mean())
print(tf_cont_non_exporter['rempag'].mean())

print(tf_cont_non_exporter['fabval'].median())
print(tf_cont_non_exporter['rempag'].median())


#sumé que no tiene sentido tener 0 empleados si fabricó
#y que haya vendido menos de lo que exportó
