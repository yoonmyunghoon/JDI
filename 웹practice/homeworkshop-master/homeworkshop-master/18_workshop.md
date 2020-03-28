# 18_workshop

## 문제1

```
CREATE TABLE bands (
	id INTEGER PRIMARY KEY, 
	name TEXT NOT NULL,
	debut INTEGER NOT NULL
);
INSERT INTO bands (name, debut) VALUES ('Queen', 1973), ('Coldplay', 1998), ('MCR', 2001);

```

## 문제2

```
SELECT id, name FROM bands;
```



## 문제3

```
SELECT name FROM bands WHERE debut<2000;
```

