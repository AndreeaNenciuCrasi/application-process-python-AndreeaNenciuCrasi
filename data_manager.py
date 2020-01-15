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
                    VALUES ({id}, '{first_name}', '{last_name}', '{phone_number}', '{email}', {application_code});
                   """.format(id=id, first_name=first_name, last_name=last_name, phone_number=phone_number, email=email, application_code=application_code))
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


@database_common.connection_handler
def delete_applicant_from_db(cursor, email):
    cursor.execute("""DELETE FROM applicants WHERE email LIKE '%{email}';
                    """.format(email=email))
    # names = cursor.fetchall()
    # return names


@database_common.connection_handler
def get_all_mentors_data(cursor):
    cursor.execute("""
                    SELECT * FROM mentors;
                   """)
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_all_applicants_data(cursor):
    cursor.execute("""
                    SELECT * FROM applicants;
                   """)
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_mentors_and_schools(cursor):
    cursor.execute(""" SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
                       FROM mentors JOIN schools
                       ON mentors.city=schools.city
                       ORDER BY mentors.id; """)
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_mentors_and_schools_right_join(cursor):
    cursor.execute(""" SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
                       FROM schools LEFT JOIN mentors
                       ON mentors.city=schools.city
                       ORDER BY mentors.id; """)
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_mentors_number_by_country(cursor):
    cursor.execute("""SELECT COUNT(mentors.first_name) AS "Count", schools.country
                    FROM mentors JOIN schools
                    ON mentors.city=schools.city
                    GROUP BY schools.country;""")
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_contacts(cursor):
    cursor.execute("""SELECT schools.name, CONCAT(mentors.first_name, ' ', mentors.last_name) AS "Name"
                    FROM schools LEFT JOIN mentors
                    ON mentors.id=schools.contact_person
                    ORDER BY schools.name;""")
    names = cursor.fetchall()
    return names

