import data_manager
from flask import Flask, render_template,request

app = Flask(__name__)



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/search-mentor')
def search_mentor():
    return render_template('search_mentor.html')


@app.route('/mentors-with-best-first-name', methods=['POST', 'GET'])
def mentor_names_search():
    # László
    if request.method == 'POST':
        first_name_input = request.form.get('first_name')
    mentor_names = data_manager.get_mentor_names_by_first_name(first_name_input)

    return render_template('mentor_names.html', mentor_names=mentor_names)

@app.route('/mentors-full-name')
def mentor_full_names():
    mentor_full_names = data_manager.get_mentor_full_names()

    return render_template('mentor_names.html', mentor_full_names=mentor_full_names)


@app.route('/mentors-nicknames')
def mentor_nicknames():
    mentor_nicknames = data_manager.get_mentor_nicknames()

    return render_template('mentor_names.html', mentor_nicknames=mentor_nicknames)


@app.route('/search-applicant')
def search_applicant():
    return render_template('search_applicant.html')


@app.route('/applicant-name', methods=['POST', 'GET'])
def applicant_name_search():
    # Carol
    if request.method == 'POST':
        first_name_input = request.form.get('first_name')
    applicant_names = data_manager.get_applicant_name(first_name_input)

    return render_template('mentor_names.html', applicant_names=applicant_names)


@app.route('/search-applicant-by-email')
def search_applicant_by_email():
    return render_template('search_applicant_email.html')


@app.route('/applicant-name-by-email', methods=['POST', 'GET'])
def applicant_name_by_email():
    # @adipiscingenimmi.edu
    if request.method == 'POST':
        email_input = request.form.get('email')
    applicant_names_by_email = data_manager.get_applicant_name_by_email(email_input)

    return render_template('mentor_names.html', applicant_names_by_email=applicant_names_by_email)


@app.route('/insert')
def insert():
    return render_template('insert_form.html')


@app.route('/insert_applicant', methods=['POST', 'GET'])
def insert_applicant_in_database():
    max = data_manager.max_id()[0]['max'] + 1
    if request.method == 'POST':
        first_name_input = request.form.get('first_name')
        last_name_input = request.form.get('last_name')
        phone_input = request.form.get('phone')
        email_input = request.form.get('email')
        code_input =  request.form.get('code')
    data_manager.insert_applicant_in_db(max, first_name_input, last_name_input, phone_input, email_input, code_input)
    add_message='The applicant was added'

    return render_template('mentor_names.html', add_message=add_message)


@app.route('/search-applicant-by-application-code')
def search_applicant_by_application_code():
    return render_template('search_applicant_code.html')


@app.route('/applicant-by-application_code', methods=['POST', 'GET'])
def applicant_by_application_code():
    # 61823
    if request.method == 'POST':
        code_input = request.form.get('code')
    applicant_name_by_application_code = data_manager.get_applicant_by_application_code(code_input)

    return render_template('mentor_names.html', applicant_name_by_application_code=applicant_name_by_application_code)


@app.route('/update')
def update():
    return render_template('update_form.html')


@app.route('/update_applicant', methods=['POST', 'GET'])
def update_applicant_in_database():
    # data_manager.update_applicant_in_db('Jemima', 'Foreman', '003670/223-7459')
    if request.method == 'POST':
        first_name_input = request.form.get('first_name')
        last_name_input = request.form.get('last_name')
        phone_input = request.form.get('phone')
    data_manager.update_applicant_in_db(first_name_input, last_name_input, phone_input)
    update_message = 'The applicant was updated'

    return render_template('mentor_names.html', update_message=update_message)


@app.route('/search-applicant_by_full_name')
def search_applicant_by_full_name():
    return render_template('search_applicant_name.html')


@app.route('/applicant_by_full_name', methods=['POST', 'GET'])
def applicant_by_full_name():
    # applicant_by_name = data_manager.get_applicant_update_data('Jemima', 'Foreman')
    if request.method == 'POST':
        first_name_input = request.form.get('first_name')
        last_name_input = request.form.get('last_name')
    applicant_by_name = data_manager.get_applicant_update_data(first_name_input, last_name_input)

    return render_template('mentor_names.html', applicant_by_name=applicant_by_name)


@app.route('/delete')
def delete():
    return render_template('delete_form.html')

@app.route('/delete_applicant-by-email', methods=['POST', 'GET'])
def delete_applicant_from_database():
    # data_manager.delete_applicant_from_db('@groovecoverage.com')
    if request.method == 'POST':
        email_input = request.form.get('email')
    data_manager.delete_applicant_from_db(email_input)
    delete_message='The applicant was deleted'

    return render_template('mentor_names.html', delete_message=delete_message)


@app.route('/mentors-data')
def mentors_full_data():
    mentor_names_all = data_manager.get_all_mentors_data()

    return render_template('mentor_names.html', mentor_names_all=mentor_names_all)


@app.route('/applicants-data')
def applicants_full_data():
    applicants_names_all = data_manager.get_all_applicants_data()

    return render_template('mentor_names.html', applicants_names_all=applicants_names_all)


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.route('/mentors')
def mentor_and_schools_page():
    mentor_schools = data_manager.get_mentors_and_schools()

    return render_template('mentor_names.html', mentor_schools=mentor_schools)


@app.route('/all-school')
def mentors_and_all_schools_page():
    mentor_all_schools = data_manager.get_mentors_and_schools_right_join()

    return render_template('mentor_names.html', mentor_all_schools=mentor_all_schools)



@app.route('/mentors-by-country')
def mentors_number_by_country():
    mentor_by_country = data_manager.get_mentors_number_by_country()

    return render_template('mentor_names.html', mentor_by_country=mentor_by_country)


@app.route('/contacts')
def schools_contacts():
    school_contact_persons = data_manager.get_contacts()

    return render_template('mentor_names.html', school_contact_persons=school_contact_persons)



if __name__ == '__main__':
    app.run(debug=True)
