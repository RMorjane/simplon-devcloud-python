create schema elearning;

create table elearning.vcategory(
    vcategory_id serial primary key,
    vcategory_name varchar(50) not null
);

create table elearning.video(
    video_id serial primary key,
    video_name varchar(100) not null,
    video_link varchar(200) not null,
    vcategory_id int references vcategory(vcategory_id)
);