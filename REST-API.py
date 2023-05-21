from flask import Flask, jsonify, request, Blueprint
from flask.views import MethodView
import sqlite3

app = Flask(__name__)

class MachineResource(MethodView):
    def __init__(self):
        self.connection = sqlite3.connect('multi_system_installer.db')
        self.cursor = self.connection.cursor()

    def get(self):
        self.cursor.execute("SELECT * FROM machines;")
        machine_list = self.cursor.fetchall()        
        return jsonify(machine_list)

    def post(self):
        data = request.get_json()
        machine_id = data["machine_id"]
        ip_address = data["ip_address"]
        port_no = data["port_no"]
        username = data["username"]
        os_type = data["os_type"]
        path = data["path"]
        password = data["password"]
        email = data["email"]
        machine_type = data["machine_type"]
        query = \
        """
        INSERT INTO machines (machine_id, ip_address, port_no, username, os_type, path, password, email, machine_type)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
        """
        self.cursor.execute(query, (machine_id, ip_address, port_no, username, os_type, path, password, email, machine_type))
        self.connection.commit()
        return jsonify({'message': 'Machine entry created successfully'})

    def delete(self, machine_id):
        query = "DELETE FROM machines WHERE machine_id = ?;"
        self.cursor.execute(query, (machine_id, ))
        self.connection.commit()
        return jsonify({'message': 'Machine entry deleted successfully'})


class ScheduledJobResource(MethodView):
    def __init__(self):
        self.connection = sqlite3.connect('multi_system_installer.db')
        self.cursor = self.connection.cursor()

    def get(self):        
        self.cursor.execute("SELECT * FROM scheduled_jobs;")
        scheduled_job_list = self.cursor.fetchall()
        return jsonify(scheduled_job_list)

    def post(self):
        data = request.get_json()
        job_id = data["job_id"]
        machine_id = data["machine_id"]
        software_id = data["software_id"]
        scheduled_time = data["scheduled_time"]
        query = \
        """
        INSERT INTO scheduled_jobs (job_id, machine_id, software_id, scheduled_time) 
        VALUES (?, ?, ?, ?,);
        """
        self.cursor.execute(query, (job_id, machine_id, software_id, scheduled_time))
        self.connection.commit()
        return jsonify({'message': 'Scheduled job entry created successfully'})

    def delete(self, job_id):
        query = "DELETE FROM scheduled_jobs WHERE job_id = ?;"
        self.cursor.execute(query, (job_id, ))
        self.connection.commit()
        return jsonify({'message': 'Scheduled job entry deleted successfully'})

class CompletedJobResource(MethodView):
    def __init__(self):
        self.connection = sqlite3.connect('multi_system_installer.db')
        self.cursor = self.connection.cursor()

    def get(self):
        self.cursor.execute("SELECT * FROM completed_jobs;")
        completed_job_list = self.cursor.fetchall()
        return jsonify(completed_job_list)
    
class SoftwareResource(MethodView):
    def __init__(self):
        self.connection = sqlite3.connect('multi_system_installer.db')
        self.cursor = self.connection.cursor()

    def get(self):
        self.cursor.execute("SELECT * FROM software_repository;")
        software_list = self.cursor.fetchall()
        return jsonify(software_list)

    def post(self):
        data = request.get_json()
        software_id = data["software_id"]
        name = data["name"]
        version = data["version"]
        description = data["description"]
        os_type = data["os_type"]
        extension = data["extension"]
        query = \
        """
        INSERT INTO software_repository (software_id, name, version, description, os_type, extension) 
        VALUES (?, ?, ?, ?, ?, ?);
        """
        self.cursor.execute(query, (software_id, name, version, description, os_type, extension))
        self.connection.commit()
        return jsonify({'message': 'Software entry created successfully'})

    def delete(self, software_id):
        query = "DELETE FROM software_repository WHERE software_id = ?;"
        self.cursor.execute(query, (software_id, ))
        self.connection.commit()
        return jsonify({'message': 'Software entry deleted successfully'})


machine_blueprint = Blueprint('machine', __name__)
machine_view = MachineResource.as_view('machine_api')
machine_blueprint.add_url_rule('/machines', methods=['GET'], view_func=machine_view)
machine_blueprint.add_url_rule('/machines', methods=['POST'], view_func=machine_view)
machine_blueprint.add_url_rule('/machines/<int:machine_id>', methods=['DELETE'], view_func=machine_view)

scheduled_job_blueprint = Blueprint('scheduled_job', __name__)
scheduled_job_view = ScheduledJobResource.as_view('scheduled_job_api')
scheduled_job_blueprint.add_url_rule('/scheduled-jobs', methods=['GET'], view_func=scheduled_job_view)
scheduled_job_blueprint.add_url_rule('/scheduled-jobs', methods=['POST'], view_func=scheduled_job_view)
scheduled_job_blueprint.add_url_rule('/scheduled-jobs/<int:job_id>', methods=['DELETE'], view_func=scheduled_job_view)

completed_job_blueprint = Blueprint('completed_job', __name__)
completed_job_view = CompletedJobResource.as_view('completed_job_api')
completed_job_blueprint.add_url_rule('/completed-jobs', methods=['GET'], view_func=completed_job_view)

software_blueprint = Blueprint('software', __name__)
software_view = SoftwareResource.as_view('software_api')
software_blueprint.add_url_rule('/software', methods=['GET'], view_func=software_view)
software_blueprint.add_url_rule('/software', methods=['POST'], view_func=software_view)
software_blueprint.add_url_rule('/software/<int:software_id>', methods=['DELETE'], view_func=software_view)

app.register_blueprint(machine_blueprint)
app.register_blueprint(scheduled_job_blueprint)
app.register_blueprint(completed_job_blueprint)
app.register_blueprint(software_blueprint)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
