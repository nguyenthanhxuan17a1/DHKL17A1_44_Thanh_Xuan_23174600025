import pandas as pd
data = {
    'Team': ['Spain', 'Italy', 'Germany', 'Portugal', 'England', 'France', 'Greece', 'Czech Republic', 'Denmark', 'Sweden', 'Croatia', 'Ukraine', 'Poland', 'Russia', 'Netherlands', 'Ireland'],
    'Goals': [12, 6, 10, 6, 5, 3, 5, 4, 4, 5, 4, 2, 2, 5, 2, 1],
    'Yellow Cards': [11, 16, 10, 12, 5, 6, 9, 7, 4, 6, 9, 5, 7, 6, 5, 3],
    'Red Cards': [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    'Shooting Accuracy': ['50%', '45%', '60%', '55%', '53%', '48%', '43%', '40%', '42%', '47%', '49%', '38%', '35%', '46%', '39%', '34%']
}
df = pd.DataFrame(data)
df.to_csv('euro2012.csv')
df = pd.read_csv('euro2012.csv')
print(df.head()) 
#1.In gái trị cột Goals
print(df['Goals'])
#2. Có bao nhiêu đội tham gia Euro 2012?
teams_count = df['Team'].nunique()
print("Số đội tham gia Euro 2012:", teams_count)
#3. In thông tin của Euro2012.
print(df.info())
#4. Tạo 1 DataFrame mới từ euro12 chỉ chứa 3 cột: Team, Yellow Cards, Red Cards.
df_discipline = df[['Team', 'Yellow Cards', 'Red Cards']]
print(df_discipline)
#5. Sắp xếp discipline giảm dần theo 2 cột: Red Cards, Yellow Cards.
df_discipline_sorted = df_discipline.sort_values(by=['Red Cards', 'Yellow Cards'], ascending=False)
print(df_discipline_sorted)
#6.a Tính trung bình số thẻ Yellow Cards.
yellow_cards_mean = df['Yellow Cards'].mean()
print("Trung bình thẻ vàng:", yellow_cards_mean)
#6.b Lọc các đội đã ghi hơn 6 bàn thắng.
teams_more_than_6_goals = df[df['Goals'] > 6]
print(teams_more_than_6_goals)
#7.In các đội có tên bắt đầu bằng chữ “G”.
teams_start_with_g = df[df['Team'].str.startswith('G')]
print(teams_start_with_g)
#8. In 7 cột đầu của Euro 2012.
print(df.iloc[:, :7])
#9. In tất cả các cột, trừ 3 cột cuối.
print(df.iloc[:, :-3])
#10. In các cột Team, Goals, Shooting Accuracy, Yellow Cards, Red Cards.
print(df[['Team', 'Goals', 'Shooting Accuracy', 'Yellow Cards', 'Red Cards']])
# 11.Lọc các đội "England", "Italy", và "Russia" và chọn cột "Team" và "Shooting Accuracy"
selected_teams = df[df['Team'].isin(['England', 'Italy', 'Russia'])][['Team', 'Shooting Accuracy']]
print(selected_teams)
