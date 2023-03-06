import pandas

data = pandas.read_csv('/Users\galahad\Desktop\proga\MST_XWAP_SEX_AGE_CBR_NB_A.csv.gz')
(row_count, col_count) = data.shape

data = data[['ref_area', 'sex', 'time', 'obs_value', 'classif1', 'classif2']]

print("Количество строк: " + str(row_count) + "\nКоличество колонок: " + str(col_count))

print("MAX трудоспособного населения")
print(data[
          (data.classif1 == 'AGE_AGGREGATE_TOTAL') &
          (data.sex == 'SEX_T') &
          (data.classif2 == 'CBR_BIR_TOTAL')
          ].obs_value.max())

print("MAX трудоспособного населения MALE")
print(data[
          (data.classif1 == 'AGE_AGGREGATE_TOTAL') &
          (data.sex == 'SEX_M') &
          (data.classif2 == 'CBR_BIR_TOTAL')
          ].obs_value.max())

print("MAX трудоспособного населения FEMALE")
print(data[
          (data.classif1 == 'AGE_AGGREGATE_TOTAL') &
          (data.sex == 'SEX_F') &
          (data.classif2 == 'CBR_BIR_TOTAL')
          ].obs_value.max())

print("Топ-10 по женскому трудоспособному населению за 2020")
print(data[
          (data.classif1 == 'AGE_AGGREGATE_TOTAL') &
          (data.sex == 'SEX_F') &
          (data.classif2 == 'CBR_BIR_TOTAL') &
          (data.time == 2020)
          ].sort_values(by='obs_value', ascending=False)[:10])

print("Топ-10 НЕместному трудоспособному населению за 2020")
print(data[
          (data.classif1 == 'AGE_AGGREGATE_TOTAL') &
          (data.sex == 'SEX_T') &
          (data.classif2 == 'CBR_BIR_FOREIGN') &
          (data.time == 2020)
          ].sort_values(by='obs_value', ascending=False)[:10])

print("Топ-10 женского трудоспособного населения за 2020 (возраст 25-34)")
print(data[
          (data.classif1 == 'AGE_10YRBANDS_Y25-34') &
          (data.sex == 'SEX_F') &
          (data.time == 2020)
          ].sort_values(by='obs_value', ascending=False)[:10])
