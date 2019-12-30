import data_manager
from flask import Flask, render_template,request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mentors-with-best-first-name')
def mentor_names():
    # We get back dictionaries here (for details check 'database_common.py')
    mentor_names = data_manager.get_mentor_names_by_first_name('László')

    return render_template('mentor_names.html', mentor_names=mentor_names)

@app.route('/mentors-full-name')
def mentor_full_names():
    mentor_full_names = data_manager.get_mentor_full_names()

    return render_template('mentor_names.html', mentor_full_names=mentor_full_names)


@app.route('/mentors-nicknames')
def mentor_nicknames():
    mentor_nicknames = data_manager.get_mentor_nicknames()

    return render_template('mentor_names.html', mentor_nicknames=mentor_nicknames)


@app.route('/applicant-name')
def applicant_name():
    applicant_names = data_manager.get_applicant_name('Carol')

    return render_template('mentor_names.html', applicant_names=applicant_names)


@app.route('/applicant-name-by-email')
def applicant_name_by_email():
    applicant_names_by_email = data_manager.get_applicant_name_by_email('@adipiscingenimmi.edu')

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

    return render_template('mentor_names.html')


@app.route('/applicant-by-application_code')
def applicant_by_application_code():
    applicant_name_by_application_code = data_manager.get_applicant_by_application_code('54823')

    return render_template('mentor_names.html', applicant_name_by_application_code=applicant_name_by_application_code)


@app.route('/update_applicant')
def update_applicant_in_database():
    data_manager.update_applicant_in_db('Jemima', 'Foreman', '003670/223-7459')

    return render_template('mentor_names.html')


@app.route('/applicant_by_full_name')
def applicant_by_full_name():
    applicant_by_name = data_manager.get_applicant_update_data('Jemima', 'Foreman')

    return render_template('mentor_names.html', applicant_by_name=applicant_by_name)


@app.route('/delete_applicant-by-email')
def delete_applicant_from_database():
    data_manager.delete_applicant_from_db('mauriseu.net')

    return render_template('mentor_names.html')


@app.route('/mentors-data')
def mentors_full_data():
    mentor_names_all = data_manager.get_all_mentors_data()

    return render_template('mentor_names.html', mentor_names_all=mentor_names_all)


@app.route('/applicants-data')
def applicants_full_data():
    applicants_names_all = data_manager.get_all_applicants_data()

    return render_template('mentor_names.html', applicants_names_all=applicants_names_all)



if __name__ == '__main__':
    app.run(debug=True)
