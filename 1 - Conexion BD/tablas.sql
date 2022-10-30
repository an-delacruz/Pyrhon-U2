drop database if exists unidad2;

create database unidad2;

\c unidad2;

create table if not exists generos (
    id serial primary key ,
    nombre varchar(50) not null
);

create table if not exists autores (
    id serial primary key,
    nombre varchar(50) not null,
    apellido varchar(50) not null,
    nacionalidad varchar(50) not null
);

create table if not exists libros(
    id serial primary key,
    titulo varchar(50) not null,
    anio_publicacion int not null,
    genero integer not null references generos(id),
    autor integer not null references autores(id)
);
