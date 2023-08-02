import mysql.connector
from schemas import User  
# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Lokendar$14",
    database="fastapi"
)

cursor = db.cursor()

# Create User profile table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_profiles (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age INT NOT NULL,
        email VARCHAR(100) NOT NULL,
        gender VARCHAR(10) NOT NULL,
        mobile_number VARCHAR(15) NOT NULL,
        birthday VARCHAR(10) NOT NULL,
        city VARCHAR(100) NOT NULL,
        state VARCHAR(100) NOT NULL,
        country VARCHAR(100) NOT NULL,
        address1 VARCHAR(255) NOT NULL,
        address2 VARCHAR(255),
        UNIQUE (email)
    )
""")
db.commit()

def create_user(user):
    try:
        cursor.execute(
            "INSERT INTO user_profiles (name, age, email, gender, mobile_number, birthday, city, state, country, address1, address2) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (user.name, user.age, user.email, user.gender, user.mobile_number, user.birthday, user.city,
             user.state, user.country, user.address1, user.address2)
        )
        db.commit()
        return True
    except mysql.connector.IntegrityError:
        return False

def update_user(email, user):
    cursor.execute(
        "UPDATE user_profiles "
        "SET name = %s, age = %s, gender = %s, mobile_number = %s, birthday = %s, city = %s, state = %s, "
        "country = %s, address1 = %s, address2 = %s "
        "WHERE email = %s",
        (user.name, user.age, user.gender, user.mobile_number, user.birthday, user.city, user.state,
         user.country, user.address1, user.address2, email)
    )
    db.commit()
    return cursor.rowcount > 0

def delete_user(email):
    cursor.execute("DELETE FROM user_profiles WHERE email = %s", (email,))
    db.commit()
    return cursor.rowcount > 0

def get_user_by_email(email):
    cursor.execute("SELECT * FROM user_profiles WHERE email = %s", (email,))
    user_data = cursor.fetchone()
    if not user_data:
        return None
    return User(
        name=user_data[1],
        age=user_data[2],
        email=user_data[3],
        gender=user_data[4],
        mobile_number=user_data[5],
        birthday=user_data[6],
        city=user_data[7],
        state=user_data[8],
        country=user_data[9],
        address1=user_data[10],
        address2=user_data[11],
    )
