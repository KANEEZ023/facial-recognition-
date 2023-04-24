import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("ServiceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime-c9021-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "2101864001":
        {
            "NAME":"S.AKHILA",
            "COURSE":"MCA",
            "STARTING_YEAR":2021,
            "TOTAL_ATTENDANCE":32,
            "STANDING":"Good",
            "YEAR":2,
            "LAST_ATTENDANCE_TIME":"2023-01-07 00:54:34"
        },
    "2101864005":
        {
            "NAME":"SRI HARSHA",
            "COURSE":"MCA",
            "STARTING_YEAR":2021,
            "TOTAL_ATTENDANCE":35,
            "STANDING":"Good",
            "YEAR":2,
            "LAST_ATTENDANCE_TIME":"2023-01-07 00:54:34"
        },
    "2101864012":
        {
            "NAME":"KANEEZ SULTANA",
            "COURSE":"MCA",
            "STARTING_YEAR":2021,
            "TOTAL_ATTENDANCE":36,
            "STANDING":"Good",
            "YEAR":2,
            "LAST_ATTENDANCE_TIME":"2023-01-07 00:54:34"
        },
    "2101864021":
        {
            "NAME":"K.SUPRIYA",
            "COURSE":"MCA",
            "STARTING_YEAR":2021,
            "TOTAL_ATTENDANCE":33,
            "STANDING":"Good",
            "YEAR":2,
            "LAST_ATTENDANCE_TIME":"2023-01-07 00:54:34"
        },
    "2101864027":
        {
            "NAME":"JAYACHANDRA",
            "COURSE":"MCA",
            "STARTING_YEAR":2021,
            "TOTAL_ATTENDANCE":37,
            "STANDING":"Good",
            "YEAR":2,
            "LAST_ATTENDANCE_TIME":"2023-01-07 00:54:34"
        },
    "2101864035":
        {
            "NAME":"SANA KOUSAR",
            "COURSE":"MCA",
            "STARTING_YEAR":2021,
            "TOTAL_ATTENDANCE":34,
            "STANDING":"Good",
            "YEAR":2,
            "LAST_ATTENDANCE_TIME":"2023-01-07 00:54:34"
        }
}

for key,value in data.items():
    ref.child(key).set(value)
