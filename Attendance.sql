create table �X�u��ƪ�
(
�X�u�O���s�� char(2),
�Ǹ� char(9),
�Z�Žs�� nvarchar(50) not null,
�ҵ{�s�� char(5),
�I�W�ɶ� char(20),
�X�u���A nvarchar(50) not null,
�Ƶ� nvarchar(50) null,
primary key(�Ǹ�,�ҵ{�s��),
foreign key(�Ǹ�)references �ǥ͸�ƪ�(�Ǹ�)
on update cascade
on delete cascade,
foreign key(�ҵ{�s��)references �ҵ{��ƪ�(�ҵ{�s��),
)

insert into �X�u��ƪ�
values('A1','110B00001','��uA','ACS01','2023-01-01 10:02:15','�X�u',''),
('A1','110B00001','��uA','ACS03','2023-01-02 15:02:15','���X�u','�f��')
