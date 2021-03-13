CREATE DATABASE YoutubeStyledTwitter;
USE YoutubeStyledTwitter;

CREATE TABLE Users (
  id int not null auto_increment,
  email varchar(255) not null,
  picture varchar(255) not null,
  name varchar(255) not null,
  primary key (id)
);