create table ���Z��ƪ�
(
�Ǹ� char(9),
�ҵ{�s�� char(5),
���Z int,
primary key(�Ǹ�,�ҵ{�s��),
foreign key(�Ǹ�)references �ǥ͸�ƪ�(�Ǹ�)
on update cascade
on delete cascade,
foreign key(�ҵ{�s��)references �ҵ{��ƪ�(�ҵ{�s��),
)

insert into ���Z��ƪ�
values('110B00001','ACS01','90'),
('110B00001','ACS03','60'),
('110B00002','ACS03','55')