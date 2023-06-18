import faust
from urllib.parse import urlparse


app = faust.App('top_domain', broker='kafka://kafka1:9092')
topic = app.topic('browser-history', key_type=str, value_type=str, value_serializer='raw')
table = app.Table("domains", key_type=str, value_type=int, partitions=3, default=int)


def get_domain(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    return domain.split(".")[-1]


@app.agent(topic)
async def processor(stream):
    async for message in stream:
        domain = get_domain(message)
        table[domain] += 1
        print(sorted(table.items(), key=lambda x: x[1], reverse=True)[:5])


if __name__ == '__main__':
    app.main()
