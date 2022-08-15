from flask import Flask
from redis import Redis
app = Flask(__name__)
redis= Redis(host='redis',port=6379)


@app.route('/')
def main():
    redis.incr('hits')
    return 'KEEP LEARING , KEEO VISITING IN PAGE TO INCEARSE COUNT %s ' % redis.get('hits')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)