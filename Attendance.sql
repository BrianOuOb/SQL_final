create table 出席資料表
(
出席記錄編號 char(2),
學號 char(9),
班級編號 nvarchar(50) not null,
課程編號 char(5),
點名時間 char(20),
出席狀態 nvarchar(50) not null,
備註 nvarchar(50) null,
primary key(學號,課程編號),
foreign key(學號)references 學生資料表(學號)
on update cascade
on delete cascade,
foreign key(課程編號)references 課程資料表(課程編號),
)

insert into 出席資料表
values('A1','110B00001','資工A','ACS01','2023-01-01 10:02:15','出席',''),
('A1','110B00001','資工A','ACS03','2023-01-02 15:02:15','未出席','病假')
