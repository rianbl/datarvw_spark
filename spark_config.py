### Aula 1: Spark Básico para Ciência de Dados e Machine Learning

# **Configuração do Ambiente no Google Colab**

## 1. Instalação do Apache Spark e dependências

# Instalar Java 8
!apt-get install openjdk-8-jdk-headless -qq > /dev/null

# Baixar e instalar o Spark
!wget -q https://archive.apache.org/dist/spark/spark-3.2.1/spark-3.2.1-bin-hadoop2.7.tgz
!tar xf spark-3.2.1-bin-hadoop2.7.tgz

# Configurar variáveis de ambiente
import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = "/content/spark-3.2.1-bin-hadoop2.7"

# Instalar o PySpark
!pip install -q pyspark

## 2. Inicialização do Spark

from pyspark.sql import SparkSession

# Criar uma SparkSession
spark = SparkSession.builder.master("local[*]").appName("HelloWorld").getOrCreate()

## 3. Verificar a versão do Spark

print("Versão do Spark:", spark.version)

## 4. Executar o primeiro código (Hello World)

# Criar um DataFrame básico
data = [("Rian", 25), ("Maria", 30), ("João", 22)]

# Definir o esquema das colunas
df = spark.createDataFrame(data, ["Nome", "Idade"])

# Exibir o DataFrame
df.show()

## 5. Conceitos Básicos

"""
- **SparkContext**: É o ponto de entrada para a funcionalidade do Spark.
- **RDD (Resilient Distributed Dataset)**: A estrutura fundamental para o processamento distribuído.
- **SparkSession**: Um ponto de entrada unificado para trabalhar com dados em Spark.
- **DataFrame**: Uma coleção distribuída de dados organizada em colunas, semelhante a uma tabela SQL.
"""

## 6. Encerrando a SparkSession

spark.stop()
