from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]


# Helper function to reduce duplicate "find by id" logic
def find_event(event_id):
    return next((e for e in events if e.id == event_id), None)


# Helper function to generate the next available id
def next_id():
    return max((e.id for e in events), default=0) + 1


# Root route - JSON welcome message
@app.route("/")
def index():
    return jsonify({"message": "Welcome to the Event Management API"})


# GET /events - return all events as a JSON array
@app.route("/events", methods=["GET"])
def get_events():
    return jsonify([event.to_dict() for event in events]), 200


# POST /events - Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()

    # Input validation: title is required
    if not data or "title" not in data or not data["title"]:
        return jsonify({"error": "Missing required field: title"}), 400

    new_event = Event(next_id(), data["title"])
    events.append(new_event)

    return jsonify(new_event.to_dict()), 201


# PATCH /events/<id> - Update the title of an event
@app.route("/events/<int:id>", methods=["PATCH"])
def update_event(id):
    event = find_event(id)

    if event is None:
        return jsonify({"error": f"Event with id {id} not found"}), 404

    data = request.get_json()

    if not data or "title" not in data or not data["title"]:
        return jsonify({"error": "Missing required field: title"}), 400

    event.title = data["title"]

    return jsonify(event.to_dict()), 200


# DELETE /events/<id> - Remove an event from the list
@app.route("/events/<int:id>", methods=["DELETE"])
def delete_event(id):
    event = find_event(id)

    if event is None:
        return jsonify({"error": f"Event with id {id} not found"}), 404

    events.remove(event)

    return jsonify({"message": f"Event {id} deleted successfully"}), 200


if __name__ == "__main__":
    app.run(debug=True)


# from flask import Flask, jsonify, request

# app = Flask(__name__)

# # Simulated data
# class Event:
#     def __init__(self, id, title):
#         self.id = id
#         self.title = title

#     def to_dict(self):
#         return {"id": self.id, "title": self.title}

# # In-memory "database"
# events = [
#     Event(1, "Tech Meetup"),
#     Event(2, "Python Workshop")
# ]

# # TODO: Task 1 - Define the Problem
# # Create a new event from JSON input
# @app.route("/events", methods=["POST"])
# def create_event():
#     # TODO: Task 2 - Design and Develop the Code

#     # TODO: Task 3 - Implement the Loop and Process Each Element

#     # TODO: Task 4 - Return and Handle Results
#     pass

# # TODO: Task 1 - Define the Problem
# # Update the title of an existing event
# @app.route("/events/<int:event_id>", methods=["PATCH"])
# def update_event(event_id):
#     # TODO: Task 2 - Design and Develop the Code

#     # TODO: Task 3 - Implement the Loop and Process Each Element

#     # TODO: Task 4 - Return and Handle Results
#     pass

# # TODO: Task 1 - Define the Problem
# # Remove an event from the list
# @app.route("/events/<int:event_id>", methods=["DELETE"])
# def delete_event(event_id):
#     # TODO: Task 2 - Design and Develop the Code

#     # TODO: Task 3 - Implement the Loop and Process Each Element

#     # TODO: Task 4 - Return and Handle Results
#     pass

# if __name__ == "__main__":
#     app.run(debug=True)
