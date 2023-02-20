use masterworks;

create table students(
    studentname varchar(500),
    rollnumber varchar(10) primary key not null,
    study_year int(1),
    gender varchar(6),
    course varchar(100),
    joinedyear varchar(4)
);