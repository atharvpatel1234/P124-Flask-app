from flask import Flask,jsonify,request

app=Flask(__name__)

contact=[
    {
        'contact':9987644456,
        'Name':'Raju',
        'done':False,
        'id':1
    },
    {
        'contact':9876543222,
        'Name':'Rahul',
        'done':False,
        'id':2
    }
]

@app.route("/")
def hello_world():
    return "Hello World"


@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data!"
        },400)

    contact={
        'id':tasks[-1]['id']+1,
        'Name':request.json['Name'],
        'contact':request.json.get('contact',""),
        'done':False

    }
    tasks.append(task)
    return jsonify({
        "status":"Success",
        "message":"Task added Succesfully"
    })



if(__name__ == "__main__"):
    app.run(debug=True)