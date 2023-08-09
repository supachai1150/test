from flask import Flask, request, jsonify

app = Flask(__name__)

def fibonacci(n):
    fib_sequence = [0, 1]
    for _ in range(n - 2):  
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

@app.route('/api/v1/test/<int:member_count>', methods=['GET'])
def get_fibonacci(member_count):
    if 1 <= member_count <= 100:
        fib_list = fibonacci(member_count)
        fib_sum = sum(fib_list)  

        response = {
            'member-count': member_count,
            'sequence': fib_list,
            'total': fib_sum
        }

        return jsonify(response)
    else:
        return jsonify({'error': 'จำนวนสมาชิกต้องอยู่ระหว่าง 1 และ 100'})

if __name__ == '__main__':
    app.run(debug=True)
