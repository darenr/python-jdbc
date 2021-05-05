# python-jdbc

Experiments with using JDBC from python jupyter lab in a Conda environment

## Conda Enviroment

conda create -n python-jdbc python=3.7
conda activate python-jdbc

conda install -c conda-forge openjdk
conda install -c conda-forge jupyterlab=2.3
conda install -c conda-forge JayDeBeApi

The sqlite JDBC driver was downloaded from: https://repo1.maven.org/maven2/org/xerial/sqlite-jdbc/3.34.0/sqlite-jdbc-3.34.0.jar


## Test the code w/ Jshell

jshell --class-path jar/sqlite-jdbc-3.34.0.jar


```bash
$ jshell --class-path jar/sqlite-jdbc-3.34.0.jar
|  Welcome to JShell -- Version 11.0.9.1
|  For an introduction type: /help intro

jshell> /open SQLiteSample.java

jshell> SQLiteSample.main(new String[0])
name = Alice
name = Bob

jshell>

```

You can go old-school retro and compile the java code thus:

```bash
$ javac --class-path jar/sqlite-jdbc-3.34.0.jar  SQLiteSample.java
$ java --class-path jar/sqlite-jdbc-3.34.0.jar:.  SQLiteSample
name = Alice
name = Bob
```

## From Python

```python
$ python connect-with-jdbc-to-sqlite.py
(1, 'Alice')
(1, 'Bob')
```
