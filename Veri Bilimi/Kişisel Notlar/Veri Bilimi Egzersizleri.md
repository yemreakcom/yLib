---
description: Veri bilimi için bir kaç kod parçası
---

# Veri Bilimi Egzersizleri

## Dw3 - Miniprojects

```py
# Post_code göre sıralayıp, ilk post_code'u alma
unique_practices = practices.sort_values('post_code').groupby('code').first().reset_index()

# Verileri birleştirme
merged_data = scripts.merge(unique_practices[['code', 'post_code']], how='left', left_on='practice', right_on='code')

# Post_code ve bnf_name'e ait toplam items'ları hesaplama. Indeksi sıfırlama (post_code değil 0, 1, 2 ... diye olsun)
total_items_by_pc_bnf = merged_data.groupby(['post_code', 'bnf_name'])['items'].sum().reset_index()

# En yüksek `items`a sahip `post_code`ların index tablosunu alma
max_mask = total_items_by_pc_bnf.groupby('post_code')['items'].idxmax()

# Maskeden verileri alıp, `post_code`a göre sıralama ve ilk 100 veriyi alma
max_items_by_pc = total_items_by_pc_bnf.loc[max_mask].sort_values('post_code')[:100]

# `post_code` başına düşen toplam `items`ı hesaplama, indexi `post_code` yerine 0, 1, .. şekline çevirme ve `post_code`a göre sıralama
sum_items_by_pc = total_items_by_pc_bnf.groupby('post_code')['items'].sum().reset_index().sort_values('post_code')

# Toplam ve Max tablolarını setlerini birleştirme (left join)
merged_max_sum_items_by_pc = max_items_by_pc.merge(sum_items_by_pc, how="left", on='post_code')

# Toplam / Max oranını hesaplama ve sütuna atma
merged_max_sum_items_by_pc['ratio'] = merged_max_sum_items_by_pc['items_x'] / merged_max_sum_items_by_pc['items_y']

# Toplamları ve Max değerlerini kaldırma (axis=1 -> sütun'u kaldır, inplace=True -> Değişikliği uygula)
merged_max_sum_items_by_pc.drop(['items_x', 'items_y'], axis=1, inplace=True)

# Verileri listeye çevirme
items_by_region = merged_max_sum_items_by_pc.values.tolist()
```

### Dw3 Old - Mini Projects

```py
merged_data = scripts.merge(unique_practices[['code', 'post_code']], how='left', left_on='practice', right_on='code')

```py
all_data = pd.merge(left=scripts,right=practices, left_on='practice', right_on='code').filter(['post_code', 'bnf_name', 'items'])

# Bir bnf, birden fazla posta kodunda olmayacak
# all_data.loc[all_data.groupby('bnf_name')['post_code'].transform(min) == all_data['post_code']]

all_data = all_data.sort_values('post_code')

# Her ayrı post ve bnf için toplam item sayısı
pb_all_data = all_data.groupby(['post_code', 'bnf_name']).sum()

# Post kodlardaki max item hesaplama (eski item yerine gelir)
idx = pb_all_data.groupby(['post_code'])['items'].transform(max) == pb_all_data['items']
df_items_by_region = pb_all_data[idx]['items'] /  pb_all_data.groupby('post_code').sum()['items']

items_by_region = []
for i in range(100):
    x, y = df_items_by_region.index[i]
    z = df_items_by_region[i]
    items_by_region.append((x, y, z))
```

## Dw4 - Miniprojects

```py
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']
unique_post_practices = practices.sort_values('post_code').drop_duplicates('code','first')
scripts_posts = scripts.merge(unique_post_practices, left_on='practice', right_on='code')
unique_chem = chem.drop_duplicates('CHEM SUB')
unique_chem['opioid'] = unique_chem['NAME'].str.contains('|'.join(opioids), case=False)

chem_scripts = scripts_posts.merge(unique_chem, left_on='bnf_code', right_on='CHEM SUB',how='left')
chem_scripts['opioid'].fillna(False, inplace=True)

opioids_per_practice = chem_scripts.groupby('practice')['opioid'].mean()
mean_opioids = chem_scripts['opioid'].mean()
relative_opioids_per_practice = opioids_per_practice - mean_opioids

standard_error_per_practice = chem_scripts['opioid'].std()/np.sqrt(chem_scripts['practice'].value_counts())
opioid_scores = relative_opioids_per_practice/standard_error_per_practice

opioid_scores = opioid_scores.sort_values(ascending=False)
opioid_scores.head()
df = opioid_scores.to_frame().reset_index()
df = df.rename(columns= {0: 'opioid_scores'})
df.index.name = 'index'

total_prescriptions = scripts.groupby('practice').size() 
df1 = total_prescriptions.to_frame().reset_index()
df1 = df1.rename(columns= {0: 'scripts_no'})
df1.index.name = 'index'
merged_chem_f = df.merge(df1,how='left' ,left_on='index', right_on='practice')
uniquepractice1=(practices.sort_values('name')
        .groupby('code').first().reset_index())
uniquepractice1.head()
merged_chem_f_final= merged_chem_f.merge(uniquepractice1,how='left' ,left_on='practice', right_on='code')
merged_chem_f_final.sort_values('opioid_scores',ascending=False)

subset = merged_chem_f_final[['name','opioid_scores','scripts_no']]
tuples = [tuple(x) for x in subset.values]
anomalies=[]
anomalies=tuples[0:100]
```

## Dw5 - Miniprojects

```py
scripts16 = pd.read_csv('./dw-data/201606scripts_sample.csv.gz',compression='gzip', delimiter=',')
drugs_16 = scripts16[['bnf_name', 'items']]
drugs_16 = drugs_16.groupby('bnf_name').count().reset_index()
drugs_16.columns = ['bnf_name', 'count16']

drugs_17 = scripts[['bnf_name', 'items']]
drugs_17 = drugs_17.groupby('bnf_name').count().reset_index()
drugs_17.columns = ['bnf_name', 'count17']

drugs = drugs_16.merge(drugs_17, on='bnf_name', how='inner')
drugs = drugs[drugs['count16']>=50]

drugs.is_copy=False
drugs['growth'] = ((drugs['count17']-drugs['count16'])/drugs['count16'])
drugs = drugs[['bnf_name', 'growth', 'count16']]
drugs.sort_values('growth', ascending=False, inplace=True)
drugs_final = pd.concat([drugs.iloc[:50], drugs.iloc[-50:]], axis=0)

script_growth=drugs_final
```

## Dw6 - Miniprojects

```py
rates = scripts['bnf_code'].value_counts() / scripts['bnf_name'].count()

rates.head()

p = 1. /scripts['bnf_code'].nunique()

mask = rates < .1 * p

rare_codes = rates[mask].index

scripts['rare'] = scripts['bnf_code'].isin(rare_co  des)

scripts.head()

rare_cost_prop = (scripts[scripts['rare']].groupby('practice')['act_cost'].sum()/ scripts.groupby('practice')['act_cost'].sum()).fillna(0)

rare_cost_prop.head()

cost_all = scripts[scripts['rare']]['act_cost'].sum() / scripts['act_cost'].sum()

relative_rare_cost_prop = rare_cost_prop - cost_all

standard_errors = relative_rare_cost_prop.std()  

z_score = relative_rare_cost_prop / standard_errors

z_score = pd.DataFrame(z_score.sort_values(ascending = False))    

z_score.reset_index(inplace = True)

z_score.columns = ['practice', 'z_score']

fin = (practices.groupby(['code'])[['code', 'name']]).head() # 

result = z_score.merge(fin, how = 'left', left_on = 'practice',right_on = 'code').drop('code', axis = 1)

df = result.groupby('practice').first().sort_values('z_score', ascending = False).reset_index()[:100] 

rare_scripts = list(zip(df.practice, df.name, df.z_score))
```


