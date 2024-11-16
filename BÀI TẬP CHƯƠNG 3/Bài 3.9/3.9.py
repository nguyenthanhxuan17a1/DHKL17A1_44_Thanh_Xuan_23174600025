import pandas as pd
data = pd.read_csv('D:\\BÀI TẬP\\BÀI TẬP CHƯƠNG 3\\Bài 3.9\\euro2012.csv',delimiter=',')
df = pd.DataFrame(data)
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
