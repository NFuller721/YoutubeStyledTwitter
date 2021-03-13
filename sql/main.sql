CREATE DATABASE YoutubeStyledTwitter;
USE YoutubeStyledTwitter;

CREATE TABLE Users (
  id int not null auto_increment,
  email varchar(255) not null,
  picture varchar(255) not null,
  name varchar(255) not null,
  primary key (id)
);

CREATE TABLE Posts (
  id int not null auto_increment,
  postText varchar(255) not null,
  userID int not null,
  likes int not null,
  primary key (id)
)
