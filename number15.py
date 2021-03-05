import random
import json

def generate():
    with open('options.json', 'r') as f:
        d = json.loads(f.read())

        return (
            f"Number {random.randint(1,20)}: "
            f"{random.choice(d['places'])} "
            f"{random.choice(d['parts'])} "
            f"{random.choice(d['food'])}"
        )

if __name__=='__main__':
    print(generate())
