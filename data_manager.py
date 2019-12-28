import database_common


@database_common.connection_handler
def get_mentor_names_by_first_name(cursor, first_name):
    cursor.execute("""
                    SELECT first_name, last_name FROM mentors
                    WHERE first_name = %(first_name)s ORDER BY first_name;
                   """,
                   {'first_name': first_name})
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_mentor_full_names(cursor):
    cursor.execute("""
                    SELECT first_name, last_name FROM mentors;
                   """)
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_mentor_nicknames(cursor):
    cursor.execute("""
                    SELECT nick_name FROM mentors;
                   """)
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_applicant_name(cursor, first_name):
    cursor.execute("""
                    SELECT CONCAT(first_name, ' ', last_name) AS full_name, phone_number
                    FROM applicants WHERE first_name = %(first_name)s ORDER BY first_name;
                   """,
                   {'first_name': first_name})
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_applicant_name_by_email(cursor, email):
    cursor.execute("""
                    SELECT CONCAT(first_name, ' ', last_name) AS full_name, phone_number
                    FROM applicants WHERE email LIKE '%{email}';
                   """.format(email=email))
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def insert_applicant_in_db(cursor, id, first_name, last_name, email, phone_number, application_code):
    cursor.execute("""
                    INSERT INTO applicants (id, first_name, last_name, email, phone_number, application_code)
                    VALUES ({id}, '{first_name}', '{last_name}', '{email}', '{phone_number}', {application_code});
                   """.format(id=id, first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, application_code=application_code))
    # names = cursor.fetchall()
    # return names

@database_common.connection_handler
def max_id(cursor):
    cursor.execute("""SELECT MAX(id) FROM applicants""")
    maxim_id = cursor.fetchall()
    return maxim_id


@database_common.connection_handler
def get_applicant_by_application_code(cursor, application_code):
    cursor.execute("""
                    SELECT *
                    FROM applicants WHERE application_code = %(application_code)s;
                   """,
                   {'application_code': application_code})
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def update_applicant_in_db(cursor, first_name, last_name, phone_number):
    cursor.execute("""UPDATE applicants 
                    SET phone_number='{phone_number}' 
                    WHERE first_name='{first_name}' AND last_name='{last_name}';
                    """.format(phone_number=phone_number, first_name=first_name, last_name=last_name))
    # names = cursor.fetchall()
    # return names


@database_common.connection_handler
def get_applicant_update_data(cursor, first_name, last_name):
    cursor.execute("""
                    SELECT *
                    FROM applicants 
                    WHERE first_name='{first_name}' AND last_name='{last_name}';
                   """.format(first_name=first_name, last_name=last_name))
    names = cursor.fetchall()
    return names
