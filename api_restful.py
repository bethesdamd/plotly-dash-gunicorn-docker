# Sample Flask app using flask_restful Resource class, this apparently
# is a best practice.
# Use this as an example of how to build a REST API 


from flask import Flask, render_template, make_response
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

# This just renders Jinja2 templates.  Normally we might organize these outside of the REST API document
class MyTemplate(Resource):
    def get(self):
        # NOTE: must use make_response() or else render_template won't work with flask apps that use the Resource Class
        return make_response(render_template('home.txt'))


api.add_resource(HelloWorld, '/')
api.add_resource(MyTemplate, '/template')


if __name__ == '__main__':
    app.run(debug=True)
