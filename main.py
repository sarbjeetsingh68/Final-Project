from flask import Flask, jsonify
app = Flask(__name__)
courses = [
{
'id': '0',
'name': "Sarbjeet Singh",
'email': "rahul@gmail.com",
'gender': "Male"
},
{
'id': '1',
'name': "Nariendar Modi",
'email': "Jayne_Kuhic@sydney.com",
'gender': "Male"
},
{
'id': '2',
'name': "babu rao",
'email': "Nikita@garfield.biz",
'gender': "Male"
},
{
'id': '3',
'name': "Amit Shah",
'email': "Lew@alysha.tv",
'gender': "Male"
},
{
'id': '4',
'name': "shakti kapoor",
'email': "Hayden@althea.biz",
'gender': "Male"
},
{
'id': '5',
'name': "Naruto",
'email': "Presley.Mueller@myrl.com",
'gender': "Male"
},
{
'id': '6',
'name': "emma watson",
'email': "Dallas@ole.me",
'gender': "Female"
},
{
'id': '7',
'name': "Harry potter",
'email': "Mallory_Kunze@marie.org",
'gender': "Male"
},
{
'id': '8',
'name': "Kylie",
'email': "Meghan_Littel@rene.us",
'gender': "Female"
},
{
'id': '9',
'name': "baby brown",
'email': "Carmen_Keeling@caroline.name",
'gender': "Female"
}]

@app.route('/')
def hello_world():
    return 'TO get dataset type http://127.0.0.1:5000/courses'

@app.route('/courses', methods=['GET'])
def get():
    return jsonify({'courses':courses})

@app.route("/courses/<int:course_id>",methods=['GET'])
def get_course(course_id):
    return jsonify({'course': courses[course_id]})


if __name__ == '__main__':
    app.run(debug=True)