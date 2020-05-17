# 19_homework

## 문제1

```
CREATE TABLE friends (
	id INTEGER PRIMARY KEY,
	name TEXT NOT NULL,
	location TEXT NOT NULL
);
```



## 문제2

```
INSERT INTO friends (name, location) VALUES ('Justin', 'Seoul'), ('Simon', 'New York'), ('Chang', 'Las Vegas'), ('John', 'Sydney');
```



## 문제3

```
ALTER TABLE friends ADD COLUMN married INTEGER;
```



## 문제4

```
UPDATE friends SET location='LA', married=1 WHERE id=1;
UPDATE friends SET married=0 WHERE id=2;
UPDATE friends SET location='LasVegas', married=0 WHERE id=3;
UPDATE friends SET married=1 WHERE id=4;
```

