create table 成績資料表
(
學號 char(9),
課程編號 char(5),
成績 int,
primary key(學號,課程編號),
foreign key(學號)references 學生資料表(學號)
on update cascade
on delete cascade,
foreign key(課程編號)references 課程資料表(課程編號),
)

insert into 成績資料表
values('110B00001','ACS01','90'),
('110B00001','ACS03','60'),
('110B00002','ACS03','55')