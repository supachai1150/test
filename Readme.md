ขั้นตอนการ build
------------------------------------------------------------------------------------------------------------------------------
from flask import Flask, request, jsonify # เรียกใช้โมดูล Flask และโมดูลอื่น ๆ ที่เกี่ยวข้อง เพื่อใช้ในการสร้างและปรับแต่ง API

app = Flask(__name__) # สร้างแอปพลิเคชัน Flask โดยใช้ชื่อของไฟล์เป็นชื่อของแอปพลิเคชัน

def fibonacci(n): # นิยามฟังก์ชัน fibonacci สำหรับคำนวณลำดับฟีโบนัชชี โดยรับพารามิเตอร์ n ซึ่งเป็นจำนวนสมาชิกที่ต้องการในลำดับ

fib_sequence = [0, 1] # สร้างรายการเริ่มต้นสำหรับลำดับฟีโบนัชชีที่มีสมาชิกแรก 2 ตัว.

for _ in range(n - 2):  # วนลูปเพื่อคำนวณลำดับฟีโบนัชชี โดยใช้ลูป for และคำสั่ง range เพื่อสร้างสมาชิกเพิ่มเข้าไปในลำดับ

fib_sequence.append(fib_sequence[-1] + fib_sequence[-2]) # เพิ่มสมาชิกใหม่ในลำดับฟีโบนัชชี โดยบวกสมาชิกที่สองล่าสุดและสมาชิกล่าสุดของลำดับ
    
return fib_sequence # ส่งคืนลำดับฟีโบนัชชีที่คำนวณได้

@app.route('/api/v1/test/<int:member_count>', methods=['GET']) # กำหนดเส้นทางของ API สำหรับการรับข้อมูลและคำนวณลำดับฟีโบนัชชี โดย <int:member_count> คือพารามิเตอร์ที่รับค่าจำนวนสมาชิกที่ต้องการในลำดับฟีโบนัชชี

def get_fibonacci(member_count): # เป็นฟังก์ชันที่ใช้สร้างและส่งคืน JSON ที่ระบุลำดับฟีโบนัชชีและผลรวมของสมาชิกในลำดับตามจำนวนสมาชิกที่ระบุมาใน URL ของ API 
    
if 1 <= member_count <= 100: # เช็คเงื่อนไขว่าจำนวนสมาชิกที่ระบุต้องอยู่ในช่วง 1 ถึง 100

fib_list = fibonacci(member_count) # เรียกใช้ฟังก์ชัน fibonacci เพื่อคำนวณลำดับฟีโบนัชชี

fib_sum = sum(fib_list)   # คำนวณผลรวมของสมาชิกในลำดับฟีโบนัชชี

response = { 'member-count': member_count,'sequence': fib_list,'total': fib_sum} # สร้างตัวแปร response ในรูปแบบของ JSON ที่มีคุณสมบัติตามที่ระบุในคำถาม

return jsonify(response) # ส่งค่า JSON ในรูปแบบของการตอบสนอง
    else: 
return jsonify('error') # ส่งค่า JSON ในรูปแบบของข้อผิดพลาดเมื่อจำนวนสมาชิกไม่อยู่ในช่วงที่กำหนด

if __name__ == '__main__': # เช็คว่าไฟล์ถูกเรียกโดยตรงหรือไม่ (ไม่ได้ถูก import โดยไฟล์อื่น)

app.run(debug=True) # เริ่มให้แอปพลิเคชัน Flask ทำงาน และเปิดโหมด debug เพื่อให้แสดงข้อผิดพลาดในกรณีเกิดข้อผิดพลาด

----------------------------------------------------------------------------------------------------------------------------
ขั้นตอนการ Run

#เข้าโปรแกรม Vscode จากนั้นเปิด Terminal แล้วนำตำแหน่งไปยังโฟลเดอร์ที่มีไฟล์ .py ที่คุณสร้าง // ใช้คำสั่งต่อไปนี้เพื่อรันแอปพลิเคชัน Flask: python your_app_file_name.py
ู#หรือ กด คลิกขวาที่ช่องว่างของหน้าโค๊ดนั้นแล้วกดไปที่ Run python -> Run python file in Terminal 
#เมื่อแอปพลิเคชันถูกรัน คุณสามารถเข้าถึง API ผ่าน URL เช่น http://localhost:5000/api/v1/test/8 เพื่อดูผลลัพท์ที่ได้
