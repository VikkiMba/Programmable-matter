import pandas

#%matplotlib inline

pandas.set_option('max_columns', 10)
df = pandas.read_csv('bubble_chart_one.csv')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
plt.scatter(x=df['Extension'],
            y=df['Force'],
            s=df['Force'] * 3,alpha=0.5,
            c=df['Bubble colour'])
            
plt.xlabel('Extension')
plt.ylabel('Force')
plt.title('Improvement on mechanical properties of recycled Aluminium scrap drink cans ')
x,y = df['Extension'], df['Force']

for i, txt in enumerate(df['Composition_and_Temperature']):   
    plt.annotate(txt, (x[i], y[i]))
    print(i, txt, x[i], y[i], df['Force'][i], df['Bubble colour'][i])
comp_temlst = list(df['Composition_and_Temperature'])
Bubble_colour_list = list(df['Bubble colour'])

l = []
for i in range(0,len(df.index)):
    l.append(mpatches.Patch(color=Bubble_colour_list[i],
                            alpha=0.5,
                            label=comp_temlst[i]))
                        
plt.legend(handles=l, loc=(1, 0))
plt.subplots_adjust(hspace=0.5, wspace=0.05)
plt.show()