from kafka import KafkaProducer
import pandas as pd

def text_producer():
    producer = KafkaProducer(
    bootstrap_servers=['b-1.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092','b-2.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092'],
    client_id='g2-text-producer')
    data = pd.read_csv('/mnt/10ac-batch-6/notebooks/gedion_abebe/Amharic News Dataset.csv')
    random_text = data.sample(n=1)[["headline","category","article"]]
    random_text.reset_index(drop=True, inplace=True)
    if random_text['category'][0] == 'ሀገር አቀፍ ዜና':
        producer.send("g2-national_news", {"headline": random_text['headline'][0].strip(),"category":random_text['category'][0].strip(),"article":random_text['article'][0].strip()})
    elif random_text['category'][0] == 'መዝናኛ':
        producer.send("g2-entertainment", {"headline": random_text['headline'][0].strip(),"category":random_text['category'][0].strip(),"article":random_text['article'][0].strip()})
    elif random_text['category'][0] == 'ቢዝነስ':
        producer.send("g2-business", {"headline": random_text['headline'][0].strip(),"category":random_text['category'][0].strip(),"article":random_text['article'][0].strip()})
    elif random_text['category'][0] == 'ዓለም አቀፍ ዜና':
        producer.send("g2-international_news", {"headline": random_text['headline'][0].strip(),"category":random_text['category'][0].strip(),"article":random_text['article'][0].strip()})
    elif random_text['category'][0] == 'ፖለቲካ':
        producer.send("g2-politics", {"headline": random_text['headline'][0].strip(),"category":random_text['category'][0].strip(),"article":random_text['article'][0].strip()})
    elif random_text['category'][0] == 'ስፖርት':
        producer.send("g2-sport", {"headline": random_text['headline'][0].strip(),"category":random_text['category'][0].strip(),"article":random_text['article'][0].strip()})
    return